from screenelement import *
from buffer import *

class TextEditor(ScreenElement):
    _inputMode = "Normal"
    _buffers = None
    _buffersScrolledLines = None
    _activeBufferIndex = 0

    def __init__(self, window):
        super().__init__(window)
        self._buffers = list()
        self._buffersScrolledLines = list()
       
    def draw(self):
        self.emptyArea()
            

        lineCounter = 0
        for line in self.getCurrentBuffer().getContent():
            currentY = lineCounter - self._buffersScrolledLines[self._activeBufferIndex]

            #Make sure we dont draw over other screen elements
            if (currentY > self.getStartY()) and (currentY < self.getEndY()):

                #Draw the lines
                self.drawLineNumber(lineCounter - self._scrolledY, lineCounter)
                self._window.addText(self._offsetX, currentY, line)
            
            lineCounter += 1

        self._window.addText(0, 0, self.getCurrentBuffer().getFilePath())
        self._window.addText(0, 1, self.getCurrentBuffer().getFileName())
        self._window.addText(0, 3, str(len(self.getCurrentBuffer().getContent())))

    def drawLineNumber(self, y, lineNumber):
        #Draw the linenumber in color
        self._window.addText(0, y, str(lineNumber), 3)

    def getInputMode(self):
        return self._inputMode
   

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
        self._buffersScrolledLines.append(0)
        
        #Open new buffer
        self.setActiveBuffer(len(self._buffers) - 1)

    def setActiveBuffer(self, bufferIndex):
        self._activeBufferIndex = bufferIndex

    def getCurrentBuffer(self):
        return self._buffers[self._activeBufferIndex]
