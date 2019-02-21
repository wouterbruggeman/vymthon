from screenelement import *
from buffer import *
from cursor import *

class TextEditor(ScreenElement):

    def __init__(self, window):
        super().__init__(window)
        self._buffers = list()
        self._cursors = list()
        self._scrolledLines = list()

        self._activeBufferIndex = 0

    def draw(self):
        self.emptyArea()
            
        for y in range(self.getStartY(), self.getEndY()):
            lineIndex = self.getScrolledLines() + y

            #If out of range
            if lineIndex >= len(self.getBuffer().getContent()): 
                return

            self.drawLine(y, lineIndex)

    def drawLine(self, y, lineNumber):
        #Draw the linenumber
        self.drawLineNumber(y, lineNumber)

        #Draw the line
        self._window.addText(
            self.getOffsetX(),
            y,
            self.getBuffer().getContent()[lineNumber]
        )

    def drawLineNumber(self, y, lineNumber):
        #Draw the linenumber in color
        self._window.addText(0, y, str(lineNumber), 3)

    def openFile(self, filepath):
        #Check if file already exists in buffer
        index = 0
        for buf in self._buffers:
            if buf.getFilePath() == filepath:
                self.setActiveBuffer(index)
                return
            index += 1

        #File was not found in buffers list, create new buffer
        self._buffers.append(Buffer(filepath, self))
        
        #Open new buffer
        self.setActiveBuffer(len(self._buffers) - 1)

        #Create cursor
        self._cursors.append(Cursor(self.getBuffer(), self, self._window))

        #Append a new item to the scrolled lines list.
        self._scrolledLines.append(0) 

    def insertChar(self, char):
        self.getBuffer().insertInLine(
            self.getCursor().getLineNumber(),
            self.getCursor().getIndex(),
            char
        )
        self.redrawLine(self.getCursor().getLineNumber())
        self.getCursor().right()
    
    def replaceChar(self, char):
        self.getBuffer().replaceChar(
            self.getCursor().getLineNumber(),
            self.getCursor().getIndex(),
            char
        )
        self.redrawLine(self.getCursor().getLineNumber())

    def backspace(self):
        #Backspace at index 0
        if self.getCursor().getIndex() == 0:
            lineNumber = self.getCursor().getLineNumber()
            if lineNumber != 0:
                #Get original lettercount
                letterCount = self.getBuffer().getLetterCount(lineNumber)
                
                #Move the line
                self.getBuffer().moveLine(lineNumber, lineNumber - 1)
                
                #Move the cursor
                self.getCursor().up()
                self.getCursor().setIndex(
                    self.getBuffer().getLetterCount(lineNumber - 1) - letterCount
                )

        #Normal backspace
        else: 
            self.getBuffer().removeChar(
                self.getCursor().getLineNumber(),
                self.getCursor().getIndex() -1
            )
            #self.redrawLine(self.getCursor().getLineNumber())
            self.getCursor().left()

    def insertNewline(self):
        #Insert the line
        self.getBuffer().insertNewLine(
            self.getCursor().getLineNumber(),
            self.getCursor().getIndex())

        #Move the cursor
        self.getCursor().down()
        self.getCursor().setIndex(0);

    def setActiveBuffer(self, bufferIndex):
        self._activeBufferIndex = bufferIndex

    def getBuffer(self):
        return self._buffers[self._activeBufferIndex]

    def getCursor(self):
        return self._cursors[self._activeBufferIndex]

    def getScrolledLines(self):
        return self._scrolledLines[self._activeBufferIndex]

    def getOffsetX(self):
        return len(str(self.getBuffer().getLineCount())) + 1

    def scrollUp(self):
        self._scrolledLines[self._activeBufferIndex] -= 1

    def scrollDown(self):
        self._scrolledLines[self._activeBufferIndex] += 1
