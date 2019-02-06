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
        curses.raw()
        self._stdscr.keypad(1)
        curses.noecho()

        #Create the window
        self._win = curses.newwin(
            self._window_height - self._window_padding * 2,
            self._window_width - self._window_padding * 2,
            self._window_padding,
            self._window_padding
        )
        
        #Resize the window and draw the screen.
        self.resizeWindow()
    
    def cursesStop(self):
        #Stop curses
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()
    
    #Start the program
    def cursesLoop(self, stdscr):

        #Draw screen
        self._textEditor.draw()
        self.draw()

        #Loop
        while 1:
            #TODO: Resize if needed
            #resize = curses.is_term_resized(self._window_width, self._window_height)
            #if resize == True:
                #self.resizeWindow()

            #Handle keypresses
            self._inputHandler.handleKeyPress()

            #Refresh the window 
            self.draw()

            if self._aborted:
                break
            
    def draw(self):
        #Get the cursor to render the bar
        cursor = self._textEditor.getCursor()

        #Render the bar
        self._bar.setLineNumber(cursor.getBufferY())
        self._bar.setProcentY(cursor.getProcentY())
        self._bar.draw()

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
            self._bar.setPosition(self._window_height - 1, self._window_height)

            #Update the editor height
            self._textEditor.setPosition(0, self._bar.getStartY())

            #self._win.clear()
            #self.draw()
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

    def getHeight(self):
        return self._window_height

    def getWidth(self):
        return self._window_width

    def exit(self):
        self._aborted = True

