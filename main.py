import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Желтая окружность')
        self.pushButton.clicked.connect(self.draw_circle)


    def draw_circle(self):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)

        # Завершаем рисование
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(30, 30, 120, 130)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
