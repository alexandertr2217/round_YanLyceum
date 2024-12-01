import sys
from random import randrange

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow

class Osnova(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.naris)

    def paintEvent(self, event):
        if self.flag:
            qpai = QPainter()
            qpai.begin(self)
            self.ris(qpai)
            qpai.end()
        self.flag = False

    def naris(self):
        self.flag = True
        self.update()

    def ris(self, qpai):
        qpai.setBrush(QColor(255, 255, 2))
        for i in range(randrange(1, 10)):
            rad = randrange(1, 150)
            qpai.drawEllipse(randrange(1, 700), randrange(1, 600), rad, rad)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Osnova()
    ex.show()
    sys.exit(app.exec())
