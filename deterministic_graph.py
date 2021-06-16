from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLabel,QToolTip,QDesktopWidget,QMainWindow,QStatusBar,QHBoxLayout,QVBoxLayout,QColorDialog
import sys
from PySide2.QtGui import QIcon,QPixmap,QFont,QGuiApplication,Qt,QColor
import matplotlib.colors as myColor
import MainWindow
from PySide2.QtWidgets import QRadioButton,QTextEdit

class DeterministicGraphScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Deterministic Graph')
        self.setGeometry(150,150,800,600)
        self.setFixedSize(800,600)
        