import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

DEGREE_SMB = u'\N{DEGREE SIGN}'

class Graph(pg.GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("graph")

        labelStyle = {'color': '#FFF', 'font-size': '14pt'}
        font = QtGui.QFont('serif',14)

        #self.plot1 = self.addPlot(row=0, col=0)
        # TODO: 単位
        #self.plot1.setLabel('left', "Ip", units='A',**labelStyle)
        #self.plot1.getAxis('left').setWidth(100)
        #self.plot1.getAxis('left').tickFont = font
        self.plots = [self.addPlot(row=i%8,col=i//8) for i in range(16)]
        #self.curve1 = self.graph.plot1.plot(pen=self.colors['Ip'])
        
        self.curves = [p.plot() for p in self.plots]
        [p.hideAxis('bottom') for i,p in enumerate(self.plots) if (i+1)%8]

        #self.graph.plot1.setXLink(self.graph.plot3)

if __name__ == '__main__':
    pass
