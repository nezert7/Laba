import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, \
    QBoxLayout, QTabWidget, QListWidget, QFileDialog, QTextEdit, QMessageBox, QToolButton
from PyQt6.QtGui import QPixmap, QIcon  # для картинок
from PyQt6.QtCore import Qt, QFile, QIODevice, QTextStream, QSize
from main import create_account, login_system, all_name_subject


class Matan_Window(QWidget):  # окно с конспектами по матану
    def __init__(self):
        super().__init__()
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"  # путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):  # задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600)  # 600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по матану")
        self.setUpMatan_Window()
        self.show()

    def setUpMatan_Window(self):
        con_box = QVBoxLayout()
        con1 = QLabel("первый конспект",
                      self)  # создание текста и кнопки для первого конспекта #вместо "первый конспект" можно название темы написать
        con1_button = QPushButton("показать")
        con1_button.clicked.connect(self.open_con1)

        con1_h_box = QHBoxLayout()
        con1_h_box.addWidget(con1)
        con1_h_box.addWidget(con1_button)
        con_box.addLayout(con1_h_box)

        con2 = QLabel("второй конспект", self)
        con2_button = QPushButton("показать")
        con2_button.clicked.connect(self.open_con2)

        con2_h_box = QHBoxLayout()
        con2_h_box.addWidget(con2)
        con2_h_box.addWidget(con2_button)
        con_box.addLayout(con2_h_box)

        self.text_area = QTextEdit()  # пустое поле, в котором потом показывается содержимое файла
        con_box.addWidget(self.text_area)

        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)
        con_box.addWidget(self.exit_button)

        self.setLayout(con_box)

    def open_con1(self):  # функция открытия файла
        с1 = QFile(self.con1)
        if с1.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с1)
            content = stream.readAll()
            self.text_area.setText(content)
            с1.close()

    def open_con2(self):  # функция открытия файла
        с2 = QFile(self.con2)
        if с2.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с2)
            content = stream.readAll()
            self.text_area.setText(content)
            с2.close()

    def goto_MainWindow(self):  # функция перехода на главное окно
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()


class Main_Window(QWidget):  # окно с выбором предмета, основное окно приложения
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):  # задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600)  # 600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("главное окно")
        self.setUpMain_Window()
        self.show()

    def setUpMain_Window(self):
        main_v_box = QVBoxLayout()
        sub_name = QLabel("предмет:", self)

        self.vari = QComboBox(self)
        list_subject = [""] + all_name_subject()
        self.vari.addItems(list_subject)
        self.ac_button = QPushButton("подтвердить", self)
        self.ac_button.clicked.connect(self.show_current_selection)

        sub_h_box = QHBoxLayout()
        sub_h_box.addWidget(sub_name)
        sub_h_box.addWidget(self.vari)
        sub_h_box.addWidget(self.vari)
        sub_h_box.setAlignment(self.vari, Qt.AlignmentFlag.AlignTop)
        sub_h_box.addWidget(self.ac_button)
        main_v_box.addLayout(sub_h_box)

        main_v_box.setAlignment(sub_h_box, Qt.AlignmentFlag.AlignTop)

        self.setLayout(main_v_box)

    def show_current_selection(self):
        current_text = self.vari.currentText()
        current_index = self.vari.currentIndex()
        # self.selection_label.setText(f"Selected: {current_text} (Index: {current_index})")
        self.ac_button.clicked.connect(self.goto_ScreenMatan)

    def goto_ScreenMatan(self):
        self.hide()
        self.screen_matan = Matan_Window()
        self.screen_matan.show()


class Log_Window(QWidget):  # окно регистрации
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):  # задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600)  # 600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("регистрация")
        self.setUpLog_Window()
        self.show()

    def setUpLog_Window(self):
        main_v_box = QVBoxLayout()
        self.input_logr = QLineEdit(self)
        self.input_logr.setPlaceholderText("Придумайте логин")

        self.input_pasr = QLineEdit(self)
        self.input_pasr.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_pasr.setPlaceholderText("Придумайте пароль")

        self.input_pasr2 = QLineEdit(self)
        self.input_pasr2.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_pasr2.setPlaceholderText("Повторите пароль")

        self.toggle_button = QPushButton("👁️")
        self.toggle_button.setCheckable(True)
        self.toggle_button.setFixedSize(QSize(24, 24))
        self.toggle_button.clicked.connect(self.toggle_password_visibility)

        self.log_button = QPushButton("зарегистрироваться", self)
        self.log_button.clicked.connect(self.process_registration)

        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)

        logr_h_box = QHBoxLayout()
        pasr_h_box = QHBoxLayout()
        pasr2_h_box = QHBoxLayout()
        logr_h_box.addWidget(self.input_logr)
        pasr_h_box.addWidget(self.input_pasr)
        pasr2_h_box.addWidget(self.input_pasr2)
        main_v_box.addLayout(logr_h_box)
        main_v_box.addLayout(pasr_h_box)
        main_v_box.addLayout(pasr2_h_box)
        main_v_box.addWidget(self.toggle_button)
        main_v_box.addWidget(self.log_button)
        main_v_box.addWidget(self.exit_button)

        self.setLayout(main_v_box)

    def validate_registration_data(self):  # Проверяет валидность данных для регистрации
        username = self.input_logr.text().strip()
        password = self.input_pasr.text().strip()
        password_confirm = self.input_pasr2.text().strip()

        if not username or not password or not password_confirm:
            return False, "Все поля должны быть заполнены"
        elif password != password_confirm:
            return False, "Пароли не совпадают"
        elif not create_account(username, password):
            return False, "Такой пользователь уже существует"
        return True, ""

    def process_registration(self):  # Обрабатывает нажатие кнопки регистрации
        is_valid, message = self.validate_registration_data()
        if is_valid:
            self.close()
            self.goto_MainWindow()
        else:
            QMessageBox.warning(self, "Ошибка регистрации", message)

    def goto_ScreenFirst(self):  # переход на окно входа
        self.hide()
        self.screen_log = First_Window()
        self.screen_log.show()

    def goto_MainWindow(self):  # функция перехода на главное окно
        self.hide()
        self.screen_first = First_Window()
        self.screen_first.show()

    def toggle_password_visibility(self):
        if self.toggle_button.isChecked():
            self.input_pasr.setEchoMode(QLineEdit.EchoMode.Normal)
            self.input_pasr2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_pasr.setEchoMode(QLineEdit.EchoMode.Password)
            self.input_pasr2.setEchoMode(QLineEdit.EchoMode.Password)



class First_Window(QWidget):  # окно открытия приложения, вход
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):  # задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600)  # 600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("заголовок окна")
        self.setUpFirst_Window()
        self.show()

    def setUpFirst_Window(self):  # расположение элементов на окне
        main_v_box = QVBoxLayout()
        head_text = QLabel("авторизация", self)
        head_text.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_log = QLineEdit(self)
        self.input_log.setPlaceholderText("Введите логин")

        self.input_pas = QLineEdit(self)
        self.input_pas.setPlaceholderText("Введите пароль")
        self.input_pas.setEchoMode(QLineEdit.EchoMode.Password)

        self.ot_button = QPushButton("войти", self)
        self.ot_button.clicked.connect(self.process_login)
        # self.ot_button.QShortcut(QKeySequence('Ctrl+O'), self)
        self.log_button = QPushButton("зарегистрироваться", self)
        self.log_button.clicked.connect(self.gotoScreen_log)

        self.toggle_button = QPushButton("👁️")
        self.toggle_button.setCheckable(True)
        self.toggle_button.setFixedSize(QSize(24, 24))
        self.toggle_button.clicked.connect(self.toggle_password_visibility)

        log_h_box = QHBoxLayout()
        pas_h_box = QHBoxLayout()
        log_h_box.addWidget(self.input_log)
        pas_h_box.addWidget(self.input_pas)
        main_v_box.addLayout(log_h_box)
        main_v_box.addLayout(pas_h_box)
        main_v_box.addWidget(self.toggle_button)
        main_v_box.addWidget(self.ot_button)
        main_v_box.addWidget(self.log_button)

        self.setLayout(main_v_box)

    def validate_login_data(self):  # Проверяет валидность данных для авторизации
        username = self.input_log.text().strip()
        password = self.input_pas.text().strip()
        check, id = login_system(username, password)
        if not username or not password:
            return False, "Заполните все поля"
        elif not check:
            return False, "Неверный логин или пароль"
        return True, ""

    def process_login(self):  # Обрабатывает нажатие кнопки входа
        is_valid, message = self.validate_login_data()
        if is_valid:
            self.gotoScreen_Main()
        else:
            QMessageBox.warning(self, "Ошибка авторизации", message)

    def gotoScreen_log(self):  # переход на окно регистрации
        self.hide()
        self.screen_log = Log_Window()
        self.screen_log.show()

    def gotoScreen_Main(self):  # переход на основное окно с конспектами
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()

    def toggle_password_visibility(self):
        if self.toggle_button.isChecked():
            self.input_pas.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_pas.setEchoMode(QLineEdit.EchoMode.Password)


def run():
    app = QApplication(sys.argv)
    window = First_Window()
    sys.exit(app.exec())  # открытие приложения


run()
