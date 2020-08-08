import sys
import socket
import os, json, urllib.request
import clipboard
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PIL import ImageGrab
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy

 


form_class = uic.loadUiType("webEngineViewTest.ui")[0]
whois_key = '2019111811330574298381'




class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10
        

        #WebEngineView의 시그널
        self.webEngineView_Test.loadStarted.connect(self.printLoadStart)
        self.webEngineView_Test.loadProgress.connect(self.printLoading)
        self.webEngineView_Test.loadFinished.connect(self.printLoadFinished)
        self.webEngineView_Test.urlChanged.connect(self.urlChangedFunction)

        #버튼들에 기능을 연결
        self.btn_setUrl.clicked.connect(self.urlGo)
        self.pushButton.clicked.connect(self.changeGO)
        self.pushButton_2.clicked.connect(self.clip)
        self.pushButton_3.clicked.connect(self.scre)
        self.pushButton_4.clicked.connect(self.copyip)
        #변환
        self.pushButton.setShortcut("F1")
        #복사
        self.pushButton_2.setShortcut("F3")
        #아이피 복사
        self.pushButton_4.setShortcut("F2")
        #스크린샷
        self.pushButton_3.setShortcut("F4")
        #pyautogui.screenshot('test2.png', region=(0, 0, 200, 200))
        

    #WebEngineView의 시그널에 연결된 함수들
    def printLoadStart(self) : print("Start Loading")
    def printLoading(self) : print("Loading")
    def printLoadFinished(self) : print("Load Finished")

    #url 이동
    def urlChangedFunction(self) :
        self.line_url.setText(self.webEngineView_Test.url().toString())
        print("Url Changed")

    #버튼을 눌렀을 때 실행될 함수들
    def urlGo(self) :
        self.webEngineView_Test.load(QUrl(self.line_url.text()))

    #whois 이동
    def changeGO(self) :
        #print(self.textEdit.toPlainText())
        addr1 = socket.gethostbyname(self.textEdit.toPlainText())
        #print(addr1)
        query = "http://whois.kisa.or.kr/openapi/whois.jsp?query=" + addr1 + "&key="+ whois_key + "&answer=json"
        request = urllib.request.urlopen(query).read().decode("utf-8")
        dict = json.loads(str(request))
        hop = (self.textEdit.toPlainText() +'\t' + str(addr1) + '\t' + str(dict['whois']['countryCode']))
        self.textBrowser_2.setPlainText(hop)
        a = self.textBrowser_2.toPlainText()

    #전체복사
    def clip(self) :
        clipboard.copy(self.textBrowser_2.toPlainText())
        #clipboard.copy(self.textBrowser_2.setPlainText(hop))
        #print(str(hop))
    
    #아이피복사
    def copyip(self) :
        addr1 = socket.gethostbyname(self.textEdit.toPlainText())
        print(addr1)
        self.textBrowser_3.setPlainText(addr1)
        clipboard.copy(self.textBrowser_3.toPlainText())
        #print(self.textBrowser_3.setPlainText(addr1))
    
    #스크린샷
    def scre(self, event) :
        
        ix, iy = -1, -1
        imgGrab = ImageGrab.grab(bbox=(480, 100, 1170, 724))
        cv_img = cv2.cvtColor(numpy.array(imgGrab), cv2.COLOR_RGB2BGR)
        draw = cv_img
        def draw_circle(event, x, y, flags, param):
            global ix, iy, drawing, mode
            drawing = False  # True 이면 마우스가 눌린 상태입니다.
            mode = True  # True이면 사각형을 그립니다. 'm'을 누르면 곡선으로 변경(토글)됩니다
            if event == cv2.EVENT_LBUTTONDOWN:
                drawing = True
                ix, iy = x, y
            elif event == cv2.EVENT_LBUTTONUP:
                drawing = False
                if mode == True:
                    cv2.rectangle(cv_img, (ix, iy), (x, y), (0, 0, 255), True)
                else:
                    cv2.circle(cv_img, (x, y), 5, (0, 0, 255), -1)

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_circle)
        while (1):
            drawing = False  # True 이면 마우스가 눌린 상태입니다.
            mode = True  # True이면 사각형을 그립니다. 'm'을 누르면 곡선으로 변경(토글)됩니다
            cv2.imshow('image', cv_img)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                mode = not mode
            elif k == 27:
                break

        cv2.destroyAllWindows()
        #
        
            


#마우스


#색깔
        

#------------------------------


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

'''
ax = plt.gca()

rect = patches.Rectangle((80,10),
            70,
            100,
            linewidth=2,
            edgecolor='red',
            fill = False)

ax.add_patch(rect)

plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
'''