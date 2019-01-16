from mainwindow import *
from abc import ABC, abstractmethod

class ScreenElement(ABC):
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
    
    def emptyArea(self):
        for y in range(self._window.getHeight()):
            for x in range(self._window.getWidth()):
                self._window.addText(x, y, " ")
    
    @abstractmethod
    def draw(self):
        pass
