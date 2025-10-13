import sys
import webbrowser #чтоб ссылки открывались
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QBoxLayout, QTabWidget, QListWidget, QFileDialog, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, QSpinBox, QToolBar, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import Qt, QFile, QIODevice, QTextStream, QSize

class Gram_Window(QWidget):#окно с конспектами по цг
    def  __init__(self):
        super().__init__()
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"#путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по цг")
        self.setUpGram_Window()
        self.show()

    def setUpGram_Window(self):
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

class Tp_Window(QWidget):#окно с конспектами по тп
    def  __init__(self):
        super().__init__()
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"#путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по тп")
        self.setUpTp_Window()
        self.show()

    def setUpTp_Window(self):
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

class Proga_Window(QWidget):#окно с конспектами по проге
    def  __init__(self):
        super().__init__()
        self.con1 = "C:/Users/l.sakharnova/Desktop/code/команды для лабы 1.txt"#путь к файлу #обязательно именно такая / палка
        self.con2 = "C:/Users/l.sakharnova/Desktop/code/PyQt6.txt"
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("лекции по проге")
        self.setUpProga_Window()
        self.show()

    def setUpProga_Window(self):
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

class Main_Window(QMainWindow):#окно с выбором предмета, основное окно приложения
    def  __init__(self):
        super().__init__()
        self.conspect = []
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("главное окно")
        self.setUpMain_Window()
        self.show()

    def setUpMain_Window(self):
        self.conspect = [
            {'предмет': 'матан', 'название конспекта': '1', 'ссылка': "https://www.pythontutorial.net/pyqt/pyqt-qtablewidget/", 'дата': 25},
            {'предмет': 'матан', 'название конспекта': '1', 'ссылка': "https://www.pythontutorial.net/pyqt/pyqt-qtablewidget/", 'дата': 22},
            {'предмет': 'матан', 'название конспекта': '1', 'ссылка': "https://www.pythontutorial.net/pyqt/pyqt-qtablewidget/", 'дата': 22},
        ]#список изначальных конспектов

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        filter_layout = QHBoxLayout()
        
        filter_label = QLabel("Фильтр по предмету:")
        self.filter_combo = QComboBox()
        self.filter_combo.addItem("все предметы")
        self.filter_combo.currentTextChanged.connect(self.apply_filter)
        
        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(self.filter_combo)
        filter_layout.addStretch()
        
        main_layout.addLayout(filter_layout)

        self.table = QTableWidget()
        main_layout.addWidget(self.table)

        self.table.setColumnCount(4)#кол-во столбцов
        self.table.setColumnWidth(0, 150)#настройка ширины столбцов
        self.table.setColumnWidth(1, 150)#настройка ширины столбцов
        self.table.setColumnWidth(2, 300)#настройка ширины столбцов
        self.table.setColumnWidth(3, 50)#настройка ширины столбцов

        self.table.setHorizontalHeaderLabels(['предмет', 'название конспекта', 'ссылка', 'дата'])#горизонтальные заголовки таблицы
        
        self.populate_table()#заполняем таблицу данными
        
        self.update_filter_combo()#обновляем комбобокс фильтра

        self.table.cellClicked.connect(self.on_cell_clicked)#подключаем обработчик кликов по ячейкам

        dock = QDockWidget('добавить конспект')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.subject_name = QLineEdit(form)
        self.conspect_name = QLineEdit(form)
        self.link = QLineEdit(form)
        self.age = QSpinBox(form, minimum=1, maximum=31)
        self.age.clear()

        layout.addRow('предмет:', self.subject_name)
        layout.addRow('название конспекта:', self.conspect_name)
        layout.addRow('ссылка:', self.link)
        layout.addRow('дата (день):', self.age)

        btn_add = QPushButton('добавить')
        btn_add.clicked.connect(self.add_employee)
        layout.addRow(btn_add)

        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        delete_action = QAction('&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)
        dock.setWidget(form)

    def populate_table(self, filter_subject=None):#заполняет таблицу данными с учетом фильтра
        self.table.setRowCount(0)#очищаем таблицу
        
        row = 0
        for e in self.conspect:#применяем фильтр, если он задан
            if filter_subject and filter_subject != "все предметы" and e['предмет'] != filter_subject:
                continue
                
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(e['предмет']))
            self.table.setItem(row, 1, QTableWidgetItem(e['название конспекта']))
            
            link_item = QTableWidgetItem(e['ссылка'])#создаем ячейку для ссылки с особым оформлением
            link_item.setForeground(Qt.GlobalColor.blue)#синий цвет для ссылки
            link_item.setToolTip(f"Нажмите чтобы открыть: {e['ссылка']}")#подсказка
            self.table.setItem(row, 2, link_item)
            
            self.table.setItem(row, 3, QTableWidgetItem(str(e['дата'])))
            row += 1

    def update_filter_combo(self):#обновляет список предметов в комбобоксе фильтра
        current_filter = self.filter_combo.currentText()
        self.filter_combo.clear()
        self.filter_combo.addItem("все предметы")
        
        subjects = set()#собираем уникальные предметы
        for item in self.conspect:
            subjects.add(item['предмет'])
        
        for subject in sorted(subjects):#добавляем предметы в комбобокс
            self.filter_combo.addItem(subject)
        
        if current_filter in [self.filter_combo.itemText(i) for i in range(self.filter_combo.count())]:#восстанавливаем предыдущий фильтр, если он еще существует
            self.filter_combo.setCurrentText(current_filter)
        else:
            self.filter_combo.setCurrentText("все предметы")

    def apply_filter(self, subject):#применяет фильтр по выбранному предмету
        if subject == "все предметы":
            self.populate_table() #показываем все записи
        else:
            self.populate_table(subject)#показываем только выбранный предмет
    
    def on_cell_clicked(self, row, column):#обработчик клика по ячейке таблицы
        if column == 2:#только для столбца с ссылками
            item = self.table.item(row, column)
            if item and item.text().startswith(('http://', 'https://')):
                reply = QMessageBox.question(self, 'открыть ссылку', f'вы хотите открыть ссылку:\n{item.text()}', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)# Спрашиваем подтверждение перед открытием
                if reply == QMessageBox.StandardButton.Yes:
                    try:
                        webbrowser.open(item.text())
                        QMessageBox.information(self, 'успешно', 'ссылка открывается в браузере')
                    except Exception as e:
                        QMessageBox.critical(self, 'Error', f'не удалось открыть ссылку: {str(e)}')
    
    def add_employee(self):#добавление нового конспекта
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.subject_name.text().strip()))
        self.table.setItem(row, 1, QTableWidgetItem(self.conspect_name.text()))
        
        link_item = QTableWidgetItem(self.link.text())#добавление ссылку с оформлением
        link_item.setForeground(Qt.GlobalColor.blue)
        link_item.setToolTip(f"нажмите чтобы открыть: {self.link.text()}")
        self.table.setItem(row, 2, link_item)
        
        self.table.setItem(row, 3, QTableWidgetItem(self.age.text()))

        new_conspect = {'предмет': self.subject_name.text().strip(), 'название конспекта': self.conspect_name.text(), 'ссылка': self.link.text(), 'дата': self.age.text()}
        self.conspect.append(new_conspect)
    
        self.update_filter_combo()#обновляем фильтр и применяем текущий
        current_filter = self.filter_combo.currentText()
        if current_filter == "все предметы" or current_filter == self.new_conspect['предмет']:
            self.apply_filter(current_filter)

        self.reset()

    def delete(self):#кнопка удаление конспекта
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Error','выберите строку, чтоб удалить')

        button = QMessageBox.question(self, 'Error', 'вы уверены, что хотите удалить выбранную строку?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button == QMessageBox.StandardButton.Yes:#получаем предмет удаляемой строки для обновления фильтра
            deleted_subject = self.table.item(current_row, 0).text()
            
            self.table.removeRow(current_row)
            if current_row < len(self.conspect):#удаляем из списка conspect
                self.conspect.pop(current_row)
            
            self.update_filter_combo()#обновляем фильтр
            current_filter = self.filter_combo.currentText()
            self.apply_filter(current_filter)

    def valid(self):
        subject_name = self.subject_name.text().strip()
        conspect_name = self.conspect_name.text().strip()
        link = self.link.text().strip()
        
        if not subject_name:
            QMessageBox.critical(self, 'Error', 'пожалуйста добавьте название предмета')
            self.subject_name.setFocus()
            return False

        if not conspect_name:
            QMessageBox.critical(self, 'Error', 'пожалуйста добавьте тему конспекта')
            self.conspect_name.setFocus()
            return False
        
        if not link:
            QMessageBox.critical(self, 'Error', 'пожалуйста добавьте ссылку на конспект')
            self.link.setFocus()
            return False
        
        if not link.startswith(('http://', 'https://')):# Проверяем, что ссылка начинается с http:// или https://
            QMessageBox.warning(self, 'Error', 'ссылка должна начинаться с http:// или https://\nДобавляю https:// автоматически')
            self.link.setText('https://' + link)
            return self.valid()  # Повторная проверка

        try:
            age = int(self.age.text().strip())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'пожалуйста добавьте дату создания конспекта')
            self.age.setFocus()
            return False

        if age <= 0 or age > 31:
            QMessageBox.critical(self, 'Error', 'дата должна быть числом от 1 до 31')
            self.age.setFocus()
            return False

        return True

    def reset(self):
        self.subject_name.clear()
        self.conspect_name.clear()
        self.link.clear()
        self.age.clear()


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
        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)

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
        main_v_box.addWidget(self.exit_button)

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
    
    def goto_MainWindow(self):#функция перехода на главное окно
        self.hide()
        self.screen_first = First_Window()
        self.screen_first.show()


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