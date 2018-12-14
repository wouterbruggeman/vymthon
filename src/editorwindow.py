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
        #Create bar
        self._bar = Bar()
        self._bar.setInputMode("Normal")
    
        #Create text editor
        self._textEditor = TextEditor(filepath)
        self._textEditor.setInputMode("Normal")

        #Create command interpreter
        self._commandInterpreter = CommandInterpreter(self._bar, self._textEditor, self)

        #Setup curses stuff
        self.cursesStart()
        curses.wrapper(self.cursesLoop)
        self.cursesStop()
    
    def cursesStart(self):
        #Init curses
        self._stdscr = curses.initscr()

        #Curses settings
        curses.cbreak()
        self._stdscr.keypad(1)
        curses.noecho()

        self._stdscr.addstr(0,10,"Hit 'q' to quit")
        self._stdscr.refresh()

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
            self._stdscr.refresh()
        except:
            pass

    def moveCursor(self, x, y):
            self._win.move(y,x) 
            curses.setsyx(y,x)

    def exit(self):
        self._aborted = True

    def redrawWindow(self):
        #Render the editor
        yCounter = 0
        for line in self._textEditor.getContent():
            self.addText(0, yCounter, line)
            yCounter += 1

        #Render the bar
        self._bar.setFilename(self._textEditor.getCurrentFilename())
        self.addText(0, self._bar.getPosition(),
                self._bar.getContent())

        #TODO: is a refresh really needed?
        self._win.refresh()
        
    def setInputMode(self, inputMode):
        self._textEditor.setInputMode(inputMode)
        self._bar.setInputMode(inputMode);

        if inputMode == "Command":
            self._bar.setStatusMessage(":");

        elif inputMode == "Normal":
            self._bar.setStatusMessage("");

        #TODO: REMOVE LINE BELOW
        #self.redrawWindow()
        self.redrawWindow()
    
    def handleKeyPress(self):
            inputMode = self._textEditor.getInputMode()

            #Get char from input
            c = self._stdscr.getch()

            #Pressing - allows the user to go to a different mode
            if c == ord('-'):
                self.setInputMode("Normal")
            elif c == ord('i'):
                self.setInputMode("Insert")
                self.moveCursor(9,0);
            elif c == ord('r'):
                self.setInputMode("Replace")
                self.moveCursor(9,0);
            elif c == ord(':'):
                self.setInputMode("Command")

                cmd = self.getStringInput(1, self._bar.getPosition() + 1)
                self._commandInterpreter.interpret(cmd)

                #Change mode
                self.setInputMode("Normal")

    def getStringInput(self, x, y):
        curses.echo()
        cmd = self._win.getstr(y, x).decode("utf-8")
        curses.noecho()
        return cmd
