from buffer import *
from screenelement import *
from cursor import *

class TextEditor(ScreenElement):
    _inputMode = ""
    _buffer = Buffer
    _cursor = Cursor

    _offsetX = 0
    _scrolledY = 0

    def __init__(self, window, filepath):
        super().__init__(window)
        self._buffer = Buffer(filepath)
       
        #Calculate offset
        lineCount = len(self._buffer.getContent())
        self._offsetX = self.getOffsetX(lineCount) + 1

        self._cursor = Cursor(self._buffer, self._window, self, self._offsetX)

    def getCurrentFilename(self):
        return self._buffer.getFilename()

    def setInputMode(self, inputMode):
        self._inputMode = inputMode
    
    def getInputMode(self):
        return self._inputMode

    def saveBuffer(self):
        self._buffer.saveToFile()
        return "Written to file: " + self.getCurrentFilename()

    def openFile(self, filename):
        #TODO: implement multiple buffers
        self._buffer = Buffer(filename)

    def draw(self):
        self.emptyArea()

        lineCounter = 0
        for line in self._buffer.getContent():
            currentY = lineCounter - self._scrolledY

            #Make sure we dont draw over other screen elements
            if (currentY > self.getStartY()) and (currentY < self.getEndY()):
                #Draw the lines
                self.drawLineNumber(lineCounter - self._scrolledY, lineCounter)
                self._window.addText(self._offsetX, currentY, line)
            
            lineCounter += 1

    def redrawLine(self, lineNumber):
        #Draw empty line 
        for i in range(self._window.getWidth()):
            self._window.addText(self._offsetX + i, lineNumber - self._scrolledY, " ")

        #Draw the line
        line = self._buffer.getContent()[lineNumber]
        self._window.addText(self._offsetX, lineNumber - self._scrolledY, line)


    def getOffsetX(self, y):
         return len(str(y))
    
    def drawLineNumber(self, y, lineNumber):
        #Draw the number in color
        self._window.addText(0, y, str(lineNumber), 3)

    def getCursor(self):
        return self._cursor

    def scrollUp(self):
        if self._scrolledY > 0:
            self._scrolledY -= 1
            self.draw();

    def scrollDown(self):
        if self._scrolledY < len(self._buffer.getContent()):
            self._scrolledY += 1
            self.draw();

    def getScrolledY(self):
        return self._scrolledY

    def insertChar(self, char):
        self._buffer.insertInLine(self._cursor.getBufferY(), self._cursor.getBufferX(), char)
        self.redrawLine(self._cursor.getBufferY())
        self._cursor.right()
    
    def replaceChar(self, char):
        self._buffer.replaceChar(self._cursor.getBufferY(), self._cursor.getBufferX(), char)
        self.redrawLine(self._cursor.getBufferY())

    def removeChar(self):
        self._buffer.removeFromLine(self._cursor.getBufferY(), self._cursor.getBufferX() -1)
        self.redrawLine(self._cursor.getBufferY())
        self._cursor.left()

    def insertNewline(self):
        #Insert the line
        self._buffer.insertNewLine(self._cursor.getBufferY(), self._cursor.getBufferX())

        #Move the cursor
        self._cursor.down()
        self._cursor.setBufferX(0);
        self.draw();
