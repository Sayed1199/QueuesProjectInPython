from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLabel,QToolTip,QDesktopWidget,QMainWindow,QStatusBar,QHBoxLayout,QVBoxLayout,QColorDialog
import sys
from PySide2.QtGui import QIcon,QPixmap,QFont,QGuiApplication,Qt,QColor
import matplotlib.colors as myColor
import MainWindow
from PySide2.QtWidgets import QRadioButton
import determenistic
import sochastic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Queues\' Type')
        self.setGeometry(150,150,800,500)
        self.setFixedSize(800,500)

        self.center()
        self.setIcon()

        self.initRadioButtons()

        

    def initRadioButtons(self):

        width=self.width()
        height=self.height()

        self.deterministicRadio=QRadioButton('Deterministic Queue',self)
        self.deterministicRadio.setFont(QFont('Sanserif',18))
        self.deterministicRadio.setStyleSheet('QRadioButton{color:maroon}')
        self.deterministicRadio.adjustSize()
        self.deterministicRadio.move(100,100)
        self.deterministicRadio.clicked.connect(self.deterministicRadioClicked)
       

        self.stochasticRadio=QRadioButton('Stochastic Queue',self)
        self.stochasticRadio.setFont(QFont('Sanserif',18))
        self.stochasticRadio.setStyleSheet('QRadioButton{color:darkslategray}')
        self.stochasticRadio.adjustSize()
        self.stochasticRadio.move((width/2)+50,100)
        self.stochasticRadio.clicked.connect(self.stochasticRadioClicked)

        self.deterministicRadio=QRadioButton('WhatEver Queue',self)
        self.deterministicRadio.setFont(QFont('Sanserif',18))
        self.deterministicRadio.setStyleSheet('QRadioButton{color:steelblue}')
        self.deterministicRadio.adjustSize()
        self.deterministicRadio.move(300,200)

        icon1=QIcon('line.png')
        label1=QLabel('Sample',self)
        pixmap1=icon1.pixmap(100,100,QIcon.Active,QIcon.On)
        label1.setPixmap(pixmap1)
        label1.move((width/2)-50,300)
        label1.adjustSize()




    def deterministicRadioClicked(self):

        print('clickeddddd')
        self.dete=determenistic.DeterministicScreen()
        self.dete.show()
        self.destroy()




    def stochasticRadioClicked(self):
        self.soch=sochastic.SochasticScreen()
        self.soch.show()
        self.destroy()


    def center(self):
        qRect=self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerpoint)
        self.move(qRect.topLeft())


    def setIcon(self):
        appIcon=  QIcon('line.png')
        self.setWindowIcon(appIcon)  

    def closeEvent(self,event):
        userInfo = QMessageBox.question(self,'Closing ?','Do u want to quit ?',QMessageBox.Yes|QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            event.accept()
            self.close()
            #sys.exit(QApplication(sys.argv).exec_())                   
            
        elif userInfo == QMessageBox.No:
            event.ignore()       



   

        
