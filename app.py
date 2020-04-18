import sys
import time
import random
from aip import AipOcr

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtSql import QSqlQuery,QSqlDatabase

from Ui_ocrui import Ui_MainWindow
# from configDialog import Ui_Dialog #暂时未使用

APP_ID = '19105187'   #APP_ID
API_KEY = 'IywiicFEKa5ny2ckUp29tHVk'  #API_KEY
SECRET_KEY =  'uWnu44pu6lFjPZylFLMBymurGNTtrD2t'  #SECRET_KEY
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {
            'detect_direction': 'true',
            'language_type': 'CHN_ENG',
        }


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.text = ""
        self.strTime = ""
        self.basicid = ""
        self.filePath = ""

    def loadImage(self):
        self.filePath,_ = QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.png *.jpg *.jpeg)')
        self.jpg = QtGui.QPixmap(self.filePath).scaled(self.plabel.width(), self.plabel.height())
        self.plabel.setPixmap(self.jpg)

    def recognize(self):
        if(self.filePath == ""):
            print(QMessageBox.warning(self, "错误", "没有找到图片", QMessageBox.Yes, QMessageBox.Yes))
            return

        result = aipOcr.basicAccurate(self.get_file_content(self.filePath), options)
        words_result = result['words_result']
        for i in range(len(words_result)):
            self.text = self.text + words_result[i]['words'] +'\n'
            
        self.tedit.setPlainText(self.text)
        self.tedit.repaint()    # 解决mac端文本无法显示的问题

        self.text = ''

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
            
    def cleanText(self):
        self.tedit.repaint()    # 解决mac端文本无法显示的问题

    def configApi(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())