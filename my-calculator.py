
from cgi import MiniFieldStorage
from cgitb import text
from lib2to3.pgen2.token import EQUAL
import sys 
import math
from tkinter import Widget
from unittest import main
from PyQt5 import QtWidgets            
from PyQt5 import QtGui
from PyQt5 import QtCore
from km import Mywindow1


class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calculator") 
        self.setGeometry(500,500,500,300)
        self.add_menu_bar()
        
        self.first_line_edit=QtWidgets.QLineEdit()
        self.second_line_edit=QtWidgets.QLineEdit()
        #buttons
        self.buttons={}
        self.button_info={"x²":[2,0],"π":[2,1],"C":[2,2], "««":[2,3], "*":[2,4],"/":[2,5],

                        "10(x)":[3,0],"7":[3,1], "8":[3,2], "9":[3,3],"(":[3,4], ")":[3,5],

                        "1/x":[4,0],"4":[4,1],"5":[4,2],"6":[4,3],"-":[4,4], "+":[4,5],

                        "√":[5,0],"1":[5,1],"2":[5,2],"3":[5,3],"mod":[5,4], "n!":[5,5],

                        "x(y)": [6,0],"+/-": [6,1],"0": [6,2], "=": [6,3], ".":[6,4], "%":[6,5] 
        }
        
      

    
        main_layaut=QtWidgets.QGridLayout()

        #lineddit
        main_layaut.addWidget(self.first_line_edit,1,0,1,6)
        main_layaut.addWidget(self.second_line_edit,0,0,1,6)

    #creating button

        for btn_name, pos in self.button_info.items():
            self.buttons[btn_name]=QtWidgets.QPushButton(btn_name)
            main_layaut.addWidget(self.buttons[btn_name], *pos)
            
        self.setup_events()
        self.styling()

       


        vertical_layaout=QtWidgets.QVBoxLayout()
        self.first_line_edit.setAlignment(QtCore.Qt.AlignRight)
        vertical_layaout.addStretch(5)
        self.second_line_edit.setAlignment(QtCore.Qt.AlignLeft)
        vertical_layaout.addStretch(5)


        vertical_layaout.addLayout(main_layaut,90)


        widget=QtWidgets.QWidget()
        widget.setLayout(vertical_layaout)
        self.setCentralWidget(widget)

    #function

    def setup_events(self):
        for btn_name, pos in self.button_info.items():

         if btn_name not in {"C", "=", "x²", "1/x", "««","10(x)", "√", "mod", "n!", "x(y)", "+/-", "%","π"}:
            self.buttons[btn_name].clicked.connect(self.evn_btn_clicked )

        self.buttons["1/x"].clicked.connect(self.one_devide_x)
        self.buttons["C"].clicked.connect(self.evt_clear)
        self.buttons["="].clicked.connect(self.evt_equal_btn_clicked)
        self.buttons["x²"].clicked.connect(self.number_square)
        self.buttons["««"].clicked.connect(self.remove_last_char)
        self.buttons["10(x)"].clicked.connect(self.ten_gr)
        self.buttons["√"].clicked.connect(self.number_root)
        self.buttons["+/-"].clicked.connect(self.opposite)
        self.buttons["π"].clicked.connect(self.p)
        self.buttons["n!"].clicked.connect(self.fact)
        self.buttons["x(y)"].clicked.connect(self.x_square_y)
        self.buttons["mod"].clicked.connect(self.mod_function)



        


    #all function section

    #style
        for btn_name in {"1", "2","3", "4","5", "6","7", "8","9", "0",}:
            self.buttons[btn_name].setStyleSheet("background-color:#ffcff1;")

    def styling(self):
        style = """
            QMainWindow {
                background-color:#a2a2d0;
            }
            QPushButton {
                background-color:#bfff00;
                color:#696969;
                font: 24px bold ;
                border: 5px solid #8f8f91;
                border-radius: 16px;
                padding: 3px;
            }
            QLineEdit {
                background-color:#a2a2d0
		;
                color: #F0F7D4;
                font: 30px;
                border: none;
            }

          QPushButton:hover
          { background-color: #89CFF0	 }

         

        """
        self.setStyleSheet(style)

      
    #menu bar function                                         

    def add_menu_bar(self):
        menu_bar = QtWidgets.QMenuBar()
        mode_menu = menu_bar.addMenu("Calculator-Mode")
        

        default_mode = QtWidgets.QAction("Standart", self)
        default_mode.triggered.connect(self.defaul)

        km_mode = QtWidgets.QAction("km/miles", self)
        km_mode.triggered.connect(self.km)

      

        #connect

        mode_menu.addAction(default_mode)
        mode_menu.addAction(km_mode)

        self.setMenuBar(menu_bar)

    def defaul (self):

        widget1=Mywindow()
        self.setCentralWidget(widget1)

 
    def km(self):
        wwidget=Mywindow1()
      

        style = """
            QMainWindow {
                background-color:#E6E6FA	;
            }
            QPushButton {
                border-radius: 20px;
                background-color:#E6E6FA;
                color: #20B2AA;
                font: 24px;
                margin: 1;
            }

            QLineEdit {
                background-color:#E6E6FA	;
                color:#20B2AA;
                font: 30px;
                border: none;
            }
            QPushButton:hover{
                background-color:#F08080;

            }

        """
      

        self.setCentralWidget(wwidget)
        self.setStyleSheet(style)



    #clear everythin in line_edit function
    def evt_clear(self):
         self.first_line_edit.clear()
         self.second_line_edit.clear()

    #add text in line_edit function
    def evn_btn_clicked(self):
        old_text = self.first_line_edit.text()
        self.first_line_edit.setText(old_text + self.sender().text())

            
        
    #equal function
    def evt_equal_btn_clicked(self):
        dic={"^": "**", "mod": "%"}
        equation=self.first_line_edit.text()
        for key, value in dic.items():
            equation=equation.replace(key,value)


            
        result=eval(equation)
        self.first_line_edit.setText(str(result))
    #history
        ls=[]
        ls.append(equation)
        joi="".join(ls[-1])
        if self.first_line_edit !="0":
            self.second_line_edit.setText( f'{joi}={result}')
        elif self.first_line_edit =="0":
            self.second_line_edit.setText("0")



    #uaryofiti ricxvis dadebitad gadayvana da piriqit
    def opposite(self):
        number1=self.first_line_edit.text()
        if "-" in number1:
            self.first_line_edit.setText(number1.replace("-",""))
        else:
            self.first_line_edit.setText(f'- {number1}')

        
    #x number square y

    def x_square_y(self):
        number1=self.first_line_edit.text()
        self.first_line_edit.setText(number1 + "^")

     #mod function

    def mod_function(self):
        number1=self.first_line_edit.text()
        self.first_line_edit.setText(number1 + "%")


    #number square function ( kvadratshi ayvana)
    def number_square(self):
        number1=self.first_line_edit.text()
        sq=int(number1) * int(number1)
        self.first_line_edit.setText(str(sq))
    
    #1 divide x function
    def one_devide_x(self):
        number1=self.first_line_edit.text()
        devide_x= 1 / int(number1)
        self.first_line_edit.setText(str(devide_x))


        
        
    #10  grade (is xarisxshi ayvana)
    def ten_gr(self):
        num1=self.first_line_edit.text()
        sq=10 **int(num1) 
        self.first_line_edit.setText(str(sq))


    #number root function ( fesvis amogeba)
    def number_root(self):
        num1=math.sqrt(int(self.first_line_edit.text()))
        self.first_line_edit.setText(str(num1))


    #P (3.14) function
    def p(self):
        num1=self.first_line_edit.text()
        pi=3.14
        self.first_line_edit.setText(num1 + str(pi))


      
    #function back
    def remove_last_char(self):
        num1=self.first_line_edit.text()
        num1=num1[:-1]
        self.first_line_edit.setText(num1)

    

    #function factorial
    def fact(self):

        num1=self.first_line_edit.text()
        num1=int(num1)
        if num1 <= 0:
            self.first_line_edit.setText("0")
        else:
            n=1
            for i in range(1,num1+1):
                n=n*i

            self.first_line_edit.setText(str(n))




   

    

if __name__=="__main__":
    app= QtWidgets.QApplication(sys.argv)      
    win=Mywindow()
    win.show()
    sys.exit(app.exec_())                                               



