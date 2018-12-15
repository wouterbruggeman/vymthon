from buffer import *
from screenelement import *

class Cursor(ScreenElement):
    _posX = 0
    _posY = 0

    _offsetX = 0
    _offsetY = 0

    def __init__(self, buffer, window, offsetX):
        super().__init__(window)
        self._buffer = buffer
        self._offsetX = offsetX

    def down(self):
        if self.getY() < (self._buffer.getLengthY() - 1):
            self.move(self.getX(), self.getY() + 1)

        if self.getX() > self._buffer.getLengthX(self.getY()):
            self.move(self._buffer.getLengthX(self.getY()), self.getY())

    def up(self):
        if self.getY() > 0:
            self.move(self.getX(), self.getY() - 1)
        
        if self.getX() > self._buffer.getLengthX(self.getY()):
            self.move(self._buffer.getLengthX(self.getY()), self.getY())

    def left(self):
        if self.getX() > 0:
            self.move(self.getX() - 1, self.getY())

    def right(self):
        if self.getX() < self._buffer.getLengthX(self.getY()):
            self.move(self.getX() + 1, self.getY())

    def move(self, x, y):
        self._posX = x
        self._posY = y
        self.update()

    def update(self):
        self._window.moveCursor(
                self._posX + self._offsetX, 
                self._posY + self._offsetY
                )

    def getX(self):
        return self._posX

    def getY(self):
        return self._posY 
