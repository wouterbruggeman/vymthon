from bar import *
from texteditor import * 
from commandinterpreter import *
from cursor import *

class InputHandler:
    _inputMode = "Normal"
    _bar = Bar
    _textEditor = TextEditor
    _window = None
    _commandInterpreter = CommandInterpreter

    def __init__(self, bar, textEditor, window):
        self._bar = bar
        self._textEditor = textEditor
        self._window = window
        self._commandInterpreter = CommandInterpreter(self._bar, self._textEditor, window)

        self._bar.setInputMode(self._inputMode)
        self._textEditor.setInputMode(self._inputMode)
    
    def setInputMode(self, inputMode):
        self._inputMode = inputMode

        self._textEditor.setInputMode(inputMode)
        self._bar.setInputMode(inputMode);

    def getInputMode(self):
        return self._inputMode

    def handleKeyPress(self):
        #Get the cursor
        cursor = self._textEditor.getCursor()
        cursor.update()

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
                cursor.down()
            elif c in [curses.KEY_UP, ord('k')]:
                cursor.up()
            elif c in [curses.KEY_RIGHT, ord('l')]:
                cursor.right()
            elif c in [curses.KEY_LEFT, ord('h')]:
                cursor.left()
            #elif c == ord("G"):
                #TODO: cursor.moveToBottom()
            #elif c == ord("g"):
                #TODO: cursor.moveToTop()
        elif self._inputMode == "Insert":
            while True:
                c = self._window._stdscr.getch()
                if c == ord('`'):
                    break;
                #if c == curses.KEY_BACKSPACE:
                    #self._textEditor.removeChar()
                #if c == curses.KEY_ENTER:
                    #self._textEditor.insertNewline()
                else:
                    #Tmp way to insert text
                    self._textEditor.insertChar(chr(c))
                    
            

            #return to normal
            self.setInputMode("Normal")

        elif self._inputMode == "Replace":
            while True:
                c = self._window._stdscr.getch()
                if c == ord('`'):
                    break;

            #TODO: Replace char
    
            #return to normal
            self.setInputMode("Normal")

        elif self._inputMode == "Command":
            cmd = self.getStringInput(1, self._bar.getStartY() + 1)
            self._commandInterpreter.interpret(cmd)
        
            #Return to normal
            self.setInputMode("Normal")


    def getStringInput(self, x, y):
        curses.echo()
        cmd = self._window._win.getstr(y, x).decode("utf-8")
        curses.noecho()
        return cmd
