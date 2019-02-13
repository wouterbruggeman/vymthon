from abc import ABC, abstractmethod

class ScreenElement(ABC):

    def __init__(self, window):
        self._window = window
        self._startY = 0
        self._endY = 0
    
    def setPosition(self, startY, endY):
        self._startY = startY
        self._endY = endY
    
    def getStartY(self):
        return self._startY

    def getEndY(self):
        return self._endY
    
    def emptyArea(self):
        for y in range(self._startY, self._endY):
            self._window.clearLine(y)
    
    @abstractmethod
    def draw(self):
        pass
