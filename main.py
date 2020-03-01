import sys, datetime, os
import numpy as np
import pandas as pd
from pyqtgraph.Qt import QtCore, QtGui

from UI import UIWindow
from readsettings import make_datafolders, get_datafolderpth

from load_rawdata import get_some_file, read_axuv_raw

# must inherit QtCore.QObject in order to use 'connect'
class MainWidget(QtCore.QObject, UIWindow):
    DEFAULT_TEMPERATURE = 0

    sigAbortWorkers = QtCore.pyqtSignal()

    def __init__(self, app: QtGui.QApplication):
        super(self.__class__, self).__init__()
        self.__app = app
        self.connections()
        self.showMain()

    def connections(self):
        """ UI connections """
        self.controlDock.testBtn.clicked.connect(self.test)
    
    def test(self):
        """ test function """
        data = read_axuv_raw(get_some_file(basedir='../data'))
        [c.setData(data['time'],data[ch]) for c,ch in zip(self.graph.curves,data.keys()[1:])]
        x = np.arange(1,17)
        y = data['time'].values
        z = data.iloc[:,1:].values.T
        self.contour.image.setImage(z)
        self.contour.image.scale(1/50000,1)
        self.controlDock.tminSb.valueChanged.connect(self.rescale)
        self.controlDock.tmaxSb.valueChanged.connect(self.rescale)

    def rescale(self):
        """ Rescale 1D plots """
        tmin = self.controlDock.tminSb.value()
        tmax = self.controlDock.tmaxSb.value()
        [p.setXRange(tmin,tmax,0) for p in self.graph.plots]
        self.contour.plot.setXRange(tmin,tmax,0)
        
    def __quit(self):
        """ terminate app """
        self.__app.quit()   

    def fulltonormal(self):
       """ Change from full screen to normal view on click"""
       if self.controlDock.FullNormSW.isChecked():
           self.MainWindow.showFullScreen()
           self.controlDock.setStretch(*(10,300)) # minimize control dock width
       else:
           self.MainWindow.showNormal()
           self.controlDock.setStretch(*(10,300)) # minimize control dock width

if __name__ == "__main__":
    app = QtGui.QApplication([])
    widget = MainWidget(app)

    sys.exit(app.exec_())
