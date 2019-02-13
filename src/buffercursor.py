from buffer import *
from texteditor import *

class BufferCursor:
    _buffer = None
    _textEditor = None

    _index = 0
    _lineNumber = 0

    def __init__(self, buffer, textEditor):
        _buffer = buffer 
        _textEditor = textEditor

    #Navigate the cursor through the buffer
    def down(self):
        #Check if the view has to be scrolled down
        if ((self.getRealY() == (self._textEditor.getEndY() - 1)) and 
            (self.getRealY() < self._buffer.getLineCount())):

            #Move the view
            self._buffer.scrollDown()

        #Check the cursor can be moved down in the file
        if self._lineNumber < (self._buffer.getLineCount()):
            self._lineNumber += 1 
            self.jumpLeftIfNeeded()

    def up(self):
        #Check if the view has to be scrolled down
        if ((self.getRealY() == self._textEditor.getStartY()) and
            (self.getRealY() > self._buffer.getLineCount())):

            #Move the view
            self._buffer.scrollUp()

        #Check the cursor can be moved down in the file
        if self._lineNumber > (self._buffer.getLineCount()):
            self._lineNumber -= 1 
            self.jumpLeftIfNeeded()

    def left(self):
        #Check the cursor can be moved left in the file
        if self._index > 0:
            self._index -= 1
            self.draw()

    def right(self):
        #Check the cursor can be moved right in the file
        if self._index < self._buffer.getLetterCount(self._lineNumber):
            self._index += 1
            self.draw()
    
    #def moveToTop(self):
        #TODO: CHECK THIS CODE
    #    self._scrolledY = 0
    #    self._posY = 0;
    #    self.draw()

    #def moveToBottom(self):
        #TODO: FIX THIS CODE
    #    self._scrolledY = self._buffer.getLengthY() - self._textEditor.getEndY()
    #    self._posY = self._textEditor.getEndY()
    #    self.draw()

    def jumpLeftIfNeeded(self):
        #Move the cursor to the left if needed
        if self._index > self._buffer.getLetterCount(self._lineNumber):
            self._index = self._buffer.getLetterCount(self._lineNumber)
            self.draw()

    def draw(self):
        self._window.moveCursor(self.getRealX(), self.getRealY())
    
    def getProcentY(self):
        return (100 / self._buffer.getLineCount()) * self._lineNumber() + 1

    def getRealX(self):
        return self._index + self._textEditor.getOffsetX()
    
    def getRealY(self):
        return self._lineNumber - self._textEditor.getScrolledLines()