import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

DEGREE_SMB = u'\N{DEGREE SIGN}'

class Contour(pg.GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("Contour")
        self.plot = self.addPlot()
        self.image = pg.ImageItem()
        self.contour = self.plot.addItem(self.image)

        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.image)
        self.addItem(self.hist)

