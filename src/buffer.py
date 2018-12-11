class Buffer:
    _filepath = None
    _buffer = None

    def __init__(self, _filepath):
        #Save the _filepath
        self._filepath = _filepath

        #Read file into _buffer
        file = open(self._filepath, "r");

        self._buffer = file.read().split("\n")
        self.deleteLine(len(self._buffer) - 1);

        file.close()

    #Buffer edit options
    def deleteLine(self, lineNumber):
        if lineNumber < len(self._buffer):
            del self._buffer[lineNumber]

    def insertLine(self, lineNumber, string):
        self._buffer.insert(lineNumber, string)

    def appendLine(self, lineNumber, string):
        self._buffer[lineNumber] += string; 

    def insertInLine(self, lineNumber, index, string):
        #Split the line
        line = self._buffer[lineNumber].split()

        #Insert in the line _buffer
        line.insert(index, string)

        #Join the string
        line = join(line)
            
        #Write the string back to the buffer
        self._buffer[lineNumber] = line
    
    #Other functions
    def getArrayOfLines(self):
        return self._buffer

    def getFilename(self):
        return self._filepath

    def getContent(self):
        return self._buffer

    #python property
