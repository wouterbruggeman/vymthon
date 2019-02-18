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
            self.commandSave(arguments)
        elif command == "wq":
            self.commandSave(arguments)
            self._window.exit()
        elif command == "e":
            self.commandOpen(arguments)

    def commandSave(self, arguments):
        if len(arguments) > 0:
            filepath = arguments[0]
        else:
            filepath = self._textEditor.getBuffer().getFilePath()

        #Save the file
        self._statusBar.setStatusMessage(self._textEditor.getBuffer().saveToFile(filepath))
        
        #Switch to the file
        self._textEditor.openFile(filepath)

    def commandOpen(self, arguments):
        if len(arguments) > 0:
            self._textEditor.openFile(arguments[0])
        else:
            self._statusBar.setStatusMessage("Cannot open file: No filepath given.")


