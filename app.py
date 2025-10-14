import sys
import webbrowser  # чтоб ссылки открывались
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, \
    QBoxLayout, QTabWidget, QListWidget, QFileDialog, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem, \
    QDockWidget, QFormLayout, QSpinBox, QToolBar, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, \
    QDockWidget, QFormLayout, QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon, QAction
from PyQt6.QtCore import Qt, QFile, QIODevice, QTextStream, QSize
from main import create_account, login_system, all_name_subject, all_info_files_user, download_inf_file_in_db

USER_ID = 0


class Main_Window(QMainWindow):  # окно с выбором предмета, основное окно приложения
    def __init__(self):
        super().__init__()
        self.conspect = []
        self.firs_window = First_Window
        self.initializeUI()

    def initializeUI(self):  # задача базовых настроек приложения
        self.setGeometry(600, 200, 900, 600)  # 600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("главное окно")
        self.setUpMain_Window()
        self.show()

    def setUpMain_Window(self):  # список изначальных конспектов
        sp = all_info_files_user(USER_ID)
        for x in sp:
            self.conspect.append({'предмет': x[0], 'название конспекта': x[1],
                                  'ссылка': x[2], 'дата': x[3]})

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

        self.table.setColumnCount(4)  # кол-во столбцов
        self.table.setColumnWidth(0, 150)  # настройка ширины столбцов
        self.table.setColumnWidth(1, 150)  # настройка ширины столбцов
        self.table.setColumnWidth(2, 300)  # настройка ширины столбцов
        self.table.setColumnWidth(3, 50)  # настройка ширины столбцов

        self.table.setHorizontalHeaderLabels(
            ['предмет', 'название конспекта', 'ссылка', 'дата'])  # горизонтальные заголовки таблицы

        self.populate_table()  # заполняем таблицу данными

        self.update_filter_combo()  # обновляем комбобокс фильтра

        self.table.cellClicked.connect(self.on_cell_clicked)  # подключаем обработчик кликов по ячейкам

        dock = QDockWidget('добавить конспект')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.subject_name = QLineEdit(form)
        self.age = QSpinBox(form, minimum=1, maximum=31)
        self.age.clear()

        layout.addRow('предмет:', self.subject_name)
        layout.addRow('дата (день):', self.age)

        btn_add = QPushButton('добавить')
        btn_add.clicked.connect(self.add_employee)
        layout.addRow(btn_add)

        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        delete_action = QAction('&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)
        dock.setWidget(form)

    def populate_table(self, filter_subject=None):  # заполняет таблицу данными с учетом фильтра
        self.table.setRowCount(0)  # очищаем таблицу

        row = 0
        for e in self.conspect:  # применяем фильтр, если он задан
            if filter_subject and filter_subject != "все предметы" and e['предмет'] != filter_subject:
                continue

            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(e['предмет']))
            self.table.setItem(row, 1, QTableWidgetItem(e['название конспекта']))

            link_item = QTableWidgetItem(e['ссылка'])  # создаем ячейку для ссылки с особым оформлением
            link_item.setForeground(Qt.GlobalColor.blue)  # синий цвет для ссылки
            link_item.setToolTip(f"Нажмите чтобы открыть: {e['ссылка']}")  # подсказка
            self.table.setItem(row, 2, link_item)

            self.table.setItem(row, 3, QTableWidgetItem(str(e['дата'])))
            row += 1

    def update_filter_combo(self):  # обновляет список предметов в комбобоксе фильтра
        current_filter = self.filter_combo.currentText()
        self.filter_combo.clear()
        self.filter_combo.addItem("все предметы")

        sp_subject = all_name_subject()
        subjects = set()  # собираем уникальные предметы
        for item in sp_subject:
            subjects.add(item)

        for subject in sorted(subjects):  # добавляем предметы в комбобокс
            self.filter_combo.addItem(subject)

        if current_filter in [self.filter_combo.itemText(i) for i in
                              range(
                                  self.filter_combo.count())]:  # восстанавливаем предыдущий фильтр, если он еще существует
            self.filter_combo.setCurrentText(current_filter)
        else:
            self.filter_combo.setCurrentText("все предметы")

    def apply_filter(self, subject):  # применяет фильтр по выбранному предмету
        if subject == "все предметы":
            self.populate_table()  # показываем все записи
        else:
            self.populate_table(subject)  # показываем только выбранный предмет

    def on_cell_clicked(self, row, column):  # обработчик клика по ячейке таблицы
        if column == 2:  # только для столбца со ссылками
            item = self.table.item(row, column)
            if item and item.text().startswith(('http://', 'https://')):
                reply = QMessageBox.question(self, 'открыть ссылку', f'вы хотите открыть ссылку:\n{item.text()}',
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)  # Спрашиваем подтверждение перед открытием
                if reply == QMessageBox.StandardButton.Yes:
                    try:
                        webbrowser.open(item.text())
                        QMessageBox.information(self, 'успешно', 'ссылка открывается в браузере')
                    except Exception as e:
                        QMessageBox.critical(self, 'Error', f'не удалось открыть ссылку: {str(e)}')

    def add_employee(self):
        global USER_ID  # добавление нового конспекта
        if self.valid():
            download_inf_file_in_db(USER_ID, self.subject_name.text(), self.age.text())

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.subject_name.text().strip()))

        self.table.setItem(row, 3, QTableWidgetItem(self.age.text()))

        new_conspect = {'предмет': self.subject_name.text().strip(), 'дата': self.age.text()}
        self.conspect.append(new_conspect)

        self.update_filter_combo()  # обновляем фильтр и применяем текущий
        current_filter = self.filter_combo.currentText()
        if current_filter == "все предметы" or current_filter == new_conspect['предмет']:
            self.apply_filter(current_filter)

        self.reset()

    def delete(self):  # кнопка удаление конспекта
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Error', 'выберите строку, чтоб удалить')

        button = QMessageBox.question(self, 'Error', 'вы уверены, что хотите удалить выбранную строку?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if button == QMessageBox.StandardButton.Yes:  # получаем предмет удаляемой строки для обновления фильтра
            deleted_subject = self.table.item(current_row, 0).text()

            self.table.removeRow(current_row)
            if current_row < len(self.conspect):  # удаляем из списка conspect
                self.conspect.pop(current_row)

            self.update_filter_combo()  # обновляем фильтр
            current_filter = self.filter_combo.currentText()
            self.apply_filter(current_filter)
        return None

    def valid(self):
        subject_name = self.subject_name.text().strip()

        if not subject_name:
            QMessageBox.critical(self, 'Error', 'пожалуйста добавьте название предмета')
            self.subject_name.setFocus()
            return False
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
        self.age.clear()


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
        self.toggle_button2 = QPushButton("👁️")
        self.toggle_button2.setCheckable(True)
        self.toggle_button2.setFixedSize(QSize(24, 24))
        self.toggle_button2.clicked.connect(self.toggle_password_visibility2)

        self.log_button = QPushButton("зарегистрироваться", self)
        self.log_button.clicked.connect(self.process_registration)

        self.exit_button = QPushButton("назад", self)
        self.exit_button.clicked.connect(self.goto_MainWindow)

        logr_h_box = QHBoxLayout()
        pasr_h_box = QHBoxLayout()
        pasr2_h_box = QHBoxLayout()
        logr_h_box.addWidget(self.input_logr)
        pasr_h_box.addWidget(self.input_pasr)
        pasr_h_box.addWidget(self.toggle_button)
        pasr2_h_box.addWidget(self.input_pasr2)
        pasr2_h_box.addWidget(self.toggle_button2)
        main_v_box.addLayout(logr_h_box)
        main_v_box.addLayout(pasr_h_box)
        main_v_box.addLayout(pasr2_h_box)
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
        else:
            self.input_pasr.setEchoMode(QLineEdit.EchoMode.Password)

    def toggle_password_visibility2(self):
        if self.toggle_button2.isChecked():
            self.input_pasr2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input_pasr2.setEchoMode(QLineEdit.EchoMode.Password)


class First_Window(QWidget):  # окно открытия приложения, вход

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):  # задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600)  # 600, 200 - отступ при создании, 800, 600 - размер окна
        self.setWindowTitle("Авторизация")
        self.setUpFirst_Window()
        self.show()

    def setUpFirst_Window(self):  # расположение элементов на окне
        main_v_box = QVBoxLayout()
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
        pas_h_box.addWidget(self.toggle_button)
        main_v_box.addLayout(log_h_box)
        main_v_box.addLayout(pas_h_box)
        main_v_box.addWidget(self.ot_button)
        main_v_box.addWidget(self.log_button)

        self.setLayout(main_v_box)

    def validate_login_data(self):  # Проверяет валидность данных для авторизации
        global USER_ID
        username = self.input_log.text().strip()
        password = self.input_pas.text().strip()
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
