from window import * 
from texteditor import *
from statusbar import * 
from inputhandler import *

class Application:
    def __init__(self, filepath):
        #Create a window object
        self._window = Window(self)

        #Create textEditor
        self._textEditor = TextEditor(self._window)
        self._textEditor.openFile(filepath)

        #Create bar
        self._statusBar = StatusBar(self._window, self._textEditor)

        #Create inputhandler
        self._inputHandler = InputHandler(self._textEditor, self._statusBar, self._window)
        self._statusBar.setInputHandler(self._inputHandler)

        #Position the objects
        self._textEditor.setPosition(0, self._window.getHeight() - 3)
        self._statusBar.setPosition(self._window.getHeight() - 2, self._window.getHeight())

        #Start curses
        self._window.start()

    def stop(self):
        #Stop curses
        self._window.stop()

    def run(self, stdscr):
        self.draw()
        while True:
            #Handle keyboard
            self._inputHandler.handleKeyPress()

            #Draw application
            self.draw()

            if self._window.isRunning() == False:
                break
    
    def resizeObjects(self):
        #Change the position/size of the objects
        self._textEditor.setPosition(0, self._window.getHeight() - 2)
        self._statusBar.setPosition(self._window.getHeight() - 2, self._window.getHeight())
    
    def draw(self):
        #Check if the objects need to be resized
        self.resizeObjects()

        #Draw the objects
        self._textEditor.draw()
        self._statusBar.draw()
        self._textEditor.getCursor().draw()

        #Draw everything on screen
        self._window.draw()
