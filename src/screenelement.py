from abc import ABC, abstractmethod

class ScreenElement(ABC):
    _window = None
    _startY = 0
    _endY = 0

    def __init__(self, window):
        self._window = window
    
    def setPosition(self, startY, endY):
        self._startY = startY
        self._endY = endY
    
    def getStartY(self):
        return self._startY

    def getEndY(self):
        return self._endY
    
    def emptyArea(self):
        for y in range(self._startY, self._endY):
            for x in range(self._window.getWidth()):
                #Fill the area with spaces
                self._window.addText(x, y, " ")
    
    @abstractmethod
    def draw(self):
        pass
