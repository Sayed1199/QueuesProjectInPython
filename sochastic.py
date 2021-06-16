from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLabel,QToolTip,QDesktopWidget,QMainWindow,QStatusBar,QHBoxLayout,QVBoxLayout,QColorDialog
import sys
from PySide2.QtGui import QIcon,QPixmap,QFont,QGuiApplication,Qt,QColor
import matplotlib.colors as myColor
import MainWindow
from PySide2.QtWidgets import QRadioButton,QTextEdit
import main
import deterministic_graph
import QueueOperations 
import re
class SochasticScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sochastic Queue')
        self.setGeometry(150,150,1000,600)
        self.setFixedSize(1000,600)

        self.center()
        self.setIcon()

        self.initUi()

        self.createBackArrow()

        self.initUi()




    def showDeterministicGraph(self):
        self.dete_graph=deterministic_graph.DeterministicGraphScreen()
        self.dete_graph.show()


    def handleSubmit(self):
        st1=self.lambdaQEditText.toPlainText() + " " + self.meoQEditText.toPlainText() + " " + self.capacityQEditText.toPlainText()+" "+self.alreadyPresentpeopleQEditText.toPlainText()
        lam2=0
        meo2=0
        n=0
        
        if re.match(r"[0-9]+/[0-9]+\b",self.lambdaQEditText.toPlainText()):
            print("gggg")
            ar2=re.split("/",self.lambdaQEditText.toPlainText())
            lam2=int(ar2[0])/float(ar2[1])
            if int(ar2[1])!=0:
                n+=1
            st1=self.meoQEditText.toPlainText() + " " + self.capacityQEditText.toPlainText() + " " +self.alreadyPresentpeopleQEditText.toPlainText()

        if re.match(r"[0-9]+/[0-9]+\b",self.meoQEditText.toPlainText()):
            print("yyyy")
            ar2=re.split("/",self.meoQEditText.toPlainText())
            meo2=int(ar2[0])/float(ar2[1])
            if int(ar2[0])!=0 or int(ar2[1])!=0:
                n+=1
            if n!=1:
                st1=self.capacityQEditText.toPlainText() + " " +self.alreadyPresentpeopleQEditText.toPlainText()
            else:
                st1=self.lambdaQEditText.toPlainText() + " " + self.capacityQEditText.toPlainText() +" " +self.alreadyPresentpeopleQEditText.toPlainText()
        
        ar1=re.search(r"[^\d\s.//]",st1)
        ar=re.findall(r"([0-9]+\.[0-9]+)|(\.[0-9]+)|([0-9]+)",st1)

        
        if(len(ar)+n==4 and ar1==None):
            if lam2==0:
                lam2=float(self.lambdaQEditText.toPlainText())

            if meo2==0:
                meo2=float(self.meoQEditText.toPlainText())

            soch=QueueOperations.sochasitc(lam2,meo2,
            int(self.alreadyPresentpeopleQEditText.toPlainText()),int(self.capacityQEditText.toPlainText()))
            
            st="L: "+str("{:.2f}".format(soch.L()))+", Lq: "+str("{:.2f}".format(soch.Lq()))+", W: "+str("{:.2f}".format(soch.W()))+", Wq:"+str("{:.2f}".format(soch.Wq()))

            self.resultLabel.setText(st)
            
            
            self.resultLabel.setVisible(True)
        else:
            self.resultLabel.setGeometry((self.width()/2)-60,500,200,100)
            self.resultLabel.setText("Invalid Input")
            self.resultLabel.setVisible(True)

    def initUi(self):
        
        self.lambdaLabel=QLabel('λ : ',self)
        self.lambdaLabel.setFont(QFont('Sanserif',16))
        self.lambdaLabel.move(100,100)
        self.lambdaLabel.adjustSize()
        
        self.lambdaQEditText=QTextEdit(self)
        self.lambdaQEditText.setGeometry(140,90,200,50)
        self.lambdaQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.lambdaQEditText.setFont(QFont('Sanserif',13))
        self.lambdaQEditText.setAlignment(Qt.AlignCenter)
        self.lambdaQEditText.setPlaceholderText('arrival rate..')
        self.lambdaQEditText.setTextColor(QColor(255, 0, 0))
        
        

        
        self.meoLabel=QLabel('μ : ',self)
        self.meoLabel.setFont(QFont('Sanserif',16))
        self.meoLabel.move(600,100)
        self.meoLabel.adjustSize()
        
        self.meoQEditText=QTextEdit(self)
        self.meoQEditText.setGeometry(640,90,200,50)
        self.meoQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.meoQEditText.setFont(QFont('Sanserif',13))
        self.meoQEditText.setAlignment(Qt.AlignCenter)
        self.meoQEditText.setPlaceholderText('service rate..')
        self.meoQEditText.setTextColor(QColor(0, 0, 255))



        #self.nServersLabel=QLabel('n : ',self)
        #self.nServersLabel.setFont(QFont('Sanserif',16))
        #self.nServersLabel.move(350,200)
        #self.nServersLabel.adjustSize()
        
        # self.nServersQEditText=QTextEdit(self)
        # self.nServersQEditText.setGeometry(380,190,200,50)
        # self.nServersQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        # self.nServersQEditText.setFont(QFont('Sanserif',13))
        # self.nServersQEditText.setAlignment(Qt.AlignCenter)
        # self.nServersQEditText.setPlaceholderText('enter the servers number..')
        # self.nServersQEditText.setTextColor(QColor(0, 255, 0))



        self.capacityLabel=QLabel('k :  ',self)
        self.capacityLabel.setFont(QFont('Sanserif',16))
        self.capacityLabel.move(600,300)
        self.capacityLabel.adjustSize()
        
        self.capacityQEditText=QTextEdit(self)
        self.capacityQEditText.setGeometry(640,290,200,50)
        self.capacityQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.capacityQEditText.setFont(QFont('Sanserif',13))
        self.capacityQEditText.setAlignment(Qt.AlignCenter)
        self.capacityQEditText.setPlaceholderText('Capacity..')
        self.capacityQEditText.setTextColor(QColor(0, 0, 255))

        
        self.alreadyPresentpeopleLabel=QLabel('c : ',self)
        self.alreadyPresentpeopleLabel.setFont(QFont('Sanserif',16))
        self.alreadyPresentpeopleLabel.move(100,300)
        self.alreadyPresentpeopleLabel.adjustSize()
        
        self.alreadyPresentpeopleQEditText=QTextEdit(self)
        self.alreadyPresentpeopleQEditText.setGeometry(140,290,200,50)
        self.alreadyPresentpeopleQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.alreadyPresentpeopleQEditText.setFont(QFont('Sanserif',13))
        self.alreadyPresentpeopleQEditText.setAlignment(Qt.AlignCenter)
        self.alreadyPresentpeopleQEditText.setPlaceholderText('servers..')
        self.alreadyPresentpeopleQEditText.setTextColor(QColor(0, 255, 0))


        self.submitButton = QPushButton('Submit',self)
        self.submitButton.setFont(QFont('Sanserif',14))
        self.submitButton.setStyleSheet('color:white;background-color:firebrick;border: 0px solid; border-radius:15px')
        self.submitButton.move((self.width()/2)-50,460)
        self.submitButton.clicked.connect(self.handleSubmit)
        

        #out Label................

        self.resultLabel = QLabel('.......................................................................',self)
        self.resultLabel.setFont(QFont('Sanserif',14))
        self.resultLabel.setStyleSheet('color:magenta')
        self.resultLabel.adjustSize()
        self.resultLabel.setVisible(False)
        self.resultLabel.setGeometry((self.width()/2)-180,470,400,90)
        
        










    

    def createBackArrow(self):
        icon1=QIcon('arrow_back.png')
        label1=QLabel('Sample',self)
        pixmap1=icon1.pixmap(20,20,QIcon.Active,QIcon.On)
        label1.setPixmap(pixmap1)
        label1.move(25,25)
        label1.adjustSize()
        label1.mousePressEvent=self.arrowbackClicked

    def arrowbackClicked(self,event):
        print('arrow back clicked')
        self.main=main.MainWindow()
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
            self.close()
            #sys.exit(QApplication(sys.argv).exec_())                   
            
        elif userInfo == QMessageBox.No:
            event.ignore()       
    
