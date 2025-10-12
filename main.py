import sqlite3
import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from datetime import datetime
import hashlib

connect = sqlite3.connect('test.db')
cursor = connect.cursor()
# cursor.execute("""DROP TABLE IF EXISTS USERS""")
cursor.execute("""CREATE TABLE IF NOT EXISTS DOWNLOADS( 
                                            ID_USER INT,
                                            ID_SUBJECT INT,     
                                            DATE_UPLOAD DATETIME,
                                            DATE_NOTE DATE,
                                            LINK TEXT,
                                            NAME_FILE VARCHAR(15)
                                        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS USERS( 
                                            ID_USERS INTEGER PRIMARY KEY AUTOINCREMENT,     
                                            NAME TEXT UNIQUE,
                                            PASSWORD VARCHAR(15)
                                        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS SUBJECT( 
                                            ID_SUBJECT INTEGER PRIMARY KEY AUTOINCREMENT,     
                                            NAME TEXT UNIQUE
                                        )""")


def hash_password(password): # Функция для хеширования паролей
    return hashlib.sha256(password.encode()).hexdigest()


def create_account(user_name, password):
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS( 
                                                ID_USERS INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                NAME TEXT UNIQUE,
                                                PASSWORD VARCHAR(15)
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
        return 'Такой пользователь уже существует'  # здесь нужна функция, которая выведет подобную ошибку на экран


def login_system(user_name, input_password):  # Функция для проверки логина и пароля под которыми входит пользователь
    connect = sqlite3.connect('test.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS( 
                                                    ID_USERS INTEGER PRIMARY KEY AUTOINCREMENT,     
                                                    NAME TEXT UNIQUE,
                                                    PASSWORD VARCHAR(15)
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


def upload_to_drive(file_path, folder_id):  # Функция загружает файл на мой гугл драйв
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # откроет браузер для авторизации
    drive = GoogleDrive(gauth)
    file_name = os.path.basename(file_path)
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}] if folder_id else []})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    return [f"https://drive.google.com/file/d/{gfile['id']}/view", file_name]


# k = login_system()  # это id пользователя, который в системе
k = 1


# subject_name = input(
#     "Введите имя предмета: ") # имя предмета, файл который будем добавлять, надо сделать отдельную функцию для ввода с приложения
# date_note = input(
#     "Введите дату: ") # дата конспекта, не когда он был загружен, а именно когда был урок например, тоже нужна отдельная функция для ввода с приложения


def date_now():  # Здесь забирается актуальное время
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    return dt_string


def create_subject():  # Функция для добавления в db новый предметов
    new_subject = input(
        'Введите предмет который хотите добавить: ')  # Здесь должна быть функция, возвращающая предмет, который пользователь хочет добавить
    cursor.execute("SELECT 1 FROM SUBJECT WHERE NAME = ?", (new_subject,))
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("INSERT INTO SUBJECT(NAME) VALUES (?)", (new_subject,))
        return 'Successful'
    else:
        return 'Error такой предмет уже существует'


def download_inf_file_in_db(id_user, subject_name,
                            date_note):  # Функция для загрузки ссылки на файл и всей информации про файл в db
    subject_id = int(
        [str(x)[1:-2] for x in cursor.execute(f"""SELECT ID_SUBJECT FROM SUBJECT WHERE NAME = '{subject_name}'""")][0])
    link, file_name = map(str, upload_to_drive("C:\\Users\\kosty\\Downloads\\Электрические схемы Jeep WK.pdf",
                                               folder_id="1zVT6Fr6LzzqzXWO9RJdl8d89uQIIJew-"))  # Здесь file_path пользователь должен указать сам или автоматически при выборе файла
    cursor.execute("""INSERT INTO DOWNLOADS
                                    VALUES(?, ?, ?, ?, ?, ?)""",
                   (id_user, subject_id, date_now(), date_note, link, file_name))


def upload_file_from_db():  # Здесь мы выгружаем из db ссылку на файл который хотим открыть, присутствует сортировка по имени и дате
    date_create_start = input()  # Дата от которой ищем, нужна отдельная функция для ввода
    date_create_end = input()  # Дата до которой ищем, нужна отдельная функция для ввода
    subject = input()  # Название предмета ссылку на конспект которого мы хотим получить, нужна отдельная функция для ввода
    subjects_id = [int(str(x)[1:-2]) for x in
                   cursor.execute(f"""SELECT ID_SUBJECT FROM SUBJECT WHERE NAME LIKE '%{subject}%'""")]
    files_search_1 = [str(x)[2:-3] for x in
                      cursor.execute("""SELECT LINK FROM DOWNLOADS WHERE ID_SUBJECT IN (?)""", subjects_id)]
    # name = [] # В разработке...
    if date_create_start == '' and date_create_end != '':
        date_create_start = date_create_end
    elif date_create_start != '' and date_create_end == '':
        date_create_end = date_create_start
    elif date_create_start == '' and date_create_end == '':
        date_create_start = '01/01/1900'
        date_create_end = '01/01/2050'
    files_search_2 = [str(x)[2:-3] for x in cursor.execute(
        f"""SELECT LINK FROM DOWNLOADS WHERE DATE_NOTE BETWEEN {date_create_start} AND {date_create_end}""")]
    if files_search_1 and files_search_2:
        final_files = set(files_search_1) & set(files_search_2)
    elif files_search_1:
        final_files = files_search_1
    else:
        final_files = files_search_2
    return final_files
    # if name == '':
    #     name = cursor.execute("""SELECT NAME_FILE FROM DOWNLOADS""")
    #     name = [str(x)[2:-3] for x in name]


# create_subject()
# download_inf_file_in_db(k, subject_name, date_note)
# print(upload_file_from_db())
# create_account()
connect.commit()
