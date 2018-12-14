from buffer import *
from screenelement import *

class TextEditor(ScreenElement):
    _inputMode = ""
    _buffer = Buffer
    _cursorOnLine = 0
    _cursorOnRow = 0

    def __init__(self, window, filepath):
        super().__init__(window)
        self._buffer = Buffer(filepath)

    def getCurrentFilename(self):
        return self._buffer.getFilename()

    def setInputMode(self, inputMode):
        self._inputMode = inputMode

    def getInputMode(self):
        return self._inputMode

    def getContent(self):
        content = []
        lineCounter = 0
        for line in self._buffer.getContent():
            content.append(str(lineCounter) + "\t| " + line)
            lineCounter += 1
             
        return content 

    def saveBuffer(self):
        #TODO: implement this feature
        return "Written to file: " + self.getCurrentFilename()

    def openFile(self, filename):
        #TODO: implement multiple buffers
        self._buffer = Buffer(filename)

    def draw(self):
        yCounter = 0
        for line in self.getContent():
            self._window.addText(0, yCounter, line)
            yCounter += 1
