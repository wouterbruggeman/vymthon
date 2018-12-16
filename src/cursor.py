from screenelement import *
from buffer import *
from texteditor import *

class Cursor(ScreenElement):
    _posX = 0
    _posY = 0

    _offsetX = 0

    def __init__(self, buffer, window, textEditor, offsetX):
        super().__init__(window)
        self._buffer = buffer
        self._textEditor = textEditor
        self._offsetX = offsetX


    #Navigate the cursor through the buffer
    def down(self):
        #Check if the view has to be scrolled down
        if ((self.getY() == self._textEditor.getEndY() - 1) and
            (self.getBufferY() < self._buffer.getLengthY() - 1)):

            #Move the cursor in the buffer, but don't update the screen position
            self._posY = self.getBufferY() + 1
            #Move the view
            self._textEditor.scrollDown()

            self.jumpLeft()
            return

        #Check the cursor can be moved down in the file
        if self.getBufferY() < (self._buffer.getLengthY() - 1):
            self._posY = self.getBufferY() + 1
            self.update()
            self.jumpLeft()

    def up(self):
        #Check if the view has to be scrolled up
        if ((self.getY() == self._textEditor.getStartY() + 1) and
            (self.getBufferY() > 0)):

            #Move the cursor in the buffer, but don't update the screen position
            self._posY = self.getBufferY() - 1
            #Move the view
            self._textEditor.scrollUp()

            self.jumpLeft()
            return


        #Check the cursor can be moved up in the file
        if self.getBufferY() > 0:
            self._posY = self.getBufferY() - 1
            self.update()
            self.jumpLeft()

    def left(self):
        #Check the cursor can be moved left in the file
        if self.getBufferX() > 0:
            self._posX = self.getBufferX() - 1
            self.update()

    def right(self):
        #Check the cursor can be moved right in the file
        if self.getBufferX() < self._buffer.getLengthX(self.getBufferY()):
            self._posX = self.getBufferX() + 1
            self.update()

    def jumpLeft(self):
        #Move the cursor to the left if needed
        if self.getX() > self._buffer.getLengthX(self.getY()):
            self._posX = self._buffer.getLengthX(self.getY())

    def update(self):
        self._window.moveCursor(
                self.getX(),
                self.getY()
                )
    
    #Get the real screen position
    def getX(self):
        return self._posX + self._offsetX

    def getY(self):
        return self._posY - self._textEditor.getScrolledY()

    #Get the buffer cursor position
    def getBufferX(self):
        return self._posX

    def getBufferY(self):
        return self._posY

    def getProcentY(self):
        return (100 / self._buffer.getLengthY()) * self.getBufferY()
