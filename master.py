from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QCoreApplication
import sys
import matplotlib.pyplot as plt 
from matplotlib import style
import random
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Application(QtWidgets.QMainWindow):

    def __init__(self):
        super(Application, self).__init__() 
        self.setWindowTitle("I'm a cyclotron and I cure cancer. Check out my particles")
        self.setGeometry(100,100, 500, 300)

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setText("Notes here")

        menuClose = QtWidgets.QAction("Exit", self) 
        menuClose.setShortcut("Ctrl+Q")
        menuClose.setStatusTip("It closes the app")
        menuClose.triggered.connect(self.closeApp)
        
        menuSave = QtWidgets.QAction("Save your notes", self)
        menuSave.setShortcut("Crtl+S")
        menuSave.setStatusTip("Saves your notes to a file")
        menuSave.triggered.connect(self.fileSave)

        menuCompile = QtWidgets.QAction("TURN ON THE MACHINE", self)
        menuCompile.setStatusTip("FULL POWER!!!")
        menuCompile.triggered.connect(self.compileFunc)

        menuCompare = QtWidgets.QAction("Compare with other particles", self)
        menuCompare.setStatusTip("Compares with alfa particle and proton")
        menuCompare.triggered.connect(self.compareFunc)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(menuSave)
        fileMenu.addAction(menuClose)

        compMenu = mainMenu.addMenu("Compile")
        compMenu.addAction(menuCompile)
        compMenu.addAction(menuCompare)

        self.statusBar()
        self.show()

    def compileFunc(self):
        Machine(self)


    def compareFunc(self):
        style.use('seaborn')
        fig = plt.figure()

        def values():
            xs = []
            ys = []

            for i in range (0,3,1):
                x = i
                y = random.randrange(3,100,1)

                xs.append(x)
                ys.append(y)

            return xs, ys

        plot1 = plt.subplot2grid((1,2), (0,0), colspan = 1, rowspan = 1)
        plot2 = plt.subplot2grid((1,2), (0,1), colspan = 1, rowspan = 1)

        x,y = values()
        plot1.bar(x,y, label = 'Kinetic energy', color = 'orange')
        plot1.set_xlabel("Electrone/Alfa/Protone")
        plot1.set_ylabel("value in Joules")

        x,y = values()
        plot2.bar(x,y, label = 'velocity')
        plot2.set_xlabel('Electrone/Aflfa/Protone')
        plot2.set_ylabel("Value in meters per seconds ")
        plot1.legend()
        plot2.legend()
        plt.show()

    def fileSave(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', "", "text files (*txt *docx *html)")
        with open(name[0], 'w') as filename:
            textFile = self.textEdit.toPlainText()
            filename.write(textFile)
        sys.exit()
        self.show()    

    def closeApp(self): 
        choice = QtWidgets.QMessageBox.question(self, "Exit window", 
        "Are you sure?",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


class Machine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
      
        lb1 = QLabel("Mass of a particle: [kg]", self)
        lb2 = QLabel("Charge of a particle: [C]", self)
        lb3 = QLabel("Result:", self)


        ukladT = QGridLayout()
        ukladT.addWidget(lb1, 0, 0)
        ukladT.addWidget(lb2, 0, 1)
        ukladT.addWidget(lb3, 0, 2)

       
        self.setLayout(ukladT)
        
                 
        self.massEdt = QLineEdit()
        self.chargeEdt = QLineEdit()
        self.resultEdt = QLineEdit()
        self.resultEdt.setDisabled(True)

        self.resultEdt.readonly = True
        self.resultEdt.setToolTip("It's a final value of physical quantity chosen by you for a particle described by your parameters")
        self.massEdt.setToolTip("Choose value of mass of a particle")
        self.chargeEdt.setToolTip("Choose value of charge of a particle")
        
        
        ukladT.addWidget(self.massEdt, 1, 0)
        ukladT.addWidget(self.chargeEdt, 1, 1)
        ukladT.addWidget(self.resultEdt, 1, 2)

        
        ekBtn = QPushButton("Kinetic Energy [J]", self)
        ekBtn.clicked.connect(self.kineticEnergy)
        
        velBtn = QPushButton("Velocity [m/s]", self)
        velBtn.clicked.connect(self.Velocity)
        
        endBtn = QPushButton("Cancel", self)
        endBtn.clicked.connect(self.end)

        ukladH = QHBoxLayout()
        ukladH.addWidget(ekBtn)
        ukladH.addWidget(velBtn)
        

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(endBtn, 3, 0, 1, 3)

        self.setGeometry(40, 40, 300, 100)        
        self.setWindowTitle("Maschine")
        self.show()
        
    def end(self):
        self.close()
        
    def kineticEnergy(self, value):
        if int(self.massEdt.text()) == 0:
            self.resultEdt.setText("div by 0")
        else:
            value = 2.53*int(self.chargeEdt.text())**2/int(self.massEdt.text())
            value = "{:.2f}".format(value)
            self.resultEdt.setText(str(value))

        return float(value)
        self.graph()
            
    def Velocity(self, value):
        if int(self.massEdt.text()) == 0:
            self.resultEdt.setText("div by 0")
        else:
            value = 2.25*int(self.chargeEdt.text())/int(self.massEdt.text())
            value = "{:.2f}".format(value)
            self.resultEdt.setText(str(value))

        return value
        self.graph()
    
    def graph(self):
        Velocity()
        style.use('seaborn')
        fig = plt.figure()
        x = [i for i in range(0,3,1)]
        y = value
         
        """
        def graphValues():
            xs = []
            ys = []

            for i in range (0,3,1):
                x = i
                y = value

                xs.append(x)
                ys.append(y)

            return xs, ys
        """
        plot1 = plt.subplot2grid((1,2), (0,0), colspan = 1, rowspan = 1)
        plot2 = plt.subplot2grid((1,2), (0,1), colspan = 1, rowspan = 1)

        x,y = graphValues()
        plot1.bar(x,y, label = 'Kinetic energy', color = 'orange')
        plot1.set_xlabel("Electrone/Alfa/Protone")
        plot1.set_ylabel("value in Joules")

        x,y = graphValues()
        plot2.bar(x,y, label = 'velocity')
        plot2.set_xlabel('Electrone/Aflfa/Protone')
        plot2.set_ylabel("Value in meters per seconds ")
        plot1.legend()
        plot2.legend()
        plt.show()


app = QtWidgets.QApplication([]) 
Open = Application()
app.exec_()
