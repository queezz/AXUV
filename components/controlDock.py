import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from pyqtgraph import QtCore
from pyqtgraph.dockarea import Dock

class ControlDock(Dock):

    def __init__(self):
        super().__init__("Controls")
        self.widget = pg.LayoutWidget()

        self.testBtn = QtGui.QPushButton("test")
        
        self.valueBw = QtGui.QTextBrowser()
        self.valueBw.setMaximumHeight(90)
        self.valueBw.setMinimumWidth(100)
        self.valueBw.setCurrentFont(QtGui.QFont("Courier New"))
        self.__setLayout()

    def __setLayout(self):
        self.addWidget(self.widget)
        
        self.widget.addWidget(self.testBtn, 0, 0)
        self.widget.addWidget(self.valueBw, 1, 0,1,2)
        
        self.verticalSpacer = QtGui.QSpacerItem(
            0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.widget.layout.setVerticalSpacing(5)
        self.widget.layout.addItem(self.verticalSpacer)

if __name__ == "__main__":
    pass
