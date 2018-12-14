from editorwindow import *
from texteditor import *
from bar import *

class CommandInterpreter:
    _textEditor = TextEditor
    _bar = Bar
    _window = None

    def __init__(self, bar, textEditor, window):
        self._bar = bar
        self._textEditor = textEditor
        self._window = window;

    def interpret(self, command):
        if command == "q":
            self._window.exit()
        elif command == "w":
            self._bar.setStatusMessage(self._textEditor.saveBuffer())
        elif command == "wq":
            self._textEditor.saveBuffer()
            self._window.cursesStop();
