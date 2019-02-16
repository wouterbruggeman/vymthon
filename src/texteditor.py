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
            
        lineCounter = 0
        for line in self.getCurrentBuffer().getContent():
            currentY = lineCounter - self._scrolledLines[self._activeBufferIndex]

            #Make sure we dont draw over other screen elements
            if (currentY >= self.getStartY()) and (currentY < self.getEndY()):

                #Draw the lines
                self.drawLineNumber(
                        lineCounter - self._scrolledLines[self._activeBufferIndex],
                        lineCounter)
                self._window.addText(self.getOffsetX(), currentY, line)
            
            lineCounter += 1

        self.getCursor().draw()

    def drawLineNumber(self, y, lineNumber):
        #Draw the linenumber in color
        self._window.addText(0, y, str(lineNumber), 3)

   #TODO: Move these functions to the buffer class
    def getLineNumber(self):
        #TODO:
        return 0
    
    def getProcentY(self):
        #TODO:
        return 0
    
    def getCurrentFilename(self):
        #TODO:
        return "Filename"

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
        self._scrolledLines.append(0)
        
        #Open new buffer
        self.setActiveBuffer(len(self._buffers) - 1)

        #Create cursor
        self._cursors.append(Cursor(self.getBuffer(), self, self._window))

    def setActiveBuffer(self, bufferIndex):
        self._activeBufferIndex = bufferIndex

    def getCurrentBuffer(self):
        return self._buffers[self._activeBufferIndex]

    def getOffsetX(self):
        return len(str(self.getCurrentBuffer().getLineCount())) + 1

    def getCursor(self):
        return self._cursors[self._activeBufferIndex]

    def getBuffer(self):
        return self._buffers[self._activeBufferIndex]

    def getScrolledLines(self):
        return self._scrolledLines[self._activeBufferIndex]
