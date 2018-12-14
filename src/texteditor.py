from buffer import *
from screenelement import *

class TextEditor(ScreenElement):
    _inputMode = ""
    _buffer = Buffer

    _cursorPosX = 0
    _cursorPosY = 0

    _offsetX = 4
    _offsetY = 0

    _height = 0

    def __init__(self, window, filepath):
        super().__init__(window)
        self._buffer = Buffer(filepath)

    def getCurrentFilename(self):
        return self._buffer.getFilename()

    def setInputMode(self, inputMode):
        self._inputMode = inputMode
    
    def setHeight(self, height):
        self._height = height

    def getInputMode(self):
        return self._inputMode

    def saveBuffer(self):
        #TODO: implement this feature
        return "Written to file: " + self.getCurrentFilename()

    def openFile(self, filename):
        #TODO: implement multiple buffers
        self._buffer = Buffer(filename)

    def draw(self):
        yCounter = 0
        for line in self._buffer.getContent():
            
            #Make sure we dont draw over other screen elements
            if yCounter < self._height:
                #Draw the lines
                line = str(yCounter) + " | " + line
                self._window.addText(0, yCounter, line)
                yCounter += 1

    def getLineNumberWidth(self, y):
         return len(str(y))


    def cursorDown(self):
        if self._cursorPosY < (self._buffer.getLengthY() - 1):
            self._cursorPosY += 1
            self.moveCursor(self._cursorPosX, self._cursorPosY)

    def cursorUp(self):
        if self._cursorPosY > 0:
            self._cursorPosY -= 1
            self.moveCursor(self._cursorPosX, self._cursorPosY)

    def cursorLeft(self):
        if self.getBufferCursorX() > 0:
            self._cursorPosX -= 1
            self.moveCursor(self._cursorPosX, self._cursorPosY)

    def cursorRight(self):
        if self.getBufferCursorX() < self._buffer.getLengthX(self.getBufferCursorY()):
            self._cursorPosX += 1
            self.moveCursor(self._cursorPosX, self._cursorPosY)

    def moveCursor(self, x, y):
        self._cursorPosX = x
        self._cursorPosY = y
        self.updateCursor()

    def updateCursor(self):
        self._window.moveCursor(self.getCursorX(), self.getCursorY())

    def getCursorX(self):
        return (self._cursorPosX + self._offsetX)

    def getCursorY(self):
        return (self._cursorPosY + self._offsetY)

    def getBufferCursorX(self):
        return self._cursorPosX

    def getBufferCursorY(self):
        return self._cursorPosY 
