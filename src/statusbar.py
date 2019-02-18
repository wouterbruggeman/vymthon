from screenelement import *
from texteditor import *
from inputhandler import *

class StatusBar(ScreenElement):
    #Initialize the statusbar with a window and a texteditor object
    def __init__(self, window, textEditor):
        super().__init__(window)
        self._textEditor = textEditor
        self._statusMessage = ""

    def setInputHandler(self, inputHandler):
        self._inputHandler = inputHandler
    
    def setStatusMessage(self, message):
        #Show the message directly, without waiting for the draw method to be called
        self._statusMessage = message
        self._window.addText(0, self.getStartY() + 1, self._statusMessage)

    def draw(self):
        self.emptyArea()
        content = "[" + self._inputHandler.getInputMode() + "]"
        content += "[" + str(self._textEditor.getCursor().getLineNumber()) + "]"
        content += "[" + str(round(self._textEditor.getCursor().getProcentY(), 2)) + "%] "
        content += self._textEditor.getBuffer().getFileName()

        self._window.addText(0, self.getStartY(), content)
        self._window.addText(0, self.getStartY() + 1, self._statusMessage)
