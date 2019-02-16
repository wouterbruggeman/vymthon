from texteditor import *
import os.path

class Buffer:

    def __init__(self, filepath, textEditor):
        self._filepath = filepath
        self._textEditor = textEditor

        self.openFile(filepath)

    def openFile(self, filepath):
        
        if os.path.isfile(filepath):
            #File exists, read into buffer
            file = open(filepath, "r");
            self._buffer = file.read().split("\n")
            
            #If there is no content
            if len(self._buffer) == 0:
                #Add empty line
                #self._buffer.insert(0, "")
                pass
            else:
                #Delete last empty line (created for all newline chars)
                self.deleteLine(len(self._buffer) - 1);

        else:
            #File does not exists, create new file
            file = open(filepath, "w");

            #Create empty buffer
            self._buffer = list()
            self._buffer.append("")

        #Close file
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

    def backspace(self, lineNumber, index):
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
    
    def getFileName(self):
        path = self._filepath.split("/")
        return path[len(path) - 1]

    def getFilePath(self):
        return self._filepath
    
    def saveToFile(self):
        #TODO: implement this feature
        return

    def getLineCount(self):
        return len(self._buffer) - 1

    def getLetterCount(self, lineNumber):
        return len(list(self._buffer[lineNumber]))

    def getContent(self):
        return self._buffer
