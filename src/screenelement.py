from mainwindow import *

class ScreenElement:
    _window = None
    _content = []
    _startY = 0
    _endY = 0

    def __init__(self, window):
        self._window = window
    
    def setPosition(self, startY, endY):
        self._startY = startY
        self._endY = endY
    
    def getStartY(self):
        return self._startY - 1

    def getEndY(self):
        return self._endY

    def draw(self):
        return
