import sys; import time; import re; from typing import Union

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import game

class GUI(QWidget):

    def __init__(self, board: Union[set[tuple], str], w: int = 40, h: int = 40) -> None:
        super().__init__()
        if type(board) == str: board = game.rle(board)
        game.live = set(board)

        self.grid: QGridLayout = self.set_dimensions(w, h)
        self.draw()

        self.label = QLabel('Type "play" to start the simulation. \
        \nType {X, Y} coordinates or RLE to add/remove cell.')
        self.label.setFont(QFont("Roboto", pointSize=10))
        self.label.setStyleSheet("background-color: black; color: white")

        self.input = QLineEdit()
        self.input.setFont(QFont("Roboto", pointSize=10))
        self.input.returnPressed.connect(self.process_input)

        layout = QVBoxLayout()
        layout.addItem(self.grid)
        layout.addWidget(self.label)
        layout.addWidget(self.input)
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

    def process_input(self):
        if self.input.text() == "play" or self.input.text() == "stop":
            self.play()
        elif re.search(r"\d+, *\d+", self.input.text()):
            x, y = self.input.text().split(",")
            x, y = int(x), int(y)
            if (x, y) in game.live:
                game.live.remove((x, y))
            else:
                game.live.add((x, y))
            self.draw()
        elif self.input.text() == "clear":
            game.live = set()
            self.generations = 0
            self.draw()
            self.label.setText('Type "play" to start the simulation.\
            \nType {X, Y} coordinates or RLE to add/remove cell.')
            ...
        elif rle := game.rle(self.input.text()):
            game.live = rle
            self.draw()
            ...
        self.input.clear()

    def play(self):
        try:
            self.killTimer(self.timer_toggled)
            del self.timer_toggled
            self.label.setText('Type "play" to continue the simulation.\nType "clear" to clear the board.')
        except:
            self.timer_toggled = self.startTimer(150)
    
    generations = 0
    def timerEvent(self, a0: QTimerEvent) -> None:
        self.prev = game.live
        game.update()
        self.draw()
        self.label.setText(f"Generations: {self.generations}\nType \"stop\" to stop the simulation.")
        self.generations += 1
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    life = GUI("bo$2bo$3o")
    life.show()

    sys.exit(app.exec_())