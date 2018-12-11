class Bar:
    _filename = ""
    _inputMode = ""
    _lineNumber = 0

    def setFilename(self, filename):
        self._filename = filename
    
    def setInputMode(self, inputMode):
        self._inputMode = inputMode
    
    def setLineNumber(self, lineNumber):
        self._lineNumber = lineNumber;

    def getContent(self):
        string = "[" + self._inputMode + "]"
        string += "[" + str(self._lineNumber) + "] "
        string += self._filename
        return string
