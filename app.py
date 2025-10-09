import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap #для картинок

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):#задача базовых настроек приложения
        self.setGeometry(600, 200, 800, 600) #600, 200 - отступ при создании, 800б 600 - размер окна
        self.setWindowTitle("заголовок окна")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):#расположение элементов на окне
        pass

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec()) #открытие приложения