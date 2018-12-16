from screenelement import *

class Bar(ScreenElement):
    _filename = ""
    _inputMode = ""
    _lineNumber = 0
    _procentY = 0
    _statusMessage = ""

    def __init__(self, window):
        super().__init__(window)

    def setFilename(self, filename):
        self._filename = filename
    
    def setInputMode(self, inputMode):
        self._inputMode = inputMode

        if inputMode == "Command":
            self.setStatusMessage(":");
    
    def setLineNumber(self, lineNumber):
        self._lineNumber = lineNumber;

    def setStatusMessage(self, message):
        self._statusMessage = message

    def setProcentY(self, procent):
        self._procentY = procent

    def getContent(self):
        string = "[" + self._inputMode + "]"
        string += "[" + str(self._lineNumber) + "]"
        string += "[" + str(round(self._procentY, 2)) + "%] "
        string += self._filename
        string += "\n"
        string += self._statusMessage
        return string
    
    def draw(self):
        self._window.addText(0, self.getStartY(), self.getContent())
