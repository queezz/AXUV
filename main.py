import sys, datetime, os
import numpy as np
import pandas as pd
from pyqtgraph.Qt import QtCore, QtGui

from UI import UIWindow
from readsettings import make_datafolders, get_datafolderpth


# must inherit QtCore.QObject in order to use 'connect'
class MainWidget(QtCore.QObject, UIWindow):
    DEFAULT_TEMPERATURE = 0

    sigAbortWorkers = QtCore.pyqtSignal()

    def __init__(self, app: QtGui.QApplication):
        super(self.__class__, self).__init__()
        self.__app = app
        self.connections()
        self.initplots()
        self.showMain()

    def connections(self):
        """ UI connections """
        self.controlDock.testBtn.clicked.connect(self.test)
    
    def initplots(self):
        """ Initizlize plot curves
        plot1, 2, 3 - the box in Graphix layout, the axis.
        curve1, 2, 3 - data curves in the axes.
        """
        self.colors = {
            'Ip':"#8d3de3",
            'P1':"#6ac600",
            'P2':"#c9004d",
            'T':"#5999ff",
        }
        self.curve1 = self.graph.plot1.plot(pen=self.colors['Ip'])
        self.curve2 = self.graph.plot2.plot(pen=self.colors['T'])
        self.curve3 = self.graph.plot3.plot(pen=self.colors['P1'])
        self.curve4 = self.graph.plot3.plot(pen=self.colors['P2'])
        self.allcurves = [self.curve1,self.curve2,self.curve3,self.curve4]
        self.allplots = [self.graph.plot1, self.graph.plot2,self.graph.plot3]
        # link X axis
        self.graph.plot1.setXLink(self.graph.plot3)
        self.graph.plot2.setXLink(self.graph.plot3)
    
    def test(self):
        """ test function """
        x = np.linspace(0,2*np.pi)
        y = np.sin(x*np.random.normal(2,0.02))
        #self.curve1.setData(x,y)
        [i.setData(x,y + np.random.normal(1,0.1)) for i in self.allcurves]
        [i.autoRange() for i in self.allplots]
        #self.graph.plot1.enableAutoRange(True) # update scale on data change
        #self.graph.plot1.autoRange()
        self.controlDock.valueBw.setText(
            f"""
           <font size=5 color={self.colors['P1']}>
                mean(y) = {y.mean():.1e}
              </font>
            """
        )
        
        
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
