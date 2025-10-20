import os
import sys
import psycopg2
import hashlib
from datetime import datetime
from pathlib import Path
from tkinter import filedialog

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# -----------------------
# Пути к файлам и ресурсы
# -----------------------
def get_app_path():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

APP_PATH = get_app_path()
TOKEN_PATH = os.path.join(APP_PATH, "mycreds.txt")
CLIENT_SECRETS_PATH = resource_path("../client_secrets.json")

# -----------------------
# Конфигурация базы (Shared Pooler)
# -----------------------
DB_CONFIG = {
    'host': 'aws-1-us-east-2.pooler.supabase.com',  # Shared Pooler host
    'port': 6543,                                   # Port pooler
    'database': 'postgres',                         # Database
    'user': 'postgres.uhmuxhzsdojtruaisihm',       # User
    'password': 'xdun$N/qB%QJ77/'               # Пароль
}

# -----------------------
# Подключение к базе
# -----------------------
def get_connection():
    return psycopg2.connect(**DB_CONFIG)

# -----------------------
# Пользователи
# -----------------------
def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def create_account(user_name: str, password: str):
    if not user_name.strip():
        return 'некорректный логин'
    if not password.strip():
        return 'некорректный пароль'

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_users FROM users WHERE name=%s", (user_name,))
    if cur.fetchone():
        cur.close()
        conn.close()
        return False

    cur.execute("INSERT INTO users(name, password) VALUES (%s, %s) RETURNING id_users",
                (user_name, hash_password(password)))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

def login_system(user_name: str, input_password: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_users, password FROM users WHERE name=%s", (user_name,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return False, 0
    user_id, stored_password = row
    if hash_password(input_password) == stored_password:
        return True, user_id
    return False, 0

# -----------------------
# Предметы
# -----------------------
def create_subject(new_subject: str):
    new_subject = new_subject.capitalize()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM subject WHERE name=%s", (new_subject,))
    if not cur.fetchone():
        cur.execute("INSERT INTO subject(name) VALUES (%s)", (new_subject,))
        conn.commit()
    cur.close()
    conn.close()

def all_name_subject(id_user: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_subject FROM downloads WHERE id_user=%s", (id_user,))
    id_subjects = [row[0] for row in cur.fetchall()]
    if not id_subjects:
        cur.close()
        conn.close()
        return []

    placeholders = ','.join(['%s'] * len(id_subjects))
    cur.execute(f"SELECT name FROM subject WHERE id_subject IN ({placeholders})", id_subjects)
    names = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return names

# -----------------------
# Выбор файлов/папок
# -----------------------
def choose_file():
    return filedialog.askopenfilename()

def choose_folder():
    return filedialog.askdirectory()

# -----------------------
# Google Drive
# -----------------------
def setup_gauth():
    gauth = GoogleAuth()
    gauth.settings['get_refresh_token'] = True
    gauth.settings['oauth_scope'] = [
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
    ]
    gauth.LoadClientConfigFile(CLIENT_SECRETS_PATH)

    if os.path.exists(TOKEN_PATH):
        gauth.LoadCredentialsFile(TOKEN_PATH)
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(TOKEN_PATH)
    return gauth

def upload_to_drive():
    folder_id = "1zVT6Fr6LzzqzXWO9RJdl8d89uQIIJew-"  # Папка на Google Drive
    file_path = choose_file()
    gauth = setup_gauth()
    drive = GoogleDrive(gauth)

    file_name = os.path.basename(file_path)
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}] if folder_id else []})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    return [f"https://drive.google.com/file/d/{gfile['id']}/view", file_name]

# -----------------------
# Дата
# -----------------------
def date_now():
    return datetime.now()

# -----------------------
# Загрузка файлов в БД
# -----------------------
def download_inf_file_in_db(id_user: int, subject_name: str, date_note_str: str):
    conn = get_connection()
    cur = conn.cursor()

    subject_name = subject_name.capitalize()
    cur.execute("SELECT id_subject FROM subject WHERE name=%s", (subject_name,))
    row = cur.fetchone()
    if row:
        subject_id = row[0]
    else:
        create_subject(subject_name)
        cur.execute("SELECT id_subject FROM subject WHERE name=%s", (subject_name,))
        subject_id = cur.fetchone()[0]

    link, file_name = map(str, upload_to_drive())
    dt = date_now()
    date_note = datetime.strptime(date_note_str, "%d/%m/%Y").date()

    cur.execute("""INSERT INTO downloads (id_user, id_subject, date_upload, date_note, link, name_file)
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                (id_user, subject_id, dt, date_note, link, file_name))
    conn.commit()
    cur.close()
    conn.close()
    return link, dt, file_name

# -----------------------
# Скачивание файла из БД
# -----------------------
def upload_file_from_db(subject: str, name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_subject FROM subject WHERE name=%s", (subject,))
    rows = cur.fetchall()
    if not rows:
        cur.close()
        conn.close()
        return False
    subject_ids = [row[0] for row in rows]

    placeholders = ','.join(['%s'] * len(subject_ids))
    cur.execute(f"SELECT link FROM downloads WHERE id_subject IN ({placeholders}) AND name_file=%s",
                (*subject_ids, name))
    links = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    if links:
        return links
    return False

# -----------------------
# Все файлы
# -----------------------
def all_name_files():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name_file FROM downloads")
    files = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return files

# -----------------------
# Google Drive: скачивание
# -----------------------
def extract_file_id(url: str):
    if '/d/' in url:
        return url.split('/d/')[1].split('/')[0]
    elif 'id=' in url:
        return url.split('id=')[1].split('&')[0]
    return None

def download_from_gdrive(url: str, file_name: str):
    save_folder = choose_folder()
    Path(save_folder).mkdir(parents=True, exist_ok=True)
    file_id = extract_file_id(url)
    if not file_id:
        raise ValueError("Неверный URL Google Drive")

    gauth = setup_gauth()
    drive = GoogleDrive(gauth)
    gfile = drive.CreateFile({'id': file_id})
    save_path = os.path.join(save_folder, gfile['title'])
    gfile.GetContentFile(save_path)
    return save_path

# -----------------------
# Информация о файлах пользователя
# -----------------------
def all_info_files_user(id_user: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT d.id_subject, d.name_file, d.link, d.date_note, d.date_upload, s.name
                   FROM downloads d
                   JOIN subject s ON d.id_subject = s.id_subject
                   WHERE d.id_user=%s""", (id_user,))
    data = [[row[5], row[1], row[2], row[3], row[4]] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return data

# -----------------------
# Удаление файла
# -----------------------
def delete_file(id_user, name_subject, name_file, link, date):
    date_note = datetime.strptime(date, "%Y-%m-%d").date()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_subject FROM subject WHERE name=%s", (name_subject,))
    subject_id = cur.fetchone()[0]

    cur.execute("""DELETE FROM downloads 
                   WHERE id_user=%s AND id_subject=%s AND name_file=%s AND link=%s AND date_note=%s""",
                (id_user, subject_id, name_file, link, date_note))
    conn.commit()
    cur.close()
    conn.close()

    gauth = setup_gauth()
    drive = GoogleDrive(gauth)
    file_id = extract_file_id(link)
    gfile = drive.CreateFile({'id': file_id})
    gfile.Delete()