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

    def insertNewLine(self, lineNumber, index):
        #Split the line
        originalLine = list(self._buffer[lineNumber])
        currentLine = list()
        newLine = list()

        #Create a new line
        self._buffer.insert(lineNumber + 1, "")

        #Add all chars before index to the current line
        for x in range(0, index):
            currentLine.append(originalLine[x])

        #Add all chars after index to the next line
        for x in range(index, len(originalLine)):
            newLine.append(originalLine[x])

        #Add the lists to the lines
        self._buffer[lineNumber] = ''.join(currentLine)
        self._buffer[lineNumber + 1] = ''.join(newLine)

    def appendLine(self, lineNumber, string):
        self._buffer[lineNumber] += string; 

    def insertInLine(self, lineNumber, index, string):
        if index < 0:
            return

        #Split the line
        lineList = list(self._buffer[lineNumber])

        #Insert in the line _buffer
        lineList.insert(index, string)

        #Join the string
        lineStr = ''.join(map(str, lineList))
            
        #Write the string back to the buffer
        self._buffer[lineNumber] = lineStr

    def removeFromLine(self, lineNumber, index):
        if index < 0:
            return

        #Split the line
        lineList = list(self._buffer[lineNumber])

        #Remove the char
        del lineList[index]

        #Join the string
        lineStr = ''.join(map(str, lineList))
            
        #Write the string back to the buffer
        self._buffer[lineNumber] = lineStr

    def replaceChar(self, lineNumber, index, char):
        if index < 0:
            return

        #Split the line
        lineList = list(self._buffer[lineNumber])

        #Remove the char
        lineList[index] = char

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
