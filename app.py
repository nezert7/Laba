import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStackedLayout
from PyQt6.QtGui import QPixmap #для картинок
from PyQt6.QtCore import Qt

class First_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_vhod = QWidget()
        self.screen_kon = QWidget()
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

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.screen_vhod)
        self.stacked_layout.addWidget(self.screen_kon)

        self.setLayout(main_v_box)

    def checkCode(self):#работа кнопки вход
        if len(self.input_log.text()) > 0 and len(self.input_pas.text()) > 0:#надо сравнить с данными из бд
            self.ot_button.setEnabled(True)
            self.ot_button.clicked.connect(self.gotoScreen_kon)
        else:
            self.ot_button.setEnabled(False)
    
    def gotoScreen_kon(self):#переход на новую страницу
        self.stacked_layout.setCurrentWidget(self.screen_kon)

app = QApplication(sys.argv)
window = First_Window()
sys.exit(app.exec()) #открытие приложения