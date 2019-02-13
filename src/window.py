import curses

class Window:
    _stdscr = None
    _win = None
    _window_padding = 0
    _window_height = 0
    _window_width = 0

    def __init__(self):
        pass 

    def start(self):
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
        self._resizeWindow()

        #Define colors
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def _resizeWindow(self):
        self._window_height, self._window_width = self._stdscr.getmaxyx()

        #If the window was not initialized
        if self._win != False:
            self.entry_height = self._window_height - self._window_padding * 2
            self._win.resize(
                self._window_height - self._window_padding * 2,
                self._window_width - self._window_padding * 2,
            )
            #self.draw()
            curses.doupdate()


    def stop(self):
        #Stop curses
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()
   
    #Print text
    def addText(self, x, y, label, color = 1):
        try:
            #Set some text at the given position
            self._win.addstr(y, x, label, curses.color_pair(color))
        except:
            pass
    
    def getString(self, x, y):
        curses.echo()
        string = self._win.getstr(y, x).decode("utf-8")
        curses.noecho()
        return string

    def clearLine(self, y):
        for x in range(self.getWidth()):
            #Fill the area with spaces
            self.addText(x, y, " ")
    
    def getChar(self):
        return self._win.getch()

    def moveCursor(self, x, y):
            self._win.move(y,x) 
            self._win.refresh()

    def getHeight(self):
        return self._window_height

    def getWidth(self):
        return self._window_width
