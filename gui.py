import sys
import PyQt5.QtWidgets as qw
import time
import requests
from PyQt5.QtCore import pyqtSlot

class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 500)
        self.move(300, 300)
        self.setWindowTitle('Sync')

        self.go1Btn = qw.QPushButton('I', self)
        self.go1Btn.move(50, 50)
        self.go1Btn.clicked.connect(self.firstOperation)

        self.goBtn = qw.QPushButton('II', self)
        self.goBtn.move(50, 70)
        self.goBtn.clicked.connect(self.secondOperation)

        self.goBtn = qw.QPushButton('III', self)
        self.goBtn.move(50, 90)
        self.goBtn.clicked.connect(self.thirdOperation)

        self.goBtn = qw.QPushButton('IV', self)
        self.goBtn.move(50, 110)
        self.goBtn.clicked.connect(self.fourthOperation)

        self.goBtn = qw.QPushButton('V', self)
        self.goBtn.move(50, 130)
        self.goBtn.clicked.connect(self.fifthOperation)

        self.goBtn = qw.QPushButton('VI', self)
        self.goBtn.move(50, 150)
        self.goBtn.clicked.connect(self.sixthOperation)

        self.goBtn = qw.QPushButton('VII', self)
        self.goBtn.move(50, 170)
        self.goBtn.clicked.connect(self.seventhOperation)

        self.goBtn = qw.QPushButton('VIII', self)
        self.goBtn.move(50, 190)
        self.goBtn.clicked.connect(self.eighthOperation)

        self.goBtn = qw.QPushButton('IX', self)
        self.goBtn.move(50, 210)
        self.goBtn.clicked.connect(self.ninethOperation)

        self.goBtn = qw.QPushButton('X', self)
        self.goBtn.move(50, 230)
        self.goBtn.clicked.connect(self.tenthOperation)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(90, 300)
        self.quitBtn.clicked.connect(self.close)
        
    @pyqtSlot(bool)
    def firstOperation(self, evt):
        print('''Ten little nigger boys went out to dine
One choked his little self, and then there were nine.
''')
    @pyqtSlot(bool)
    def secondOperation(self, evt):
        print('''Nine little nigger boys sat up very late;
One overslept himself, and then there were eight. 
''')
    @pyqtSlot(bool)
    def thirdOperation(self, evt):
        print('''Eight little nigger boys travelling in Devon;
One said he'd stay there, and then there were seven.
''')
    @pyqtSlot(bool)
    def fourthOperation(self, evt):
        print('''Seven little nigger boys chopping up sticks;
One chopped himself in half, and then there were six. 
''')
    @pyqtSlot(bool)
    def fifthOperation(self, evt):
        print('''Six little nigger boys playing with a hive;
A bumble-bee stung one, and then there were five. 
''')
    @pyqtSlot(bool)
    def sixthOperation(self, evt):
        print('''Five little nigger boys going in for law;
One got in chancery, and then there were four. 
''')
    @pyqtSlot(bool)
    def seventhOperation(self, evt):
        print('''Four little nigger boys going out to sea;
A red herring swallowed one, and then there were three. 
''')
    @pyqtSlot(bool)
    def eighthOperation(self, evt):
        print('''Three little nigger boys walking in the Zoo;
A big bear hugged one, and then there were two. 
''')
    @pyqtSlot(bool)
    def ninethOperation(self, evt):
        print('''Two little nigger boys sitting in the sun;
One got frizzled up, and then there was one. 
''')
    @pyqtSlot(bool)
    def tenthOperation(self, evt):
        print('''One little nigger boy left all alone;
He went out and hanged himself and then there were None.
''')

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
