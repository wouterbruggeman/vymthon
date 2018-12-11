import curses
from buffer import *

class TextEditor:
    _buffer = Buffer
    _cursorOnLine = 0
    _cursorOnRow = 0

    def __init__(self, filepath):
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
        
    #def openFile(self, filename):
        #self._buffer = Buffer(filename)
