import curses
from buffer import *
from bar import *
from texteditor import *

class EditorWindow:
    _bar = Bar
    _textEditor = TextEditor

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

        #Setup curses stuff
        self.cursesStart()
        curses.wrapper(self.cursesLoop)
        self.cursesStop()
    
    def cursesStart(self):
        #Init curses
        self._stdscr = curses.initscr()

        #Curses settings
        self._stdscr.keypad(1)
        curses.noecho()
        curses.cbreak()

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
    
    def cursesStop(self):
        #Stop curses
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def setText(self, x, y, label):
        #Set some text at the given position
        try:
            self._win.addstr(y, x, label)
        except:
            pass

    def moveCursor(self, x, y):
            self._win.move(y,x) 
            curses.setsyx(y,x)

    def redrawWindow(self):
        #TODO: is a refresh really needed?
        self._win.refresh()

        #Render the editor
        yCounter = 0
        for line in self._textEditor.getContent():
            self.setText(0, yCounter, line)
            yCounter += 1

        #Render the bar
        self._bar.setFilename(self._textEditor.getCurrentFilename())
        self.setText(0, self._bar.getPosition(),
                self._bar.getContent())


        
    def cursesLoop(self, stdscr):
        while 1:
            #Resize if needed
            resize = curses.is_term_resized(self._window_width, self._window_height)
            if resize == True:
                self.resizeWindow()

            #Refresh the window 
            self._win.refresh()

            #Handle keypresses
            self.handleKeyPress()

            if self._aborted:
                break
    
    def setInputMode(self, inputMode):
        self._textEditor.setInputMode(inputMode)
        self._bar.setInputMode(inputMode);

        if inputMode == "Command":
            self._bar.setStatusMessage(":");

        elif inputMode == "Normal":
            self._bar.setStatusMessage("");

        self.redrawWindow()

    def handleKeyPress(self):
            #Get char from input
            c = self._stdscr.getch()
            
            #Pressing - allows the user to go to a different mode
            if c == ord('-'):
                self.setInputMode("Normal")
            
            if self._textEditor.getInputMode() == "Command":
                #self._stdscr.getstr(self._bar.getPosition() + 1, 1)
                cmd = self.getStringInput(1, self._bar.getPosition() + 1)

                #TODO: interpret the command
                #Change mode
                self.setInputMode("Normal")
            elif self._textEditor.getInputMode() == "Normal":
                if c == ord('q') or c == ord('Q'):
                    self._aborted = True
                elif c == ord('i'):
                    self.setInputMode("Insert")
                elif c == ord('r'):
                    self.setInputMode("Replace")
                elif c == ord(':'):
                    self.setInputMode("Command")

            elif self._textEditor.getInputMode() == "Insert":
                #Handle keybinding when in insert mode
                empty = None
            elif self._textEditor.getInputMode() == "Replace":
                #Handle keybinding when in replace mode 
                empty = None

    def getStringInput(self, x, y):
        curses.echo()
        cmd = str(self._stdscr.getstr(y, x))
        curses.noecho()
        return cmd

