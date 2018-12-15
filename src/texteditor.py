from buffer import *
from screenelement import *
from cursor import *

class TextEditor(ScreenElement):
    _inputMode = ""
    _buffer = Buffer
    _cursor = Cursor

    _drawHeight = 0
    _offsetX = 0

    def __init__(self, window, filepath):
        super().__init__(window)
        self._buffer = Buffer(filepath)
       
        #Calculate offset
        lineCount = len(self._buffer.getContent())
        self._offsetX = self.getOffsetX(lineCount) + 1

        self._cursor = Cursor(self._buffer, self._window, self._offsetX)

    def getCurrentFilename(self):
        return self._buffer.getFilename()

    def setInputMode(self, inputMode):
        self._inputMode = inputMode
    
    def setHeight(self, height):
        self._drawHeight = height

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
            if yCounter < self._drawHeight:
                #Draw the lines
                self.drawLineNumber(yCounter)
                #line = str(yCounter) + " | " + line
                self._window.addText(self._offsetX, yCounter, line)
                yCounter += 1

    def getOffsetX(self, y):
         return len(str(y))
    
    def drawLineNumber(self, y):
        #Draw the number in color
        self._window.addText(0, y, str(y), 3)


    def getCursor(self):
        return self._cursor
