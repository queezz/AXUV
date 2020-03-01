import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from pyqtgraph.dockarea import DockArea, Dock

from components.controlDock import ControlDock
from components.graph import Graph
from components.imageplot import Contour

class UIWindow(object):

    def __init__(self):
        super().__init__()
        pg.setConfigOptions(imageAxisOrder='row-major')

        self.MainWindow = QtGui.QMainWindow()
        self.tabwidg = QtGui.QTabWidget()
        self.area = DockArea()
        self.plotDock = Dock("Plots", size=(400, 400))
        self.surfaceDock = Dock("Contour", size=(250, 400))
        self.controlDock = ControlDock()
        self.controlDock.setStretch(*(10,100))
        self.graph = Graph()        
        self.contour = Contour()
        
        self.MainWindow.setGeometry(20, 50, 1200, 600)
        self.MainWindow.setObjectName("Monitor")
        self.MainWindow.setWindowTitle("AXUV tool")
        self.MainWindow.statusBar().showMessage('')
        self.MainWindow.setAcceptDrops(True)
        self.__setLayout()

    def __setLayout(self):
        self.MainWindow.setCentralWidget(self.tabwidg)
        self.tabwidg.addTab(self.area, "Data")
        
        self.area.addDock(self.plotDock, "right")
        self.area.addDock(self.controlDock,"left")
        self.area.addDock(self.surfaceDock,"bottom",self.controlDock)
        
        self.plotDock.addWidget(self.graph)
        self.surfaceDock.addWidget(self.contour)

    def showMain(self):
        self.MainWindow.show()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = UIWindow()
    ui.showMain()
    sys.exit(app.exec_())
