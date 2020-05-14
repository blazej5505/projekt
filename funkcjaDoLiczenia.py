# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import math

class Maschine(QWidget):
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
        
    def kineticEnergy(self):
        if int(self.massEdt.text()) == 0:
            self.resultEdt.setText("div by 0")
        else:
            value = 2.53*int(self.chargeEdt.text())**2/int(self.massEdt.text())
            value = "{:.2f}".format(value)
            self.resultEdt.setText(str(value))
            
    def Velocity(self):
        if int(self.massEdt.text()) == 0:
            self.resultEdt.setText("div by 0")
        else:
            value = 2.25*int(self.chargeEdt.text())/int(self.massEdt.text())
            value = "{:.2f}".format(value)
            self.resultEdt.setText(str(value))
            
        
        

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Maschine()
    sys.exit(app.exec_())
    
      

        