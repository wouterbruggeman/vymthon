from screenelement import *
from texteditor import *
from inputhandler import *

class StatusBar(ScreenElement):
    _textEditor = None
    _inputHandler = None
    _statusMessage = ""
    
    #Initialize the statusbar with a window and a texteditor object
    def __init__(self, window, textEditor, inputHandler):
        super().__init__(window)
        self._textEditor = textEditor
        self._inputHandler = inputHandler
    
    def setStatusMessage(self, message):
        _statusMessage = message

    def draw(self):
        content = "[" + self._inputHandler.getInputMode() + "]"
        content += "[" + str(self._textEditor.getLineNumber()) + "]"
        content += "[" + str(round(self._textEditor.getProcentY(), 2)) + "%] "
        content += self._textEditor.getCurrentFilename()
        content += "\n"

        self._window.addText(0, self.getStartY(), content)
        self._window.addText(0, self.getStartY() + 1, self._statusMessage)
