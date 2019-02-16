from application import *
from statusbar import *
from texteditor import *
from window import *

class CommandInterpreter:

    def __init__(self, statusBar, textEditor, window):
        self._statusBar = statusBar 
        self._textEditor = textEditor
        self._window = window;

    def interpret(self, command):
        arguments = command.split(" ") 
        command = arguments[0]
        del arguments[0]

        if command == "q":
            self._window.exit()
        elif command == "w":
            if len(arguments) > 0:
                filepath = arguments[0]
            else:
                filepath = self._textEditor.getBuffer().getFilePath()

            self._statusBar.setStatusMessage(self._textEditor.getBuffer().saveToFile(filepath))

        elif command == "wq":
            self._textEditor.saveBuffer()
            self._window.exit()
