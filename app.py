import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QBoxLayout, QTabWidget, QListWidget, QFileDialog, QTextEdit, QMessageBox
from PyQt6.QtGui import QPixmap #для картинок
from PyQt6.QtCore import Qt, QFile, QIODevice, QTextStream

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
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"#путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по дискре")
        self.setUpDiscra_Window()
        self.show()

    def setUpDiscra_Window(self):
        con_box = QVBoxLayout()
        con1 = QLabel("первый конспект", self)#создание текста и кнопки для первого конспекта #вместо "первый конспект" можно название темы написать
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

        self.text_area = QTextEdit()#пустое поле, в котором потом показывается содержимое файла
        con_box.addWidget(self.text_area)

        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)
        con_box.addWidget(self.exit_button)

        self.setLayout(con_box)

    def open_con1(self):#функция открытия файла
        с1 = QFile(self.con1)
        if с1.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с1)
            content = stream.readAll()
            self.text_area.setText(content)
            с1.close()

    def open_con2(self):#функция открытия файла
        с2 = QFile(self.con2)
        if с2.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с2)
            content = stream.readAll()
            self.text_area.setText(content)
            с2.close()

    def goto_MainWindow(self):#функция перехода на главное окно
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()

class Linal_Window(QWidget):#окно с конспектами по линалу
    def  __init__(self):
        super().__init__()
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"#путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по линалу")
        self.setUpLinal_Window()
        self.show()

    def setUpLinal_Window(self):
        con_box = QVBoxLayout()
        con1 = QLabel("первый конспект", self)#создание текста и кнопки для первого конспекта #вместо "первый конспект" можно название темы написать
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

        self.text_area = QTextEdit()#пустое поле, в котором потом показывается содержимое файла
        con_box.addWidget(self.text_area)

        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)
        con_box.addWidget(self.exit_button)

        self.setLayout(con_box)

    def open_con1(self):#функция открытия файла
        с1 = QFile(self.con1)
        if с1.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с1)
            content = stream.readAll()
            self.text_area.setText(content)
            с1.close()

    def open_con2(self):#функция открытия файла
        с2 = QFile(self.con2)
        if с2.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с2)
            content = stream.readAll()
            self.text_area.setText(content)
            с2.close()

    def goto_MainWindow(self):#функция перехода на главное окно
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()

class Matan_Window(QWidget):#окно с конспектами по матану
    def  __init__(self):
        super().__init__()
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"#путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по матану")
        self.setUpMatan_Window()
        self.show()

    def setUpMatan_Window(self):
        con_box = QVBoxLayout()
        con1 = QLabel("первый конспект", self)#создание текста и кнопки для первого конспекта #вместо "первый конспект" можно название темы написать
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

        self.text_area = QTextEdit()#пустое поле, в котором потом показывается содержимое файла
        con_box.addWidget(self.text_area)

        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)
        con_box.addWidget(self.exit_button)

        self.setLayout(con_box)

    def open_con1(self):#функция открытия файла
        с1 = QFile(self.con1)
        if с1.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с1)
            content = stream.readAll()
            self.text_area.setText(content)
            с1.close()

    def open_con2(self):#функция открытия файла
        с2 = QFile(self.con2)
        if с2.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
            stream = QTextStream(с2)
            content = stream.readAll()
            self.text_area.setText(content)
            с2.close()

    def goto_MainWindow(self):#функция перехода на главное окно
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()

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
        sub_name = QLabel("предмет:", self)

        self.vari = QComboBox(self)
        self.vari.addItems([" ", "матан", "линал", "дискра", "прога", "тп", "цг"])
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
        #self.selection_label.setText(f"Selected: {current_text} (Index: {current_index})")
        if current_text == "матан":
            self.ac_button.clicked.connect(self.goto_ScreenMatan)
        elif current_text == "линал":
            self.ac_button.clicked.connect(self.goto_ScreenLinal)
        elif current_text == "дискра":
            self.ac_button.clicked.connect(self.goto_ScreenDiscra)
        elif current_text == "прога":
            self.ac_button.clicked.connect(self.goto_ScreenProga)
        elif current_text == "тп":
            self.ac_button.clicked.connect(self.goto_ScreenTp)
        else:
            self.ac_button.clicked.connect(self.goto_ScreenGram)
    
    def goto_ScreenMatan(self):
        self.hide()
        self.screen_matan = Matan_Window()
        self.screen_matan.show()

    def goto_ScreenLinal(self):
        self.hide()
        self.screen_linal = Linal_Window()
        self.screen_linal.show()
    
    def goto_ScreenDiscra(self):
        self.hide()
        self.screen_discra = Discra_Window()
        self.screen_discra.show()
    
    def goto_ScreenProga(self):
        self.hide()
        self.screen_proga = Proga_Window()
        self.screen_proga.show()
    
    def goto_ScreenTp(self):
        self.hide()
        self.screen_tp = Tp_Window()
        self.screen_tp.show()
    
    def goto_ScreenGram(self):
        self.hide()
        self.screen_gram = Gram_Window()
        self.screen_gram.show()

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
        self.hide()
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
        self.hide()
        self.screen_log = Log_Window()
        self.screen_log.show()
    def gotoScreen_Main(self):#переход на основное окно с конспектами
        self.hide()
        self.screen_main = Main_Window()
        self.screen_main.show()

app = QApplication(sys.argv)
window = First_Window()
sys.exit(app.exec()) #открытие приложения