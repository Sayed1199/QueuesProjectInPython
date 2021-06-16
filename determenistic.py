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
import matplotlib.pyplot as plt
import numpy as np 
class DeterministicScreen(QMainWindow):
    deter=0
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Deterministic Queue')
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
        global deter
        st1=self.lambdaQEditText.toPlainText() + " " + self.meoQEditText.toPlainText() + " " + self.capacityQEditText.toPlainText() + " "+self.alreadyPresentpeopleQEditText.toPlainText() + " " +self.nServersQEditText.toPlainText()+ " " +self.timeQEditText.toPlainText()
        
        lam2=0
        meo2=0
        n=0
        
        if re.match(r"[0-9]+/[0-9]+\b",self.lambdaQEditText.toPlainText()):
            
            ar2=re.split("/",self.lambdaQEditText.toPlainText())
            lam2=int(ar2[0])/float(ar2[1])
            n+=1
            st1=self.meoQEditText.toPlainText() + " " + self.capacityQEditText.toPlainText() + " "+self.alreadyPresentpeopleQEditText.toPlainText() + " " +self.nServersQEditText.toPlainText()+ " " +self.timeQEditText.toPlainText()

        if re.match(r"[0-9]+/[0-9]+\b",self.meoQEditText.toPlainText()):
            ar2=re.split("/",self.meoQEditText.toPlainText())
            meo2=int(ar2[0])/float(ar2[1])
            n+=1
            if n!=1:
                st1=self.capacityQEditText.toPlainText() + " "+self.alreadyPresentpeopleQEditText.toPlainText() + " " +self.nServersQEditText.toPlainText()+ " " +self.timeQEditText.toPlainText()
            else:
                st1=self.lambdaQEditText.toPlainText() + " " + self.capacityQEditText.toPlainText() + " "+self.alreadyPresentpeopleQEditText.toPlainText() + " " +self.nServersQEditText.toPlainText()+ " " +self.timeQEditText.toPlainText()
        ar1=re.search(r"[^\d\s.//]",st1)
        ar=re.findall(r"([0-9]+\.[0-9]+)|(\.[0-9]+)|([0-9]+)",st1)

        flag=0
        if(self.alreadyPresentpeopleQEditText.toPlainText()==self.capacityQEditText.toPlainText()):
            if(self.alreadyPresentpeopleQEditText.toPlainText()!="0"):
                flag=1
        
        if(len(ar)+n==6 and ar1==None and flag==0):
            
            if lam2==0:
                lam2=float(self.lambdaQEditText.toPlainText())

            if meo2==0:
                meo2=float(self.meoQEditText.toPlainText())

            deter=QueueOperations.Deter(lam2,meo2,
            int(self.capacityQEditText.toPlainText()),int(self.alreadyPresentpeopleQEditText.toPlainText()))
            deter.tI()
            if(self.alreadyPresentpeopleQEditText.toPlainText()=="0" and self.capacityQEditText.toPlainText()=="0"):
                deter.ti=0
                self.resultLabel.setGeometry((self.width()/2)-70,470,300,70)
                st="Ti: "+"0"+", n("+self.timeQEditText.toPlainText()+"): "+str(deter.nTCase(float(
                self.timeQEditText.toPlainText()
                )))
            else:
                st="Ti: "+str(deter.ti)+", n("+self.timeQEditText.toPlainText()+"): "+str(deter.nTCase(float(
                self.timeQEditText.toPlainText()
                )))+ ", Wqn("+self.nServersQEditText.toPlainText()+"): "+str(deter.wqN(int(self.nServersQEditText.toPlainText())))

            self.resultLabel.setText(st)
            
            self.drawButton.setVisible(True)
            self.resultLabel.setVisible(True)
        else:
            self.resultLabel.setGeometry((self.width()/2)-60,480,200,100)
            self.resultLabel.setText("Invalid Input")
            self.drawButton.setVisible(False)
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



        self.nServersLabel=QLabel('n : ',self)
        self.nServersLabel.setFont(QFont('Sanserif',16))
        self.nServersLabel.move(350,200)
        self.nServersLabel.adjustSize()
        
        self.nServersQEditText=QTextEdit(self)
        self.nServersQEditText.setGeometry(390,190,200,50)
        self.nServersQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.nServersQEditText.setFont(QFont('Sanserif',13))
        self.nServersQEditText.setAlignment(Qt.AlignCenter)
        self.nServersQEditText.setPlaceholderText('waiting for n..')
        self.nServersQEditText.setTextColor(QColor(0, 255, 0))


        self.timeLabel=QLabel('t : ',self)
        self.timeLabel.setFont(QFont('Sanserif',16))
        self.timeLabel.move(100,300)
        self.timeLabel.adjustSize()
        
        self.timeQEditText=QTextEdit(self)
        self.timeQEditText.setGeometry(140,290,200,50)
        self.timeQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.timeQEditText.setFont(QFont('Sanserif',13))
        self.timeQEditText.setAlignment(Qt.AlignCenter)
        self.timeQEditText.setPlaceholderText('enter the time..')
        self.timeQEditText.setTextColor(QColor(255, 0, 0))


        self.capacityLabel=QLabel('k : ',self)
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

        
        self.alreadyPresentpeopleLabel=QLabel('M : ',self)
        self.alreadyPresentpeopleLabel.setFont(QFont('Sanserif',16))
        self.alreadyPresentpeopleLabel.move(350,400)
        self.alreadyPresentpeopleLabel.adjustSize()
        
        self.alreadyPresentpeopleQEditText=QTextEdit(self)
        self.alreadyPresentpeopleQEditText.setGeometry(400,390,200,50)
        self.alreadyPresentpeopleQEditText.setStyleSheet("border: 1px solid; border-radius:15px; background-color: palette(base); ")
        self.alreadyPresentpeopleQEditText.setFont(QFont('Sanserif',13))
        self.alreadyPresentpeopleQEditText.setAlignment(Qt.AlignCenter)
        self.alreadyPresentpeopleQEditText.setPlaceholderText('peresent people..')
        self.alreadyPresentpeopleQEditText.setTextColor(QColor(0, 255, 0))


        self.submitButton = QPushButton('Submit',self)
        self.submitButton.setFont(QFont('Sanserif',14))
        self.submitButton.setStyleSheet('color:white;background-color:firebrick;border: 0px solid; border-radius:15px')
        self.submitButton.move((self.width()/2)-50,460)
        self.submitButton.clicked.connect(self.handleSubmit)
        

        #out Label................

        self.resultLabel = QLabel('.............................................................',self)
        self.resultLabel.setFont(QFont('Sanserif',14))
        self.resultLabel.setStyleSheet('color:magenta')
        self.resultLabel.adjustSize()
        self.resultLabel.setVisible(False)
       # self.resultLabel.move((self.width()/2)-250,500)
        self.resultLabel.setGeometry((self.width()/2)-140,470,340,70)
        
        self.drawButton = QPushButton('Draw',self)
        self.drawButton.setFont(QFont('Sanserif',14))
        self.drawButton.setStyleSheet('color:white;background-color:dodgerblue;border: 0px solid; border-radius:15px')
        self.drawButton.move((self.width()/2)-50,550)
        self.drawButton.setVisible(False)
        self.drawButton.clicked.connect(self.showGraph)

        










    

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
            sys.exit(QApplication(sys.argv).exec_())                   
            
        elif userInfo == QMessageBox.No:
            event.ignore()       
    
    def showGraph(self):
        λ = 1 / 3


        global deter


        arr = [deter.nTCase(n) for n in range(deter.ti+40)]

        x = np.array(arr)

        m=int(self.alreadyPresentpeopleQEditText.toPlainText())
        k=int(self.capacityQEditText.toPlainText())
        
        names = [f'c{n}' for n in range(23)]
        #if m==0 and k!=0:
         #   arrival=[n for n in range(int(1/deter.lambdda),(deter.ti)+((int(1/deter.lambdda))*5),int(1/deter.lambdda))]
        #else:
         #   arrival=[n for n in range(0,(deter.ti)+((int(1/deter.lambdda))*5),int(1/deter.lambdda))]
        arrival = [n for n in range(int(1/deter.lambdda),(deter.ti)+((int(1/deter.lambdda))*5),int(1/deter.lambdda))]
        
        departures = []

        if int(self.alreadyPresentpeopleQEditText.toPlainText())==0:
            
            if( self.capacityQEditText.toPlainText()=="0"):
                 for n in range(int(1/deter.lambdda)+1,(deter.ti)+((int(1/deter.lambdda))*5)):
                    if deter.is_departure(n):
                        departures.append(n)
                    
            else:
                for n in range(int(1/deter.lambdda)+1,(deter.ti)+((int(1/deter.lambdda))*5)):
                    if deter.is_departure(n) and n<deter.ti:
                        departures.append(n)
                    if n>deter.ti and n%int(1/deter.lambdda)==0:
                        departures.append(n)
        else:
            for n in range(0,(deter.ti)+((int(1/deter.lambdda))*5)):
                    
                    if m>0:
                        print(m)
                        departures.append(n)
                        m-=int(1/deter.meu)
                    if n % int(1/deter.lambdda)==0:
                        m+=1
                    

        dates = [n // 2 for n in range(46)]
        x_values = arrival + departures
        y_values = [2 for n in range(len(arrival))] + [-2 for n in range(len(departures))]
        labels = [f'c{n}' for n in range(1,len(arrival))]

        levels = np.tile([4, 4, -5],
                        int(np.ceil(len(dates) / 3)))[:len(dates)]

        # Create figure and plot a stem plot with the date
        fig, (ax, ax2) = plt.subplots(2, figsize=(23, 23))
        ax.set(title="customers arrival and departure", xlabel="('time in seconds')")

        ax.vlines(x_values, 0, y_values, color="tab:blue")  # The vertical stems.
        ax.xaxis.set_ticks(np.arange(min(x_values), max(x_values) + 1, 1.0))
        ax.plot(x_values, np.zeros_like(x_values), "-o", color="k", markerfacecolor="w")  # Baseline and markers on it.
        
        # annotate lines
        for d, l, r in zip(x_values, y_values, labels):
            ax.annotate(r, xy=(d, l),
                        xytext=(-3, np.sign(l) * 3), textcoords="offset points",
                        horizontalalignment="center",
                        verticalalignment="bottom" if l > 0 else "top")

        # remove y axis and spines
        ax.get_yaxis().set_visible(False)
        # for spine in ["left", "top", "right"]:
        #     ax.spines[spine].set_visible(False)

        ax.margins(y=0.2)
        ax2.step(range(deter.ti + 40), x, where='post')
        ax2.set(ylabel='number of customers', xlabel='time in seconds', title='number of custorms at each second')
        plt.grid(axis='x', color='0.95')
        plt.show()

        plt.show()
