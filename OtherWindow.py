# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from pygame import mixer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLCDNumber, QMenuBar
from PyQt5.QtCore import QUrl, QTime, QTimer
import sys
from clock import DigitalClock
#imports for main core
import skimage
import numpy as np
import cv2
import time
#import requests
import urllib
from skimage.io import imread
#import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_mean
from skimage.filters import threshold_mean
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import disk
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import square
from tkinter import *
from tkinter import messagebox










###############################

url="http://192.168.43.1:8080/photo.jpg"
img_counter = 0

################################

class Ui_OtherWindow(object):
   


    def setupUi(self, OtherWindow):

        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(997, 677)
        OtherWindow.setMinimumSize(QtCore.QSize(997, 0))
        OtherWindow.setStyleSheet("background-image: url(:/newPrefix/eggtech.jpg);")
        




        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IEGD = QtWidgets.QLabel(self.centralwidget)
        self.IEGD.setGeometry(QtCore.QRect(280, 50, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Luminari")
        font.setPointSize(24)
        self.IEGD.setFont(font)
        self.IEGD.setObjectName("IEGD")
        self.EGGIE = QtWidgets.QLabel(self.centralwidget)
        self.EGGIE.setGeometry(QtCore.QRect(460, 0, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Luminari")
        font.setPointSize(36)
        self.EGGIE.setFont(font)
        self.EGGIE.setObjectName("EGGIE")
        self.start_int = QtWidgets.QPushButton(self.centralwidget)
        self.start_int.setGeometry(QtCore.QRect(100, 370, 211, 61))
        self.start_int.setObjectName("start_int")
        #self.save = QtWidgets.QPushButton(self.centralwidget)
        #self.save.setGeometry(QtCore.QRect(440, 290, 113, 32))
        #self.save.setObjectName("save")
        self.start_ex = QtWidgets.QPushButton(self.centralwidget)
        self.start_ex.setGeometry(QtCore.QRect(670, 330, 211, 61))
        self.start_ex.setObjectName("start_ex")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(450, 310, 91, 91))
        self.stop.setObjectName("stop")
        self.stop.setStyleSheet("background-image: url(:/newPrefix/shutdown.png);")

        self.report= QtWidgets.QPushButton(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(440, 430, 113, 32))
        self.report.setObjectName("report")


        self.DigitalClock=DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(20, 180, 150, 27))
        
        
        self.clock_label = QtWidgets.QLabel(self.centralwidget)
        self.clock_label.setGeometry(QtCore.QRect(25, 185, 33, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clock_label.setFont(font)
        self.clock_label.setObjectName("clock_label")

        OtherWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.setNativeMenuBar(False)

        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")

        
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        OtherWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menufile.menuAction()) 
        self.menubar.addAction(self.menuabout.menuAction())
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)
       
        #######BUTTONS################################
        self.start_int.clicked.connect(self.Internal)
        self.start_ex.clicked.connect(self.External)
        self.stop.clicked.connect(self.Stop)
        self.report.clicked.connect(self.Report)
        


        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
    
  


    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow - EggIE(2019ver2.0) Created by: Danielle Mark O. Quijano"))
        self.IEGD.setText(_translate("OtherWindow", "Internal and External Egg Detection System"))
        self.EGGIE.setText(_translate("OtherWindow", "EggIE"))
        self.start_int.setText(_translate("OtherWindow", "Start Internal Egg Detection"))
        #self.save.setText(_translate("OtherWindow", ""))
        self.start_ex.setText(_translate("OtherWindow", "Start External Egg Detection"))
        self.menufile.setTitle(_translate("OtherWindow", "File"))
        self.menuabout.setTitle(_translate("OtherWindow", "About"))
        self.report.setText(_translate("OtherWindow", "Summary Report"))
        
        self.clock_label.setText(_translate("OtherWindow", "TIME:"))
####################REPORT##########
    def Report(self):
        from prettytable import PrettyTable
        from prettytable import from_csv


        #table from csv
        path="file location"
        csv_file = open(path)
        x = from_csv(csv_file)
    
        print(x)
    



####################INTERNAL#############################################
    def Internal(self):

        OtherWindow = QtWidgets.QMainWindow()
        
        mixer.init()
        mixer.music.load("trainedvoice_dataset/Internal1.mp3")
        mixer.music.play()
        QMessageBox.information(OtherWindow,"START!!",'Processing the Internal Egg Detection system. The system will find the yolk in each egg. The system will also detect if there are blood spot inside the yolk in each egg.')
        
        import urllib
        import cv2
        import numpy as np
        import requests
        #from pygame import mixer
        url='http://192.168.43.1:8080/photo.jpg'
        img_counter = 0

        while True:
            
            imgResp = requests.get(url)
            
            # Numpy to convert into a array
            imgNp = np.array(bytearray(imgResp.content), dtype=np.uint8)
            
            # Finally decode the array to OpenCV usable format ;) 

            img = cv2.imdecode(imgNp,-1)

            frame = cv2.resize(img,(1266,668))

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            

            
            

        ##############EGGDETECT###################################################
              #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            th, bw = cv2.threshold(hsv[:, :,2], 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            eggint = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    

            ######contours####
            _, contours, hierarchy = cv2.findContours(eggint, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            
            count_yolk = 0
            count_blood = 0
            
            for contour in contours:
                count_yolk += 1
                #cnt = contours[0]
                
                x,y,w,h = cv2.boundingRect(contour)
                area1 = cv2.contourArea(contour)

                #ellipse = cv2.fitEllipse(cnt)
                #cv2.ellipse(frame,ellipse,(0,255,0),2)
                print(area1)
                if area1 > 6000 and area1 < 10300:
                    
               # cv2.drawContours(frame, contour, -1, (0, 0, 255), 1)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
                    cv2.putText(frame, 'Yolk Found: NO Blood', (x, y), cv2.FONT_HERSHEY_PLAIN, 0.6, (0, 255, 0),1)



        ################YOLK################
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            imag = cv2.medianBlur(gray, 19)  #27
            imagblood = cv2.medianBlur(gray, 35)
            #Int = imag[:,:,2]
            #V_component = hsv[:,:,2]

            kernelE = np.ones((7,7),np.uint8)
            erosion = cv2.erode(imag,kernelE,iterations = 1)

            th = cv2.adaptiveThreshold(erosion, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 115, 1)
            
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            yolk = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

        

            #hsvb = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            #imag = cv2.medianBlur(hsvb, 3)  #27
            #grey = imag[:,:,2]


            #kernelbloodErosion = np.ones((5,5),np.uint8)
            #erosionblood = cv2.erode(grey,kernelbloodErosion,iterations = 1)

            #thblood = cv2.adaptiveThreshold(erosionblood, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 115, 1)
                        
            #kernelblood = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            #yolkblood = cv2.morphologyEx(thblood, cv2.MORPH_CLOSE, kernelblood)
           # inv_img = ~yolkblood
       


                # #########CONTOURS###################
            _, contours1, _ = cv2.findContours(yolk , cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
           # _, contours2, _ = cv2.findContours(yolkblood , cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    ##################finding bloodspot#####
            #count_blood = 0

            #for contour in contours2:

                
                #count_blood +=1
                #area = cv2.contourArea(contour)
                #x,y,w,h = cv2.boundingRect(contour)
               # comparea = area
              #  if area > 450 and area < 510:

                 #   cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
                #    cv2.putText(frame, 'BloodSpot Found: Area='+str(comparea), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 0, 1),1)
            yolkess = 2
            yolkresult  = 'Total Yolkless egg:'+str(yolkess)
            bloodspot  = 'Total Blood spot:'+str(count_blood)

            #cv2.putText(frame, 'Total Eggs with yolk:'+str(count_yolk), (10, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (55, 255, 50),2)
            cv2.putText(frame, 'Total Blood spot:'+str(count_blood), (10, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (55, 55, 255),2)
            cv2.imshow('Internal Egg: Yolk Detection',frame)
            cv2.imshow('Yolk Viewer',yolk)
            #cv2.imshow('inter',eggint)
           

        

            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                mixer.init()
                mixer.music.load("trainedvoice_dataset/stop.mp3")
                mixer.music.play()
                QMessageBox.critical(OtherWindow,"",'Egg Detection Terminated')
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                break
                
            elif cv2.waitKey(33) == ord('s'):
                mixer.init()
                mixer.music.load("trainedvoice_dataset/save1.mp3")
                mixer.music.play()
                img_INTname = "Results/InternalYolkScannedEggs_{}.png".format(img_counter)
                cv2.imwrite(img_INTname, frame)
                QMessageBox.information(OtherWindow,"Result", '<EGG DETECTION RESULT SAVED>         %s                           %s' %(yolkresult,bloodspot))
                print("{} saved!".format(img_INTname))
       
                img_counter += 1
                
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)

##########################EXTERNAL###########################################################
    def External(self):

        OtherWindow = QtWidgets.QMainWindow()
        mixer.init()
        mixer.music.load("trainedvoice_dataset/external1.mp3")
        mixer.music.play()
        QMessageBox.information(OtherWindow,"START!!",'Processing the External Egg Detection system. The system will find eggs with GOOD condition. The system will also detect if there are crack and dirt in each egg.')

        import urllib
        import cv2
        import numpy as np
        import requests
        #from pygame import mixer
        url='http://192.168.43.1:8080/photo.jpg'
        img_counter = 0
        

        
        
        
        while True:
                
            imgResp = requests.get(url)
                
             # Numpy to convert into a array
            imgNp = np.array(bytearray(imgResp.content), dtype=np.uint8)
                
                # Finally decode the array to OpenCV usable format ;) 
            img = cv2.imdecode(imgNp,-1)

            frame = cv2.resize(img,(1266,668))
        ################CRACK ALGORITHM####################################
    
            blurred_frame = cv2.GaussianBlur(frame, (3, 3), 0)
            edges = cv2.Canny(blurred_frame,30,110)
            
        ##############DIRT ALGORITHM#####################################################   
            #blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
           # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            kernel = np.ones((50,50),np.uint8)
            #kernel = np.ones((31,31),np.uint8)
            
           # imag = cv2.medianBlur(frame, 7)

           # Int = imag[:,:,0]
            
            imag2 = cv2.medianBlur(frame, 3)

            Int2 = imag2[:,:,0]
            
            #opening = cv2.morphologyEx(Int, cv2.MORPH_OPEN, kernel)
            th2 = cv2.adaptiveThreshold(Int2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
            opening2 = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)
            
        ######################################################################## 
            # target contours
            #targets = []
            
            
 
            _, contours1, _ = cv2.findContours(edges , cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            _, contours2, _ = cv2.findContours(opening2 , cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            
            ##########contour1#############
            for contour in contours1:
                
                x,y,w,h = cv2.boundingRect(contour)
                area = cv2.contourArea(contour)
                cv2.drawContours(frame, contour, -1, (0, 0, 255), 1)
                #cv2.putText(frame, 'Dirt/Crack found', (x, y), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 255),1)     
                
                
            ##contour2 ##########  ########
            count_good = 0
            count_total = 30
            for contour2 in contours2:
                count_good +=1
                x,y,w,h = cv2.boundingRect(contour2)
                area = cv2.contourArea(contour2)
                cv2.putText(frame, 'Dirt/Crack Condition: GOOD', (x, y), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0),1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        
   
                

                    
            
            #############RESULT####################
            count_bad = count_total - count_good
 
            goodresult = 'Total eggs GOOD condition:'+str(count_good)  
            badresult  = 'Total eggs BAD condition:'+str(count_bad)
            
            
            cv2.putText(frame, 'Total eggs in GOOD condition:'+str(count_good), (10, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 255, 50),2)
            cv2.putText(frame, 'Total eggs in BAD condition:'+str(count_bad), (10, 590), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 50, 255),2)
            
            #cv2.imshow("mask",opening2)
        
            cv2.imshow("External Egg: Crack and Dirt Detection", frame)    
            ###################SAVING AND EXIT#####################

            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                
                mixer.init()
                mixer.music.load("trainedvoice_dataset/stop.mp3")
                mixer.music.play()
                QMessageBox.critical(OtherWindow,"",'Egg Detection Terminated')
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                break
                
            elif cv2.waitKey(33) == ord('s'):
                mixer.init()
                mixer.music.load("trainedvoice_dataset/save1.mp3")
                mixer.music.play()
                img_EXname = "Results/ExternalCrackDirtScannedEggs_{}.png".format(img_counter)
                cv2.imwrite(img_EXname, frame)
                QMessageBox.information(OtherWindow,"Result", '<EGG DETECTION RESULT SAVED>         %s                           %s' %(goodresult,badresult) )
                print("{} saved!".format(img_EXname))
       
                img_counter += 1

        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.waitKey(1)
        cv2.waitKey(1)




    ####################TURN OFF##########################################
    def Stop(self):
        
 

        OtherWindow = QtWidgets.QMainWindow()
        mixer.init()
        mixer.music.load("trainedvoice_dataset/shutdown.mp3")
        mixer.music.play()
        QMessageBox.critical(OtherWindow,'SHUTTING DOWN','EggIE will now shutdown the system. Thank you and  have a good day!')
        app.quit()

        






import src1

if __name__ == "__main__":
    import sys
   
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

