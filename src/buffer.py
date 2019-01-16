class Buffer:
    _filepath = None
    _buffer = None

    def __init__(self, _filepath):
        #Save the _filepath
        self._filepath = _filepath

        #Read file into _buffer
        file = open(self._filepath, "r");

        self._buffer = file.read().split("\n")
        #TODO: CHECK THIS self.deleteLine(len(self._buffer) - 1);

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
        lineList = list(self._buffer[lineNumber])

        #Insert in the line _buffer
        lineList.insert(index, string)

        #Join the string
        lineStr = ''.join(map(str, lineList))
            
        #Write the string back to the buffer
        self._buffer[lineNumber] = lineStr

    def removeFromLine(self, lineNumber, index):
        #Split the line
        lineList = list(self._buffer[lineNumber])

        #Insert in the line _buffer
        del lineList[index]

        #Join the string
        lineStr = ''.join(map(str, lineList))
            
        #Write the string back to the buffer
        self._buffer[lineNumber] = lineStr
    
    #Other functions
    def getArrayOfLines(self):
        return self._buffer

    def getFilename(self):
        return self._filepath

    def getContent(self):
        return self._buffer

    def getLengthY(self):
        return len(self._buffer)

    def getLengthX(self, y):
        return len(self._buffer[y])

    def saveToFile(self):
        #TODO: implement this feature
        return
