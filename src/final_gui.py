# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os,sys,subprocess
import main_copy
class Ui_MainWindow(object):
    pc=0
    ir=0
    reg=0
    idi=0
    dd=0
    clock=0
    pc_f=0
    pc_t=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 70, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(445, 230, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 750, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 380, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 20, 20, 751))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 430, 256, 331))
        self.tableWidget.setRowCount(32)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(580, 390, 20, 381))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 390, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 390, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 71, 17))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 271, 661))
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(620, 420, 291, 341))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(13)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(310, 420, 256, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(305, 230, 131, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(385, 120, 101, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 330, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(370, 280, 181, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(370, 320, 181, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 40, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 165, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(390, 165, 101, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(620, 80, 281, 301))
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(620, 70, 281, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(580, 60, 20, 381))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,42)
        self.tableWidget.setColumnWidth(2,42)
        self.tableWidget.setColumnWidth(3,42)
        self.tableWidget.setColumnWidth(4,42)
        self.tableWidget_2.setColumnWidth(0,80)
        self.tableWidget_2.setColumnWidth(1,42)
        self.tableWidget_2.setColumnWidth(2,42)
        self.tableWidget_2.setColumnWidth(3,42)
        self.tableWidget_2.setColumnWidth(4,42)
        self.tableWidget_3.setColumnWidth(1,135)
    def loaddata(self,dic):
        i=0
        for x in dic:
            temp2="x"+str(x)
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(temp2))
            temp1=dic[x].upper()
            for j in range(1,6):
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(temp1[2*j:2*(j+1)]))
            i+=1
    def loaddata2(self,dic):
        i=0
        self.tableWidget_3.setRowCount(max(11,len(dic)))
        for x in dic:
            self.tableWidget_3.setItem(i,0,QtWidgets.QTableWidgetItem(x))
            temp1=dic[x].upper()
            self.tableWidget_3.setItem(i,1,QtWidgets.QTableWidgetItem(temp1))
            i+=1
    def loaddata3(self,dic):
        
        t1=list(dic.keys())
        newdic={}
        for i in range(len(t1)):
            newdic[int(t1[i],16)]=dic[t1[i]][2:]
            t1[i]=int(t1[i],16)
        t1.sort()
        fina={}
        nice=0
        for i in range(len(t1)):
            if(t1[i]%4==0):
                nice=t1[i]//4
                fina[hex(nice*4)]=newdic[t1[i]]+"000000"
            else:
                nice=t1[i]//4
                etc=t1[i]%4
                if(fina.get(hex(nice*4),-1)==-1):
                    fina[hex(nice*4)]="00"*(etc)+newdic[t1[i]]+"00"*(3-etc)
                else:
                    fina[hex(nice*4)]=fina[hex(nice*4)][:2*(etc)]+newdic[t1[i]]+fina[hex(nice*4)][2*(etc+1):]
        self.tableWidget_2.setRowCount(max(13,len(fina)))
        i=0
        for x in fina:
            self.tableWidget_2.setItem(i,0,QtWidgets.QTableWidgetItem(x))
            temp1=fina[x].upper()
            for j in range(1,6):
                self.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(temp1[2*(j-1):2*(j)]))
            i+=1
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RISC-V Simulator"))
        self.pushButton.setText(_translate("MainWindow", "GUI Help"))
        self.pushButton_2.setText(_translate("MainWindow", "Open data.mc"))
        self.pushButton_3.setText(_translate("MainWindow", "RUN"))
        self.pushButton_4.setText(_translate("MainWindow", "Output Log"))
        self.label_3.setText(_translate("MainWindow", "Register View"))
        self.label_4.setText(_translate("MainWindow", "Memory View"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">          Register</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "STEP"))
        self.pushButton_6.setText(_translate("MainWindow", "ASSEMBLE"))
        self.label_5.setText(_translate("MainWindow", "PC :"))
        self.label_6.setText(_translate("MainWindow", "IR:"))
        self.label_7.setText(_translate("MainWindow", "Instructions"))
        self.label_8.setText(_translate("MainWindow", "Clock:"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">           PC                Instructions</p></body></html>"))
        # new stuff
        self.label.adjustSize()
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        self.pushButton_2.clicked.connect(lambda: self.opendata())
        self.pushButton.clicked.connect(lambda: self.guihelp())
        self.pushButton_4.clicked.connect(lambda: self.outputlog())
        self.pushButton_6.clicked.connect(lambda: self.assembly())
        self.pushButton_5.clicked.connect(lambda: self.step())
        self.pushButton_3.clicked.connect(lambda: self.run())


    def opendata(self):
        try:
            string=os.path.abspath(os.getcwd())
            string+="\data.mc"
            os.startfile(string)
        except:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "data.mc"])
    def guihelp(self):
        try:
            string=os.path.abspath(os.getcwd())
            string+="\guihelp.txt"
            os.startfile(string)
        except:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "guihelp.txt"])
    def outputlog(self):
        try:
            string=os.path.abspath(os.getcwd())
            string+="\output.txt"
            os.startfile(string)
        except:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "output.txt"])
    def assembly(self):
        self.ir,self.pc,self.reg,self.idi,self.dd,self.clock,self.pc_f,self.pc_t=main_copy.assemble()
        self.loaddata(self.reg)
        self.loaddata2(self.idi)
        self.loaddata3(self.dd)
        self.textBrowser_3.clear()
        self.textBrowser_3.append(self.pc)
        self.textBrowser_4.clear()
        self.clockadj()
        self.tableWidget_2.clear()


    def step(self):
        print(self.pc)
        if(self.pc!=-1):
            self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock=main_copy.runstep(self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock)
            self.loaddata(self.reg)
            self.loaddata2(self.idi)
            self.loaddata3(self.dd)
            self.textBrowser_3.clear()
            if(self.pc!=-1):
                self.textBrowser_3.append(str(self.pc))
            else:
                self.textBrowser_3.append("Completed")
            self.textBrowser_4.clear()
            self.textBrowser_4.append(self.ir)
            self.clockadj()
        else:
            return
    def run(self):
        while(self.pc!=-1):
            self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock=main_copy.runstep(self.idi,self.pc,self.pc_f,self.pc_t,self.reg,self.dd,self.ir,self.clock)
            self.loaddata(self.reg)
            self.loaddata2(self.idi)
            self.loaddata3(self.dd)
            self.textBrowser_3.clear()
            if(self.pc!=-1):
                self.textBrowser_3.append(str(self.pc))
            else:
                self.textBrowser_3.append("Completed")
            self.textBrowser_4.clear()
            self.textBrowser_4.append(self.ir)
            self.clockadj()

    def clockadj(self):
        self.textBrowser_6.clear()
        temp1=""
        if(self.clock==1):
            temp1=str(self.clock)+" Cycle"
        else:
            temp1=str(self.clock)+ " Cycles"
        self.textBrowser_6.append(temp1)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())