import curses
from bar import *
from texteditor import *
from inputhandler import *

class MainWindow:
    _bar = Bar
    _textEditor = TextEditor
    _inputHandler = InputHandler

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

        #Create input handler
        self._inputHandler = InputHandler(self._bar, self._textEditor, self)

        #Start curses
        self.cursesStart()

        #Setup other objects
        self._bar.setFilename(self._textEditor.getCurrentFilename())

        #Define colors
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
        #Loop curses
        curses.wrapper(self.cursesLoop)
        self.cursesStop()
    
    def cursesStart(self):
        #Init curses
        self._stdscr = curses.initscr()

        #Curses settings
        curses.start_color()
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

        #Give the text editor some space
        self._textEditor.setSize(0, self._bar.getPosition())
    
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
            self._inputHandler.handleKeyPress();

            if self._aborted:
                break
            
    def redrawWindow(self):
        #Render the editor
        self._textEditor.draw()

        #Render the bar
        self._bar.draw()
        cursor = self._textEditor.getCursor()
        self._bar.setLineNumber(cursor.getBufferY())

        #TODO: is a refresh really needed?
        self._win.refresh()
    
    def resizeWindow(self):
        self._window_height, self._window_width = self._stdscr.getmaxyx()

        #If the window was not initialized
        if self._win != False:
            self.entry_height = self._window_height - self._window_padding * 2
            self._win.resize(
                self._window_height - self._window_padding * 2,
                self._window_width - self._window_padding * 2,
            )
            #Update the bar size
            self._bar.setPosition(self._window_height - 2)
            #Update the editor height
            self._textEditor.setSize(0, self._bar.getPosition())

            self._win.clear()
            self.redrawWindow()
            curses.doupdate()
   
    #Print text
    def addText(self, x, y, label, color = 1):
        try:
            #Set some text at the given position
            self._win.addstr(y, x, label, curses.color_pair(color))
        except:
            pass
    
    def moveCursor(self, x, y):
            self._win.move(y,x) 
            self._win.refresh()
            #curses.setsyx(y,x)

    def exit(self):
        self._aborted = True

