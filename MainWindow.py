# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:40:07 2020

@author: pc
"""

from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLabel,QToolTip,QDesktopWidget,QMainWindow,QStatusBar,QHBoxLayout,QVBoxLayout,QColorDialog
import sys
from PySide2.QtGui import QIcon,QPixmap,QFont,QGuiApplication,Qt,QColor
import matplotlib.colors as myColor
import main

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Queues\'Project')
        self.setGeometry(150,150,800,500)
        self.setFixedSize(800,500)            

        self.setIcon()
        self.center()

        self.createLayout()

        self.backGroundcolorChanger()
        



    def backGroundcolorChanger(self):
        icon1=QIcon('colors.png')
        label1=QLabel('ColorPalette',self)
        pixmap1=icon1.pixmap(30,30,QIcon.Active,QIcon.On)
        label1.setPixmap(pixmap1)
        label1.setToolTip('go to Previous Screen')
        label1.mousePressEvent=self.getBackgroundColor

        self.namesLabel=QLabel('Designed by:\n\tAbd-ElRahman Abd-ElFattah Habib.\n\tMohammed Ahmed Mekkawy.\n\tElSayed Abd-ElMohaymen ElSayed.\n',self)
        self.namesLabel.width=300
        width=self.width()
        height=self.height()

        label1.move(width-40,height-40)
        self.namesLabel.move(10,height-60)
        self.namesLabel.adjustSize()

    def getBackgroundColor(self,event):
        color = QColorDialog.getColor()
        self.setStyleSheet('background-color:%s'%color.name())
        self.namesLabel.setStyleSheet('color:white')
       
        


    def createLayout(self):

        icon1=QIcon('line.png')
        label1=QLabel('Sample',self)
        pixmap1=icon1.pixmap(200,200,QIcon.Active,QIcon.On)
        label1.setPixmap(pixmap1)

        self.submitButton=QPushButton('Continue',self)
        self.submitButton.setFont(QFont('Sanserif',18))
        self.submitButton.setStyleSheet('background-color: blueviolet;color:white;border: 1px solid; border-radius:15px')
        self.submitButton.clicked.connect(self.handleSubmitClick)

        vbox=QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)
        vbox.setContentsMargins(10,30,10,30)

        vbox.addWidget(label1)
        vbox.setSpacing(50)
        vbox.addWidget(self.submitButton)

        self.setLayout(vbox)


    def handleSubmitClick(self):
        self.main = main.MainWindow()
        self.main.show()
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
        elif userInfo == QMessageBox.No:
            event.ignore()           
        




        
     
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_()) 
     

'''

             end of main WINDOW 


'''


