from window import * 
from texteditor import *
from statusbar import * 
from inputhandler import *

class Application:
    def __init__(self):
        self._isRunning = True

        #Create a window object and start curses
        self._window = Window()
        self._window.start()

        #Create textEditor
        self._textEditor = TextEditor(self._window)

        #Create bar
        self._statusBar = StatusBar(self._window, self._textEditor)

        #Create inputhandler
        self._inputHandler = InputHandler(self._textEditor, self._statusBar, self._window)
        self._statusBar.setInputHandler(self._inputHandler)

        #Position the objects
        self._textEditor.setPosition(0, self._window.getHeight() - 3)
        self._statusBar.setPosition(self._window.getHeight() - 2, self._window.getHeight())

    def openFile(self, filePath):
        self._textEditor.openFile(filePath)

    def stop(self):
        self._isRunning = False

        #Stop curses
        self._window.stop()

    def loop(self):
        #Handle keyboard
        self._inputHandler.handleKeyPress()

        #Draw application
        self.draw()

        #Stop the application after one loop for testing purposes
        #c = self._window.getChar()
        #self.stop()

    def draw(self):
        self._textEditor.draw()
        self._statusBar.draw()
        self._window._win.refresh()

    def isRunning(self):
        return self._isRunning
