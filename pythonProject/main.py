from PIL import Image, ImageDraw
import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys  #  загружаем библиотеки и различные модули
from PyQt5 import uic  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QApplication, QMainWindow  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QWidget, QPushButton  #  загружаем библиотеки и различные модули
from PyQt5.QtGui import QPixmap  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow  #  загружаем библиотеки и различные модули
from PIL import Image, ImageFilter  #  загружаем библиотеки и различные модули
from PIL import Image, ImageDraw #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QColorDialog  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)  #  загружаем библиотеки и различные модули
from PyQt5.QtCore import Qt #  загружаем библиотеки и различные модули


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # соединили проект в дизанере и программу

        self.pushButton.clicked.connect(self.run1)  # делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton.setStyleSheet("background-color: rgb(153, 50, 204);")  # изменяем цвет кнопки

    def run1(self):  # создаём функцию, которой при входе не задаются аргументы
        im = Image.new("RGB", (500, 500))
        k = ['#87CEEB', '#017B92', '#874535', '#FFFFFF', '#FFCF40']
        p = random.randint(1, 5)
        drawer = ImageDraw.Draw(im)
        drawer.ellipse((
            (int(0.8 * 500), -int(0.2 * 500)),
            (int(1.2 * 400), int(0.2 * 500))),
            k[p])
        p = random.randint(0, 4)
        drawer.ellipse((
            (int(0.8 * 250), -int(0.2 * 500)),
            (int(1.2 * 250), int(0.2 * 500))),
            k[p])
        p = random.randint(1, 5)
        drawer.ellipse((
            (int(0.8 * 100), -int(0.2 * 50)),
            (int(1.2 * 100), int(0.2 * 50))),
            k[p])
        im.save('res1.jpg')  # сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  # загружаем картинку
        self.label.setPixmap(self.pixmap)  # открываем картинку в label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())