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
        self.testBtn.setToolTip('Load test data')
        self.shotSb = QtGui.QSpinBox(suffix=' shot')
        self.shotSb.setToolTip('Shot number')
        self.shotSb.setMaximum(99999)
        self.shotSb.setValue(40416)
        self.tminSb = QtGui.QDoubleSpinBox(suffix=' s')
        self.tminSb.setToolTip('set t min')
        self.tminSb.setValue(0)
        self.tmaxSb = QtGui.QDoubleSpinBox(suffix=' s')
        self.tmaxSb.setToolTip('set t max')
        self.tmaxSb.setValue(4.00)
        self.savefigBtn = QtGui.QPushButton("save fig")
        
        self.valueBw = QtGui.QTextBrowser()
        self.valueBw.setMaximumHeight(90)
        self.valueBw.setMinimumWidth(100)
        self.valueBw.setCurrentFont(QtGui.QFont("Courier New"))
        self.__setLayout()

    def __setLayout(self):
        self.addWidget(self.widget)
        
        self.widget.addWidget(self.shotSb, 0, 0)
        self.widget.addWidget(self.testBtn, 0, 1)
        self.widget.addWidget(self.tminSb, 1, 0)
        self.widget.addWidget(self.tmaxSb, 1, 1)
        self.widget.addWidget(self.savefigBtn, 0, 2)
        self.widget.addWidget(self.valueBw, 3, 0,1,3)
        
        self.verticalSpacer = QtGui.QSpacerItem(
            0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.widget.layout.setVerticalSpacing(5)
        self.widget.layout.addItem(self.verticalSpacer)

if __name__ == "__main__":
    pass
