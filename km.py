
from cProfile import label
from cgitb import text
from distutils.command.build_scripts import first_line_re
import sys
import math
from unittest import main
from PyQt5 import QtWidgets            
from PyQt5 import QtGui
from PyQt5 import QtCore

class Mywindow1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,500,300)
        
        self.first_line_edit=QtWidgets.QLineEdit()
        self.km_button=QtWidgets.QPushButton("convert to km")
        self.km_button.clicked.connect(self.km_function)
        self.mil_button=QtWidgets.QPushButton("convert to ml")
        self.mil_button.clicked.connect(self.mil_function)



        self.label_first=QtWidgets.QLabel("")
        self.label_first1=QtWidgets.QLabel("")
        self.label_first3=QtWidgets.QLabel("")


        #buttons
        self.buttons={} 
        self.button_info={"C":[2,0], "««":[2,1], "0": [2,2],
                        "7":[3,0],"8":[3,1],"9":[3,2],
                        "4":[4,0],"5":[4,1],"6":[4,2],
                        "1":[5,0],"2":[5,1],"3":[5,2],


        }
  
        # changing icon
        main_layaut=QtWidgets.QGridLayout()
        
        #lineddit
        main_layaut.addWidget(self.label_first,0,0)
        main_layaut.addWidget(self.first_line_edit,0,1)

        main_layaut.addWidget(self.label_first1,0,2)

        main_layaut.addWidget(self.label_first3,1,0)
        main_layaut.addWidget(self.km_button,1,1)
        main_layaut.addWidget(self.mil_button,1,2)

        self.km_button.clicked.connect(self.km_function)


    #creating button

        for btn_name, pos in self.button_info.items():
            self.buttons[btn_name]=QtWidgets.QPushButton(btn_name)
            main_layaut.addWidget(self.buttons[btn_name], *pos)
            
        self.setup_events()

       

        vertical_layaout=QtWidgets.QVBoxLayout()
        vertical_layaout.addStretch(10)
        vertical_layaout.addLayout(main_layaut,90)


        
        self.setLayout(vertical_layaout)

    #function
    
    def km_function(self):
        num1=self.first_line_edit.text()
        if num1.isdigit():
            self.first_line_edit.setText("")
            res=int(num1) / 0.62137  
            self.first_line_edit.setText(str(res))
        elif num1.isalpha():
            self.first_line_edit.setText("error")

    def mil_function(self):
        num1=self.first_line_edit.text()
        if num1.isdigit():
            self.first_line_edit.setText("")
            res=int(num1) * 0.62137  
            self.first_line_edit.setText(str(res))
        else:
            self.first_line_edit.setText("error")

    def setup_events(self):
        for btn_name, pos in self.button_info.items():

         if btn_name not in {"C", "««"}:
            self.buttons[btn_name].clicked.connect(self.evn_btn_clicked )

        if self.first_line_edit !="":
            self.buttons["C"].clicked.connect(self.evt_clear)
       

     

        self.buttons["««"].clicked.connect(self.remove_last_char)
      
    


    #all function section

      
    #menu bar function                                         

   
    #clear everythin in line_edit function
    def evt_clear(self):
         self.first_line_edit.clear()




    #add text in line_edit function
    def evn_btn_clicked(self):
        old_text = self.first_line_edit.text()
        self.first_line_edit.setText(old_text + self.sender().text())

  
    
        
    #function back
    def remove_last_char(self):
        num1=self.first_line_edit.text()
        num1=num1[:-1]
        self.first_line_edit.setText(num1)

   


                                              







