import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

DEGREE_SMB = u'\N{DEGREE SIGN}'

class Graph(pg.GraphicsLayoutWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("graph")

        labelStyle = {'color': '#FFF', 'font-size': '14pt'}
        font = QtGui.QFont('serif',14)

        self.plot1 = self.addPlot(row=0, col=0)
        # TODO: 単位
        self.plot1.setLabel('left', "Ip", units='A',**labelStyle)
        self.plot1.getAxis('left').setWidth(100)
        self.plot1.getAxis('left').tickFont = font

        self.plot2 = self.addPlot(row=1, col=0)
        self.plot2.setLabel('left', "T", units=DEGREE_SMB+'C',**labelStyle)
        # Adjust the label offset
        self.plot2.getAxis('left').setWidth(100)

        self.plot3 = self.addPlot(row=2, col=0)
        self.plot3.setLabel('left', "P", units='Torr',**labelStyle)
        self.plot3.getAxis('left').setWidth(100)
        self.plot3.setLabel('bottom', "time", units='sec',**labelStyle)
        
        self.setBackground(background='#25272b')
               
        self.plot2.getAxis('left').setPen('#fcfcc7')
        self.plot2.getAxis('left').tickFont = font
        self.plot3.getAxis('bottom').tickFont = font
        self.plot3.getAxis('bottom').setStyle(tickTextOffset = 10)

if __name__ == '__main__':
    pass
