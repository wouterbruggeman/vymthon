from commandinterpreter import *
from texteditor import *
from statusbar import *
from window import *

class InputHandler:

    def __init__(self, textEditor, statusBar, window):
        self._textEditor = textEditor
        self._statusBar = statusBar
        self._window = window
        
        self._inputMode = "Normal"

        self._commandInterpreter = CommandInterpreter(
                self._statusBar, self._textEditor, window)

    def setInputMode(self, inputMode):
        self._inputMode = inputMode

    def getInputMode(self):
        return self._inputMode

    def handleKeyPress(self):
        #Check for normal input
        if self._inputMode == "Normal":

            #Get char from input
            c = self._window._stdscr.getch()

            #Mode switching
            if c == ord('i'):
                self.setInputMode("Insert")
            elif c == ord('r'):
                self.setInputMode("Replace")
            elif c == ord(':'):
                self.setInputMode("Command")
                
            #Cursor movement
            elif c in [curses.KEY_DOWN, ord('j')]:
                self._textEditor.getCursor().down()
            
            elif c in [curses.KEY_UP, ord('k')]:
                self._textEditor.getCursor().up()
            elif c in [curses.KEY_RIGHT, ord('l')]:
                cursor.right()
            elif c in [curses.KEY_LEFT, ord('h')]:
                cursor.left()
            #elif c == ord("G"):
                #TODO: cursor.moveToBottom()
            #elif c == ord("g"):
                #TODO: cursor.moveToTop()


        elif self._inputMode == "Insert":
            #Get char from input
            c = self._window._stdscr.getch()
            
            #ESCAPE = 27
            if c == 27:
                self.setInputMode("Normal")

            #BACKSPACE = 8 ascii or curses.KEY_BACKSPACE
            elif c == curses.KEY_BACKSPACE:
                self._textEditor.backspace()
            
            #ENTER = 10 ascii
            elif c == 10:
                self._textEditor.insertNewline()

            #Insert all other characters
            else:
                self._textEditor.insertChar(chr(c))

        elif self._inputMode == "Replace":
            #Get char from input
            c = self._window._stdscr.getch()
            
            #ESCAPE = 27
            if c == 27:
                self.setInputMode("Normal")

            else:
                #Replace the current char
                self._textEditor.replaceChar(chr(c))

                #Change input mode back to normal
                self.setInputMode("Normal")

        elif self._inputMode == "Command":
            #Show the ':' char
            self._statusBar.setStatusMessage(":")
    
            #Ask for input and interpret the command
            cmd = self._window.getString(1, self._statusBar.getStartY() + 1)
            self._commandInterpreter.interpret(cmd)
        
            #Clear the status message 
            self._statusBar.setStatusMessage("")
        
            #Return to normal mode
            self.setInputMode("Normal")
