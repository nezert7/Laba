import sys
import webbrowser  # чтоб ссылки открывались

from PyQt6.QtWidgets import QApplication, QLineEdit, \
    QMessageBox, QTableWidgetItem, \
    QApplication, QMainWindow, QTableWidgetItem, \
    QLineEdit, QMessageBox, QMessageBox
from PyQt6.QtCore import Qt

from database.db import create_account, login_system, all_name_subject, \
    all_info_files_user, download_inf_file_in_db, delete_file, download_from_gdrive

from app_windows.log_window import Ui_MainWindow
from app_windows.reg_window import Ui_LogWindow
from app_windows.main_window import Ui_Con_Window

USER_ID = 0


class Main_Window(QMainWindow):  # окно с выбором предмета, основное окно приложения
    def __init__(self):
        super().__init__()
        self.conspect = []
        self.ui = Ui_Con_Window()
        self.ui.setupUi(self)

        # Настройки окна
        self.setGeometry(400, 100, 1394, 791)
        self.setWindowTitle("Главное окно")

        # Подключение сигналов
        self.ui.filter_label.currentTextChanged.connect(self.apply_filter)
        self.ui.pushButton_4.clicked.connect(self.download_selected)  # кнопка "Скачать"
        self.ui.delete_action.clicked.connect(self.delete_selected)  # кнопка "Удалить"
        self.ui.btn_add.clicked.connect(self.add_conspect)  # кнопка "Добавить"
        self.ui.pushButton_6.clicked.connect(self.go_back)  # кнопка "Назад"

        self.ui.table.cellClicked.connect(self.on_cell_clicked)

        # Загружаем данные
        self.load_conspects()
        self.update_filter_combo()

        self.show()

    # 🟡 Загружаем данные конспектов пользователя
    def load_conspects(self):
        self.conspect.clear()
        sp = all_info_files_user(USER_ID)
        for x in sp:
            self.conspect.append({
                'предмет': x[0],
                'ссылка': x[2],
                'дата занятия': x[3],
                'дата загрузки': x[4],
                'имя файла': x[1],
            })
        self.populate_table()

    # 🟡 Заполняем таблицу
    def populate_table(self, filter_subject=None):
        self.ui.table.setRowCount(0)
        row = 0
        for e in self.conspect:
            if filter_subject and filter_subject != "Выберите предмет из списка" and e['предмет'] != filter_subject:
                continue

            self.ui.table.insertRow(row)
            self.ui.table.setItem(row, 0, QTableWidgetItem(e['предмет']))

            link_item = QTableWidgetItem(e['ссылка'])
            link_item.setForeground(Qt.GlobalColor.blue)
            link_item.setToolTip(f"Нажмите чтобы открыть: {e['ссылка']}")
            self.ui.table.setItem(row, 1, link_item)
            self.ui.table.setItem(row, 4, QTableWidgetItem(str(e['имя файла'])))
            self.ui.table.setItem(row, 2, QTableWidgetItem(str(e['дата занятия'])))
            self.ui.table.setItem(row, 3, QTableWidgetItem(str(e['дата загрузки'])))
            row += 1

    # 🟡 Обновление фильтра
    def update_filter_combo(self):
        current = self.ui.filter_label.currentText()
        self.ui.filter_label.clear()
        self.ui.filter_label.addItem("Выберите предмет из списка")

        subjects = set(item for item in all_name_subject(USER_ID))
        for s in sorted(subjects):
            self.ui.filter_label.addItem(s)

        if current in [self.ui.filter_label.itemText(i) for i in range(self.ui.filter_label.count())]:
            self.ui.filter_label.setCurrentText(current)
        else:
            self.ui.filter_label.setCurrentIndex(0)

    # 🟡 Применение фильтра
    def apply_filter(self, subject):
        if subject == "Выберите предмет из списка":
            self.populate_table()
        else:
            self.populate_table(subject)

    # 🟡 Клик по ссылке
    def on_cell_clicked(self, row, column):
        if column == 1:
            item = self.ui.table.item(row, column)
            if item and item.text().startswith(('http://', 'https://')):
                reply = QMessageBox.question(
                    self,
                    'Открыть ссылку',
                    f'Вы хотите открыть ссылку:\n{item.text()}',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.Yes:
                    try:
                        webbrowser.open(item.text())
                        msg = QMessageBox(self)
                        msg.setWindowTitle('Успешно')
                        msg.setText('Ссылка открывается в браузере')
                        msg.setIcon(QMessageBox.Icon.Information)
                        msg.setStyleSheet("""
                                        QMessageBox {
                                            background-color: #121212;
                                        }
                                        QLabel {
                                            color: white;
                                            font-size: 14px;
                                        }
                                        QPushButton {
                                            background-color: #333;
                                            color: white;
                                            border-radius: 6px;
                                            padding: 6px;
                                        }
                                        QPushButton:hover {
                                            background-color: #555;
                                        }
                                    """)
                        msg.exec()
                    except Exception as e:
                        msg = QMessageBox(self)
                        msg.setWindowTitle('Ошибка')
                        msg.setText(f'Не удалось открыть ссылку: {str(e)}')
                        msg.setIcon(QMessageBox.Icon.Critical)
                        msg.setStyleSheet("""
                                        QMessageBox {
                                            background-color: #121212;
                                        }
                                        QLabel {
                                            color: white;
                                            font-size: 14px;
                                        }
                                        QPushButton {
                                            background-color: #333;
                                            color: white;
                                            border-radius: 6px;
                                            padding: 6px;
                                        }
                                        QPushButton:hover {
                                            background-color: #555;
                                        }
                                    """)
                        msg.exec()

    # 🟡 Добавление нового конспекта
    def add_conspect(self):
        subject = self.ui.subject_name.text().strip()
        date = self.ui.age.text().strip()

        if not subject or not date:
            msg = QMessageBox(self)
            msg.setWindowTitle('Ошибка')
            msg.setText('Заполните все поля')
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStyleSheet("""
                            QMessageBox {
                                background-color: #121212;
                            }
                            QLabel {
                                color: white;
                                font-size: 14px;
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border-radius: 6px;
                                padding: 6px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
            msg.exec()
            return

        # Добавляем в базу
        link, dt, file_name = download_inf_file_in_db(USER_ID, subject, date)

        # Обновляем локально
        self.conspect.append({
            'предмет': subject,
            'ссылка': link,
            'дата занятия': date,
            'дата загрузки': dt,
            'имя файла': file_name
        })
        self.update_filter_combo()
        self.apply_filter(self.ui.filter_label.currentText())

        self.ui.subject_name.clear()
        self.ui.age.clear()

    # 🟡 Удаление выбранной строки
    def delete_selected(self):
        row = self.ui.table.currentRow()
        if row < 0:
            msg = QMessageBox(self)
            msg.setWindowTitle('Ошибка')
            msg.setText('Выберите строку для удаления')
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStyleSheet("""
                            QMessageBox {
                                background-color: #121212;
                            }
                            QLabel {
                                color: white;
                                font-size: 14px;
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border-radius: 6px;
                                padding: 6px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
            msg.exec()
            return

        subject = self.ui.table.item(row, 0).text()
        name_file = self.ui.table.item(row, 4).text()
        link = self.ui.table.item(row, 1).text()
        date = self.ui.table.item(row, 2).text()

    #Настройка цвета для кнопки удаления
    def ask_delete(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Удаление")
        msg.setText(f'Удалить конспект по предмету "{subject}"?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        msg.setStyleSheet("""
            QMessageBox {
                background-color: #121212;
            }
            QPushButton {
                background-color: #333;
                color: white;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

        msg.exec()
        return
        
        if reply == QMessageBox.StandardButton.Yes:
            delete_file(USER_ID, subject, name_file, link, date)
            self.conspect.pop(row)
            self.ui.table.removeRow(row)
            self.update_filter_combo()

    # 🟡 Скачать выбранный файл (пример)
    def download_selected(self):
        row = self.ui.table.currentRow()
        if row < 0:
            msg = QMessageBox(self)
            msg.setWindowTitle('Ошибка')
            msg.setText('Выберите конспект для скачивания')
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStyleSheet("""
                            QMessageBox {
                                background-color: #121212;
                            }
                            QLabel {
                                color: white;
                                font-size: 14px;
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border-radius: 6px;
                                padding: 6px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
            msg.exec()
            return
        file_name = self.ui.table.item(row, 4).text()
        link = self.ui.table.item(row, 1).text()
        msg = QMessageBox(self)
        msg.setWindowTitle('Скачивание')
        msg.setText(f'Скачивание файла:\n{file_name}')
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStyleSheet("""
                        QMessageBox {
                            background-color: #121212;
                        }
                        QLabel {
                            color: white;
                            font-size: 14px;
                        }
                        QPushButton {
                            background-color: #333;
                            color: white;
                            border-radius: 6px;
                            padding: 6px;
                        }
                        QPushButton:hover {
                            background-color: #555;
                        }
                    """)
        msg.exec()
        download_from_gdrive(link, file_name)

    # 🟡 Назад
    def go_back(self):
        self.hide()
        self.first_window = First_Window()
        self.first_window.show()


class Log_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LogWindow()
        self.ui.setupUi(self)

        # Базовые настройки окна
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("Регистрация")

        # Подключение сигналов
        self.ui.log_button.clicked.connect(self.process_registration)
        self.ui.exit_button.clicked.connect(self.goto_ScreenFirst)
        self.ui.toggle_button.clicked.connect(self.toggle_password_visibility)
        self.ui.toggle_button_2.clicked.connect(self.toggle_password_visibility2)

        self.show()

    def validate_registration_data(self):  # Проверка данных
        username = self.ui.input_logr.text().strip()
        password = self.ui.input_pasr.text().strip()
        password_confirm = self.ui.input_pasr2.text().strip()

        if not username or not password or not password_confirm:
            return False, "Все поля должны быть заполнены"
        elif password != password_confirm:
            return False, "Пароли не совпадают"
        elif not create_account(username, password):
            return False, "Такой пользователь уже существует"
        return True, ""

    def process_registration(self):  # Обработка нажатия кнопки
        is_valid, message = self.validate_registration_data()
        if is_valid:
            msg = QMessageBox(self)
            msg.setWindowTitle("Успех")
            msg.setText("Аккаунт успешно создан")
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStyleSheet("""
                            QMessageBox {
                                background-color: #121212;
                            }
                            QLabel {
                                color: white;
                                font-size: 14px;
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border-radius: 6px;
                                padding: 6px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
            msg.exec()
            self.goto_ScreenFirst()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Ошибка регистрации")
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStyleSheet("""
                            QMessageBox {
                                background-color: #121212;
                            }
                            QLabel {
                                color: white;
                                font-size: 14px;
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border-radius: 6px;
                                padding: 6px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
            msg.exec()

    def goto_ScreenFirst(self):  # Возврат на окно авторизации
        self.hide()
        self.screen_first = First_Window()
        self.screen_first.show()

    def toggle_password_visibility(self):
        if self.ui.input_pasr.echoMode() == QLineEdit.EchoMode.Password:
            self.ui.input_pasr.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.input_pasr.setEchoMode(QLineEdit.EchoMode.Password)

    def toggle_password_visibility2(self):
        if self.ui.input_pasr2.echoMode() == QLineEdit.EchoMode.Password:
            self.ui.input_pasr2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.input_pasr2.setEchoMode(QLineEdit.EchoMode.Password)


class First_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Базовые настройки окна
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("Авторизация")

        # Подключение сигналов
        self.ui.ot_button.clicked.connect(self.process_login)
        self.ui.log_button.clicked.connect(self.gotoScreen_log)
        self.ui.toggle_button.clicked.connect(self.toggle_password_visibility)

        self.show()

    def validate_login_data(self):  # Проверяет валидность данных для авторизации
        global USER_ID
        username = self.ui.input_logi.text().strip()
        password = self.ui.input_pas.text().strip()
        check, id = login_system(username, password)
        if not username or not password:
            return False, "Заполните все поля"
        elif not check:
            return False, "Неверный логин или пароль"
        USER_ID = id
        return True, ""

    def process_login(self):  # Обрабатывает нажатие кнопки входа
        is_valid, message = self.validate_login_data()
        if is_valid:
            self.gotoScreen_Main()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Ошибка регистрации")
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStyleSheet("""
                            QMessageBox {
                                background-color: #121212;
                            }
                            QLabel {
                                color: white;
                                font-size: 14px;
                            }
                            QPushButton {
                                background-color: #333;
                                color: white;
                                border-radius: 6px;
                                padding: 6px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
            msg.exec()

    def gotoScreen_log(self):  # переход на окно регистрации
        self.hide()
        self.screen_log = Log_Window()
        self.screen_log.show()

    def gotoScreen_Main(self):  # переход на основное окно с конспектами
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()

    def toggle_password_visibility(self):
        if self.ui.toggle_button.isChecked():
            self.ui.input_pas.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.input_pas.setEchoMode(QLineEdit.EchoMode.Password)


def run():
    app = QApplication(sys.argv)
    window = First_Window()
    sys.exit(app.exec())  # открытие приложения


run()
