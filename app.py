import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStackedLayout
from PyQt6.QtGui import QPixmap #для картинок
from PyQt6.QtCore import Qt

class Main_Window(QWidget):
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("главное окно")
        self.setUpMain_Window()
        self.show()

    def setUpMain_Window(self):
        pass

class Log_Window(QWidget):
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("регистрация")
        self.setUpLog_Window()
        self.show()

    def setUpLog_Window(self):
        main_v_box = QVBoxLayout()
        logr = QLabel("придумайте логин", self)
        self.input_logr = QLineEdit(self)
        self.input_logr.textEdited.connect(self.addBD_goMain)
        pasr = QLabel("придумайте пароль", self)
        self.input_pasr = QLineEdit(self)
        self.input_pasr.textEdited.connect(self.addBD_goMain)
        pasr2 = QLabel("повторите пароль")
        self.input_pasr2 = QLineEdit(self)
        self.input_pasr2.textEdited.connect(self.addBD_goMain)
        self.log_button = QPushButton("зарегистрироваться", self)
        self.log_button.clicked.connect(self.addBD_goMain)
        self.log_button.setEnabled(False)

        logr_h_box = QHBoxLayout()
        pasr_h_box = QHBoxLayout()
        pasr2_h_box = QHBoxLayout()
        logr_h_box.addWidget(logr)
        logr_h_box.addWidget(self.input_logr)
        pasr_h_box.addWidget(pasr)
        pasr_h_box.addWidget(self.input_pasr)
        pasr2_h_box.addWidget(pasr2)
        pasr2_h_box.addWidget(self.input_pasr2)
        main_v_box.addLayout(logr_h_box)
        main_v_box.addLayout(pasr_h_box)
        main_v_box.addLayout(pasr2_h_box)
        main_v_box.addWidget(self.log_button)

        self.setLayout(main_v_box)
    def addBD_goMain(self):
        if len(self.input_logr.text()) > 0 and len(self.input_pasr.text()) > 0 and (self.input_pasr.text() == self.input_pasr2.text()):
            self.log_button.setEnabled(True)
            #придумать как добавить введенные данные в бд
            self.log_button.clicked.connect(self.goto_ScreenFirst)
        else:
            self.log_button.setEnabled(False)

    def goto_ScreenFirst(self):
        self.screen_log = First_Window()
        self.screen_log.show()


class First_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("заголовок окна")
        self.setUpFirst_Window()
        self.show()

    def setUpFirst_Window(self):#расположение элементов на окне
        main_v_box = QVBoxLayout()
        head_text = QLabel("авторизация", self)
        head_text.setAlignment(Qt.AlignmentFlag.AlignRight)
        log = QLabel("введите логин", self)
        self.input_log = QLineEdit(self)
        self.input_log.textEdited.connect(self.checkCode)
        pas = QLabel("введите пароль", self)
        self.input_pas = QLineEdit(self)
        self.input_pas.textEdited.connect(self.checkCode)
        self.ot_button = QPushButton("войти", self)
        self.ot_button.setEnabled(False)
        self.log_button = QPushButton("зарегистрироваться", self)
        self.log_button.clicked.connect(self.gotoScreen_log)

        log_h_box = QHBoxLayout()
        pas_h_box = QHBoxLayout()
        log_h_box.addWidget(log)
        log_h_box.addWidget(self.input_log)
        pas_h_box.addWidget(pas)
        pas_h_box.addWidget(self.input_pas)
        main_v_box.addLayout(log_h_box)
        main_v_box.addLayout(pas_h_box)
        main_v_box.addWidget(self.ot_button)
        main_v_box.addWidget(self.log_button)

        self.setLayout(main_v_box)

    def checkCode(self):#работа кнопки вход
        if len(self.input_log.text()) > 0 and len(self.input_pas.text()) > 0:#надо сравнить с данными из бд
            self.ot_button.setEnabled(True)
            self.ot_button.clicked.connect(self.gotoScreen_Main)
        else:
            self.ot_button.setEnabled(False)

    def gotoScreen_log(self):
        self.screen_log = Log_Window()
        self.screen_log.show()
    def gotoScreen_Main(self):
        self.screen_main = Main_Window()
        self.screen_main.show()

app = QApplication(sys.argv)
window = First_Window()
sys.exit(app.exec()) #открытие приложения