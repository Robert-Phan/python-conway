import sys; import time; import numpy

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import game

class Cell(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(15, 15)

class GUI(QWidget):

    def __init__(self, board: set[tuple]) -> None:
        super().__init__()
        game.live = board

        self.grid: QGridLayout = self.set_dimensions(40, 40)
        self.draw()

        layout = QVBoxLayout()
        layout.addItem(self.grid)
        layout.addWidget(QLabel("Click any keys to start/stop"))
        self.setLayout(layout)

        self.setStyleSheet("background-color: lightgrey")
        self.setWindowTitle("Life")

    def set_dimensions(self, w: int, h: int) -> QGridLayout:
        layout = QGridLayout()
        layout.setHorizontalSpacing(1)
        layout.setVerticalSpacing(1)

        for i in range(1, h+1):
            for j in range(1, w+1):
                t = QWidget()
                t.setFixedSize(15, 15)
                t.setStyleSheet("background-color:black")
                layout.addWidget(t, i, j)

        game.width = w; game.height = h
        return layout

    # draws results to the board
    def draw(self) -> None:
        for i in range(1, game.height+1):
            for j in range(1, game.width+1):
                self.grid.itemAtPosition(i, j).widget().setStyleSheet("background-color:black")
                ...
        for cell in game.live:
            x, y = cell
            x, y = x+1, y+1
            self.grid.itemAtPosition(y, x).widget().setStyleSheet("background-color:white")
            ...
        ...

    # updates board every time interval
    def timerEvent(self, a0: QTimerEvent) -> None:
        game.update()
        self.draw()
        ...

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        try:
            self.killTimer(self.timer_toggled)
            del self.timer_toggled
        except:
            self.timer_toggled = self.startTimer(150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    life = GUI({
        (20, 11),
        (21, 10),
        (22, 10),
        (21, 11), 
        (22, 12)
    })
    life.show()
    sys.exit(app.exec_())