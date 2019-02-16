from application import *
from statusbar import *
from texteditor import *
from window import *

class CommandInterpreter:

    def __init__(self, application, statusBar, textEditor, window):
        self._application = application
        self._statusBar = statusBar 
        self._textEditor = textEditor
        self._window = window;

    def interpret(self, command):
        if command == "q":
            self._application.stop()
        elif command == "w":
            self._statusBar.setStatusMessage(self._textEditor.saveBuffer())
            self._statusBar.draw()
        elif command == "wq":
            self._textEditor.saveBuffer()
            self._application.stop()
