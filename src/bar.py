class Bar:
    _filename = ""
    _inputMode = ""
    _lineNumber = 0
    _statusMessage = ""

    def setFilename(self, filename):
        self._filename = filename
    
    def setInputMode(self, inputMode):
        self._inputMode = inputMode
    
    def setLineNumber(self, lineNumber):
        self._lineNumber = lineNumber;

    def setStatusMessage(self, message):
        self._statusMessage = message

    def getContent(self):
        string = "[" + self._inputMode + "]"
        string += "[" + str(self._lineNumber) + "] "
        string += self._filename
        string += "\n"
        string += self._statusMessage
        return string
