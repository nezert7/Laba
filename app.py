import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QBoxLayout, QTabWidget
from PyQt6.QtGui import QPixmap #для картинок
from PyQt6.QtCore import Qt

class Gram_Window(QWidget):#окно с конспектами по цг
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по цг")
        self.setUpGram_Window()
        self.show()

    def setUpGram_Window(self):
        pass

class Tp_Window(QWidget):#окно с конспектами по тп
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по тп")
        self.setUpTp_Window()
        self.show()

    def setUpTp_Window(self):
        pass

class Proga_Window(QWidget):#окно с конспектами по проге
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по проге")
        self.setUpProga_Window()
        self.show()

    def setUpProga_Window(self):
        pass

class Discra_Window(QWidget):#окно с конспектами по дискре
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по дискре")
        self.setUpDiscra_Window()
        self.show()

    def setUpDiscra_Window(self):
        pass

class Linal_Window(QWidget):#окно с конспектами по линалу
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по линалу")
        self.setUpLinal_Window()
        self.show()

    def setUpLinal_Window(self):
        pass

class Matan_Window(QWidget):#окно с конспектами по матану
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по матану")
        self.setUpMatan_Window()
        self.show()

    def setUpMatan_Window(self):
        #fil = QFileDialog(self)#открывает проводник
        #fil.exec()
        pass

class Main_Window(QWidget):#окно с выбором предмета, основное окно приложения
    def  __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("главное окно")
        self.setUpMain_Window()
        self.show()

    def setUpMain_Window(self):
        main_v_box = QVBoxLayout()
        self.vari = QTabWidget(self)#создание меню с предметами
        mat = QLabel("матан", self)
        self.vari.addTab(mat, "матан")
        linal = QLabel("линал", self)
        self.vari.addTab(linal, "линал")
        discra = QLabel("дискра", self)
        self.vari.addTab(discra, "дискра")
        proga = QLabel("прога", self)
        self.vari.addTab(proga, "прога")
        tp = QLabel("тп", self)
        self.vari.addTab(tp, "тп")
        gram = QLabel("цг", self)
        self.vari.addTab(gram, "цг")
        
        sub_h_box = QHBoxLayout()
        sub_h_box.addWidget(self.vari)
        sub_h_box.setAlignment(self.vari, Qt.AlignmentFlag.AlignTop)
        main_v_box.addLayout(sub_h_box)

        main_v_box.setAlignment(sub_h_box, Qt.AlignmentFlag.AlignTop)

        self.setLayout(main_v_box)
    def show_current_selection(self):#работа кнопки "подтвердить"
        current_text = self.vari.currentText()
        current_index = self.vari.currentIndex()
        if current_text == "матан":
            self.ac_button.clicked.connect(self.goto_ScreenMatan)#работа кнопки "подтвердить" на переход на окно с конспектами по матану
        if current_text == "линал":
            self.ac_button.clicked.connect(self.goto_ScreenLinal)#работа кнопки "подтвердить" на переход на окно с конспектами по линалу
        if current_text == "дискра":
            self.ac_button.clicked.connect(self.goto_ScreenDiscra)#работа кнопки "подтвердить" на переход на окно с конспектами по дискре
        if current_text == "прога":
            self.ac_button.clicked.connect(self.goto_ScreenProga)#работа кнопки "подтвердить" на переход на окно с конспектами по проге
        if current_text == "тп":
            self.ac_button.clicked.connect(self.goto_ScreenTp)#работа кнопки "подтвердить" на переход на окно с конспектами по тп
        if current_text == "цг":
            self.ac_button.clicked.connect(self.goto_ScreenGram)#работа кнопки "подтвердить" на переход на окно с конспектами по цг
    
    def goto_ScreenMatan(self):#переход на окно с конспектами по матану
        self.screen_main = Matan_Window()
        self.screen_main.show()

    def goto_ScreenLinal(self):#переход на окно с конспектами по линалу
        self.screen_main = Linal_Window()
        self.screen_main.show()
    
    def goto_ScreenDiscra(self):#переход на окно с конспектами по дискре
        self.screen_main = Discra_Window()
        self.screen_main.show()
    
    def goto_ScreenProga(self):#ереход на окно с конспектами по проге
        self.screen_main = Proga_Window()
        self.screen_main.show()
    
    def goto_ScreenTp(self):#переход на окно с конспектами по тп
        self.screen_main = Tp_Window()
        self.screen_main.show()
    
    def goto_ScreenGram(self):#переход на окно с конспектами по цг
        self.screen_main = Gram_Window()
        self.screen_main.show()

class Log_Window(QWidget):#окно регистрации
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
    def addBD_goMain(self):#сохранение введеного логина и пароля
        if len(self.input_logr.text()) > 0 and len(self.input_pasr.text()) > 0 and (self.input_pasr.text() == self.input_pasr2.text()):
            self.log_button.setEnabled(True)
            #придумать как добавить введенные данные в бд
            self.log_button.clicked.connect(self.goto_ScreenFirst)
        else:
            self.log_button.setEnabled(False)

    def goto_ScreenFirst(self):#переход на окно входа
        self.screen_log = First_Window()
        self.screen_log.show()


class First_Window(QWidget):#окно открытия приложения, вход 
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
        #self.ot_button.QShortcut(QKeySequence('Ctrl+O'), self)
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

    def gotoScreen_log(self):#переход на окно регистрации
        self.screen_log = Log_Window()
        self.screen_log.show()
    def gotoScreen_Main(self):#переход на основное окно с конспектами
        self.screen_main = Main_Window()
        self.screen_main.show()

app = QApplication(sys.argv)
window = First_Window()
sys.exit(app.exec()) #открытие приложения