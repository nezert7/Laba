import sqlite3
import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from datetime import datetime
from tkinter import filedialog
import hashlib
import gdown

connect = sqlite3.connect('test.db')
cursor = connect.cursor()
# cursor.execute("""DROP TABLE IF EXISTS SUBJECT""")
cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                            ID_USER INT,
                                            ID_SUBJECT INT,     
                                            DATE_UPLOAD DATETIME,
                                            DATE_NOTE DATE,
                                            LINK TEXT,
                                            NAME_FILE TEXT
                                        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS USERS( 
                                            ID_USERS INTEGER PRIMARY KEY AUTOINCREMENT,     
                                            NAME TEXT UNIQUE,
                                            PASSWORD TEXT
                                        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS SUBJECT( 
                                            ID_SUBJECT INTEGER PRIMARY KEY AUTOINCREMENT,     
                                            NAME TEXT UNIQUE
                                        )""")


def hash_password(password: str):  # Функция для хеширования паролей
    return hashlib.sha256(password.encode()).hexdigest()


def create_account(user_name: str, password: str):
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS( 
                                                ID_USERS INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                NAME TEXT UNIQUE,
                                                PASSWORD TEXT
                                            )""")
    all_users = cursor.execute("""SELECT NAME FROM USERS""")
    all_users = [str(x)[2:-3] for x in all_users]
    if user_name == '':
        return 'некорректный логин'
    if password == '':
        return 'некорректный пароль'
    if user_name not in all_users:
        password = hash_password(password)
        cursor.execute("""INSERT INTO USERS(NAME, PASSWORD)
                                VALUES(?, ?)""", (user_name, password))
        connect.commit()
        return True
    else:
        return False


def login_system(user_name: str, input_password: str):  # Функция для проверки логина и пароля под которыми входит пользователь
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS( 
                                                    ID_USERS INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                    NAME TEXT UNIQUE,
                                                    PASSWORD TEXT
                                                )""")
    input_password = hash_password(input_password)
    all_users_password = [x for x in cursor.execute("""SELECT NAME, PASSWORD FROM USERS""")]
    for user, password in all_users_password:
        if user_name == user:
            if input_password == password:
                id_user = \
                    [str(x)[1:-2] for x in cursor.execute(f"""SELECT ID_USERS FROM USERS WHERE NAME='{user_name}'""")][
                        0]
                connect.commit()
                return True, int(
                    id_user)  # разрешаем доступ, всё хорошо и возвращаем id пользователя под именем которого зашли
    return False, 0  # здесь нужна функция, которая выведет подобную ошибку на экран


def upload_to_drive():  # Функция загружает файл на мой гугл драйв
    folder_id = "1zVT6Fr6LzzqzXWO9RJdl8d89uQIIJew-"
    file_path = choose_file()
    gauth = GoogleAuth()
    gauth.settings['get_refresh_token'] = True
    gauth.settings['oauth_scope'] = [
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive']
    # Попытка авторизации из локального файла токена
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Если токена нет — это единственный раз откроет браузер
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Если токен устарел — обновим
        gauth.Refresh()
    else:
        gauth.Authorize()
    # Сохраняем токен для последующих запусков
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    file_name = os.path.basename(file_path)
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}] if folder_id else []})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    return [f"https://drive.google.com/file/d/{gfile['id']}/view", file_name]


def date_now():  # Здесь забирается актуальное время
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    return dt_string


def all_name_subject(id_user):
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT ID_SUBJECT FROM DOWNLOADS WHERE ID_USER = ?""", (id_user,))
    id_subject = [row[0] for row in cursor.fetchall()]
    placeholders = ','.join(['?'] * len(id_subject))
    cursor.execute(f"""SELECT NAME FROM SUBJECT WHERE ID_SUBJECT IN ({placeholders})""", id_subject)
    names = [row[0] for row in cursor.fetchall()]
    return names


def create_subject(new_subject):  # Функция для добавления в db новый предметов
    cursor.execute("SELECT 1 FROM SUBJECT WHERE NAME = ?", (new_subject.capitalize(),))
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("INSERT INTO SUBJECT(NAME) VALUES (?)", (new_subject.capitalize(),))
        connect.commit()


def choose_file():  # Открываем проводник
    file_path = filedialog.askopenfilename()
    return file_path


def choose_folder():
    file_path = filedialog.askdirectory()
    return file_path


def download_inf_file_in_db(id_user: int, subject_name: str, date_note: str):  # Функция для загрузки ссылки на файл и всей информации про файл в db
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS SUBJECT( 
                                                ID_SUBJECT INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                NAME TEXT UNIQUE
                                            )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                                ID_USER INT,
                                                ID_SUBJECT INT,     
                                                DATE_UPLOAD DATETIME,
                                                DATE_NOTE DATE,
                                                LINK TEXT,
                                                NAME_FILE TEXT
                                            )""")
    all_subject = [str(x)[2:-3] for x in cursor.execute(f"""SELECT NAME FROM SUBJECT""")]
    if subject_name.capitalize() not in all_subject:
        create_subject(subject_name.capitalize())
    subject_id = int(
        [str(x)[1:-2] for x in cursor.execute(f"""SELECT ID_SUBJECT FROM SUBJECT WHERE NAME = '{subject_name.capitalize()}'""")][0])
    link, file_name = map(str, upload_to_drive())
    cursor.execute("""INSERT INTO DOWNLOADS
                                    VALUES(?, ?, ?, ?, ?, ?)""",
                   (id_user, subject_id, date_now(), date_note, link, file_name))
    connect.commit()


def upload_file_from_db(subject, name):  # Здесь мы выгружаем из db ссылку на файл который хотим открыть, присутствует сортировка по имени и дате
    # date_create_start = input()  # Дата от которой ищем, нужна отдельная функция для ввода
    # date_create_end = input()  # Дата до которой ищем, нужна отдельная функция для ввода
    # Название предмета ссылку на конспект которого мы хотим получить, нужна отдельная функция для ввода
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS SUBJECT( 
                                                    ID_SUBJECT INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                    NAME TEXT UNIQUE
                                                )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                                    ID_USER INT,
                                                    ID_SUBJECT INT,     
                                                    DATE_UPLOAD DATETIME,
                                                    DATE_NOTE DATE,
                                                    LINK TEXT,
                                                    NAME_FILE TEXT
                                                )""")
    subjects_id = [int(str(x)[1:-2]) for x in
                   cursor.execute(f"""SELECT ID_SUBJECT FROM SUBJECT WHERE NAME = '{subject}'""")]
    files_search_1 = [str(x)[2:-3] for x in
                      cursor.execute("""SELECT LINK FROM DOWNLOADS WHERE ID_SUBJECT IN (?)""", subjects_id)]
    # if date_create_start == '' and date_create_end != '':
    #     date_create_start = date_create_end
    # elif date_create_start != '' and date_create_end == '':
    #     date_create_end = date_create_start
    # elif date_create_start == '' and date_create_end == '':
    #     date_create_start = '01/01/1900'
    #     date_create_end = '01/01/2050'
    # files_search_3 = [str(x)[2:-3] for x in cursor.execute(
    #     f"""SELECT LINK FROM DOWNLOADS WHERE DATE_NOTE BETWEEN {date_create_start} AND {date_create_end}""")]
    files_search_2 = [str(x)[2:-3] for x in
                      cursor.execute(f"""SELECT LINK FROM DOWNLOADS WHERE NAME_FILE = '{name}'""")]
    if subject and name:
        final_files = set(files_search_1) & set(files_search_2)
    elif subject:
        final_files = files_search_1
    else:
        final_files = files_search_2
    connect.commit()
    if final_files:
        return final_files
    else:
        return False


def all_name_files():
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                                ID_USER INT,
                                                ID_SUBJECT INT,     
                                                DATE_UPLOAD DATETIME,
                                                DATE_NOTE DATE,
                                                LINK TEXT,
                                                NAME_FILE TEXT
                                            )""")
    return [str(x)[2:-3] for x in cursor.execute(f"""SELECT NAME_FILE FROM DOWNLOADS""")]


def extract_file_id(url: str):
    if '/d/' in url:
        return url.split('/d/')[1].split('/')[0]
    elif 'id=' in url:
        return url.split('id=')[1].split('&')[0]
    else:
        return None


def download_from_gdrive(url: str, file_name: str):
    # Извлекаем ID файла
    file_id = extract_file_id(url)
    url = f"https://drive.google.com/uc?id={file_id}"
    save_path = os.path.join(choose_folder(), file_name)

    gdown.download(url, save_path, quiet=False)


def all_info_files_user(id_user: int):
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                                ID_USER INT,
                                                ID_SUBJECT INT,     
                                                DATE_UPLOAD DATETIME,
                                                DATE_NOTE DATE,
                                                LINK TEXT,
                                                NAME_FILE TEXT
                                            )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS SUBJECT( 
                                                ID_SUBJECT INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                NAME TEXT UNIQUE
                                            )""")
    sp = [list(x) for x in cursor.execute(f"""SELECT ID_SUBJECT, NAME_FILE, LINK, DATE_NOTE FROM DOWNLOADS WHERE ID_USER = '{id_user}'""")]
    for x in sp:
        x[0] = ''.join([str(x)[2:-3] for x in cursor.execute(f"""SELECT NAME FROM SUBJECT WHERE ID_SUBJECT = '{x[0]}'""")])
    return sp


def delete_file(id_user, name_subject, name_file, link, date):
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                                ID_USER INT,
                                                ID_SUBJECT INT,     
                                                DATE_UPLOAD DATETIME,
                                                DATE_NOTE DATE,
                                                LINK TEXT,
                                                NAME_FILE TEXT
                                            )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS SUBJECT( 
                                                ID_SUBJECT INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                NAME TEXT UNIQUE
                                            )""")
    cursor.execute("SELECT ID_SUBJECT FROM SUBJECT WHERE NAME = ?", (name_subject,))
    id_subject = [row[0] for row in cursor.fetchall()][0]
    cursor.execute("""
        DELETE FROM DOWNLOADS 
        WHERE ID_USER = ? 
        AND ID_SUBJECT = ? 
        AND NAME_FILE = ? 
        AND LINK = ? 
        AND DATE_NOTE = ?
    """, (id_user, id_subject, name_file, link, date))
    connect.commit()
    gauth = GoogleAuth()
    gauth.settings['get_refresh_token'] = True
    gauth.settings['oauth_scope'] = [
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive']
    # Попытка авторизации из локального файла токена
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Если токена нет — это единственный раз откроет браузер
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Если токен устарел — обновим
        gauth.Refresh()
    else:
        gauth.Authorize()
    # Сохраняем токен для последующих запусков
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)
    file_id = extract_file_id(link)
    gfile = drive.CreateFile({'id': file_id})
    gfile.Delete()
    cursor.execute("SELECT ID_SUBJECT FROM DOWNLOADS")
    id_subject = 2
    all_id_subject = [row[0] for row in cursor.fetchall()]
    if id_subject not in all_id_subject:
        cursor.execute("""
                DELETE FROM SUBJECT 
                WHERE ID_SUBJECT = ? 
                    """, (id_subject,))
    connect.commit()
# Пример использования
# download_from_gdrive()
# download_inf_file_in_db(k, subject_name, date_note)
# print(upload_file_from_db())
# create_account()
# download_inf_file_in_db(1, 'ОРГ', '13.10.2025')
# print(upload_file_from_db('ОРГ', 'qeqe'))
# print(all_name_files())
# upload_to_drive()
# print(all_name_subject(1))