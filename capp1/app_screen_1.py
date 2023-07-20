import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ui_path = 'capp1/app_screen_1.ui'
        uic.loadUi(ui_path, self)
        self.setWindowTitle('My First Application')

if __name__== '__main__': 
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())


