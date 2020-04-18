# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/EIthschnapps/Documents/git/playground/ocr_pyqt5/ocrui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.opt = QtWidgets.QPushButton(self.layoutWidget)
        self.opt.setObjectName("opt")
        self.verticalLayout.addWidget(self.opt)
        self.start = QtWidgets.QPushButton(self.layoutWidget)
        self.start.setObjectName("start")
        self.verticalLayout.addWidget(self.start)
        self.plabel = QtWidgets.QLabel(self.layoutWidget)
        self.plabel.setEnabled(True)
        self.plabel.setMinimumSize(QtCore.QSize(100, 100))
        self.plabel.setMaximumSize(QtCore.QSize(100, 100))
        self.plabel.setText("")
        self.plabel.setObjectName("plabel")
        self.verticalLayout.addWidget(self.plabel)
        self.clean = QtWidgets.QPushButton(self.layoutWidget)
        self.clean.setObjectName("clean")
        self.verticalLayout.addWidget(self.clean)
        self.config = QtWidgets.QPushButton(self.layoutWidget)
        self.config.setObjectName("config")
        self.verticalLayout.addWidget(self.config)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tedit = QtWidgets.QTextEdit(self.layoutWidget)
        self.tedit.setObjectName("tedit")
        self.horizontalLayout.addWidget(self.tedit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.opt.clicked.connect(MainWindow.loadImage)
        self.start.clicked.connect(MainWindow.recognize)
        self.config.clicked.connect(MainWindow.configApi)
        self.clean.clicked.connect(self.tedit.clear)
        self.clean.clicked.connect(self.plabel.clear)
        self.clean.clicked.connect(MainWindow.cleanText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My OCR"))
        self.opt.setText(_translate("MainWindow", "选择图片"))
        self.start.setText(_translate("MainWindow", "开始识别"))
        self.clean.setText(_translate("MainWindow", "清空"))
        self.config.setText(_translate("MainWindow", "配置API Key"))
        self.menufile.setTitle(_translate("MainWindow", "file"))

