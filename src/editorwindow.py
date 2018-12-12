import curses
from buffer import *
from bar import *
from texteditor import *

class EditorWindow:
    _inputMode = "Normal"
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
        self._bar.setInputMode(self._inputMode)
    
        #Create text editor
        self._textEditor = TextEditor(filepath)


        #Setup curses stuff
        self.cursesStart()
        curses.wrapper(self.cursesLoop)
        self.cursesStop()
    
    def cursesStart(self):
        self._stdscr = curses.initscr()
        self._stdscr.keypad(1)
        curses.noecho()
        curses.cbreak()
        self.resizeWindow()
        self._win = curses.newwin(
            self._window_height - self._window_padding * 2,
            self._window_width - self._window_padding * 2,
            self._window_padding,
            self._window_padding
        )
    
    def resizeWindow(self):
        self._window_height, self._window_width = self._stdscr.getmaxyx()
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
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def setText(self, x, y, label):
        try:
            self._win.addstr(y, x, label)
        except:
            pass

    def moveCursor(self, x, y):
            self._win.move(y,x) 
            curses.setsyx(y,x)

    def redrawWindow(self):
        self._win.refresh()

        #Render the editor
        yCounter = 0
        for line in self._textEditor.getContent():
            self.setText(0, yCounter, line)
            yCounter += 1

        #Show bottom text
        self._bar.setFilename(self._textEditor.getCurrentFilename())
        self.setText(0, self._window_height - 2,
                self._bar.getContent())
        
        if self._inputMode == "Command":
            self.moveCursor(0,self._window_height - 1)
            self.setText(0,self._window_height - 1, "")
        else:
            self.moveCursor(9,0)

    def cursesLoop(self, stdscr):
        while 1:
            #Resize if needed
            resize = curses.is_term_resized(self._window_width, self._window_height)
            if resize == True:
                self.resizeWindow()
               
            #Redraw after everything
            self.redrawWindow()

            #Handle keypresses
            self.handleKeyPress()

            if self._aborted:
                break
    
    def setInputMode(self, inputMode):
        self._inputMode = inputMode
        self._textEditor.setInputMode(inputMode)
        self._bar.setInputMode(inputMode);

    def handleKeyPress(self):
            #Get char from input
            c = self._stdscr.getch()
            
            #Pressing - allows the user to go to a different mode
            if c == ord('-'):
                self.setInputMode("Normal")
            
            if self._inputMode == "Command":
                curses.echo()
                self._stdscr.getstr()
                curses.noecho()

            if self._inputMode == "Normal":
                if c == ord('q') or c == ord('Q'):
                    self._aborted = True
                elif c == ord('i'):
                    self.setInputMode("Insert")
                elif c == ord('r'):
                    self.setInputMode("Replace")
                elif c == ord(':'):
                    self.setInputMode("Command")

            elif self._inputMode == "Insert":
                #Handle keybinding when in insert mode
                empty = None
            elif self._inputMode == "Replace":
                #Handle keybinding when in replace mode 
                empty = None
