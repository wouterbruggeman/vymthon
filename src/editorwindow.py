import curses
from bar import *
from texteditor import *
from commandinterpreter import *

class EditorWindow:
    _bar = Bar
    _textEditor = TextEditor
    _commandInterpreter = CommandInterpreter

    _aborted = False
    _stdscr = None
    _win = None
    _window_padding = 0
    _window_height = 0
    _window_width = 0
    _win = False

    def __init__(self, filepath):
        #Create text editor
        self._textEditor = TextEditor(self, filepath)

        #Create bar
        self._bar = Bar(self)

        #Create command interpreter
        self._commandInterpreter = CommandInterpreter(self._bar, self._textEditor, self)

        #Start curses
        self.cursesStart()

        #Setup other objects
        self.setInputMode("Normal")
        self._bar.setFilename(self._textEditor.getCurrentFilename())
    
        #Loop curses
        curses.wrapper(self.cursesLoop)
        self.cursesStop()
    
    def cursesStart(self):
        #Init curses
        self._stdscr = curses.initscr()

        #Curses settings
        curses.cbreak()
        self._stdscr.keypad(1)
        curses.noecho()

        #Create the window
        self.resizeWindow()
        self._win = curses.newwin(
            self._window_height - self._window_padding * 2,
            self._window_width - self._window_padding * 2,
            self._window_padding,
            self._window_padding
        )
        
        #Place bar at some position
        self._bar.setPosition(self._window_height - 2)
    
    def cursesStop(self):
        #Stop curses
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()
    
    def cursesLoop(self, stdscr):
        while 1:
            #Resize if needed
            resize = curses.is_term_resized(self._window_width, self._window_height)
            if resize == True:
                self.resizeWindow()

            #Refresh the window 
            self.redrawWindow()

            #Handle keypresses
            self.handleKeyPress()

            if self._aborted:
                break
            
    def redrawWindow(self):
        #Render the editor
        self._textEditor.draw()

        #Render the bar
        self._bar.draw()

        #TODO: is a refresh really needed?
        self._win.refresh()
        #self._stdscr.refresh()
    
    def resizeWindow(self):
        self._window_height, self._window_width = self._stdscr.getmaxyx()

        #If the window was not initialized
        if self._win != False:
            self.entry_height = self._window_height - self._window_padding * 2
            self._win.resize(
                self._window_height - self._window_padding * 2,
                self._window_width - self._window_padding * 2,
            )
            self._win.clear()
            self.redrawWindow()
            curses.doupdate()
    
    def addText(self, x, y, label):
        #Set some text at the given position
        try:
            self._win.addstr(y, x, label)
        except:
            pass

    def moveCursor(self, x, y):
            self._win.move(y,x) 
            curses.setsyx(y,x)

    def exit(self):
        self._aborted = True

    def setInputMode(self, inputMode):
        self._textEditor.setInputMode(inputMode)
        self._bar.setInputMode(inputMode);

        if inputMode == "Command":
            self._bar.setStatusMessage(":");

    def handleKeyPress(self):
        inputMode = self._textEditor.getInputMode()

        #Check for normal input
        if inputMode == "Normal":
            #Get char from input
            c = self._stdscr.getch()

            #Pressing - allows the user to go to a different mode
            if c == ord('i'):
                self.setInputMode("Insert")
            elif c == ord('r'):
                self.setInputMode("Replace")
            elif c == ord(':'):
                self.setInputMode("Command")
            else:
                #Dont update the screen or check for other input modes
                #if no (useful) key was pressed
                return
        
        #Redraw the window
        self.redrawWindow()
    
        #Check for command input
        if inputMode == "Command":
            cmd = self.getStringInput(1, self._bar.getPosition() + 1)
            self._commandInterpreter.interpret(cmd)
        
            #Return to normal
            self.setInputMode("Normal")

    def getStringInput(self, x, y):
        curses.echo()
        cmd = self._win.getstr(y, x).decode("utf-8")
        curses.noecho()
        return cmd
