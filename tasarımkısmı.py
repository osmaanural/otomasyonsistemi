# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 835)
        MainWindow.setMinimumSize(QtCore.QSize(1012, 835))
        MainWindow.setMaximumSize(QtCore.QSize(1012, 835))
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setMidLineWidth(2)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 140, 261, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 30, 81, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(110, 30, 141, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ad = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ad.setFont(font)
        self.ad.setObjectName("ad")
        self.verticalLayout_2.addWidget(self.ad)
        self.soyad = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.soyad.setFont(font)
        self.soyad.setObjectName("soyad")
        self.verticalLayout_2.addWidget(self.soyad)
        self.tc = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tc.setFont(font)
        self.tc.setObjectName("tc")
        self.verticalLayout_2.addWidget(self.tc)
        self.cinsiyet = QtWidgets.QGroupBox(self.centralwidget)
        self.cinsiyet.setGeometry(QtCore.QRect(30, 340, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cinsiyet.setFont(font)
        self.cinsiyet.setFlat(False)
        self.cinsiyet.setCheckable(False)
        self.cinsiyet.setObjectName("cinsiyet")
        self.erkek = QtWidgets.QRadioButton(self.cinsiyet)
        self.erkek.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.erkek.setObjectName("erkek")
        self.kadin = QtWidgets.QRadioButton(self.cinsiyet)
        self.kadin.setGeometry(QtCore.QRect(130, 40, 95, 20))
        self.kadin.setObjectName("kadin")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 140, 261, 81))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 141, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.dogumyeri = QtWidgets.QComboBox(self.frame_2)
        self.dogumyeri.setGeometry(QtCore.QRect(40, 40, 181, 22))
        self.dogumyeri.setObjectName("dogumyeri")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(320, 230, 261, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(90, 0, 81, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.bolum = QtWidgets.QComboBox(self.frame_3)
        self.bolum.setGeometry(QtCore.QRect(40, 40, 181, 22))
        self.bolum.setObjectName("bolum")
        self.egitimturu = QtWidgets.QGroupBox(self.centralwidget)
        self.egitimturu.setGeometry(QtCore.QRect(310, 340, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.egitimturu.setFont(font)
        self.egitimturu.setFlat(False)
        self.egitimturu.setCheckable(False)
        self.egitimturu.setObjectName("egitimturu")
        self.orgun = QtWidgets.QRadioButton(self.egitimturu)
        self.orgun.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.orgun.setObjectName("orgun")
        self.io = QtWidgets.QRadioButton(self.egitimturu)
        self.io.setGeometry(QtCore.QRect(140, 40, 131, 20))
        self.io.setObjectName("io")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(610, 140, 371, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(110, 10, 151, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dogumtarihi = QtWidgets.QCalendarWidget(self.centralwidget)
        self.dogumtarihi.setGeometry(QtCore.QRect(610, 200, 371, 221))
        self.dogumtarihi.setObjectName("dogumtarihi")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 460, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.kayitekle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kayitekle.setFont(font)
        self.kayitekle.setObjectName("kayitekle")
        self.horizontalLayout.addWidget(self.kayitekle)
        self.kayitsil = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kayitsil.setFont(font)
        self.kayitsil.setObjectName("kayitsil")
        self.horizontalLayout.addWidget(self.kayitsil)
        self.kaytekrani = QtWidgets.QTableWidget(self.centralwidget)
        self.kaytekrani.setGeometry(QtCore.QRect(30, 530, 921, 241))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kaytekrani.setFont(font)
        self.kaytekrani.setShowGrid(True)
        self.kaytekrani.setGridStyle(QtCore.Qt.SolidLine)
        self.kaytekrani.setRowCount(1)
        self.kaytekrani.setColumnCount(8)
        self.kaytekrani.setObjectName("kaytekrani")
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaytekrani.setHorizontalHeaderItem(7, item)
        self.kaytekrani.horizontalHeader().setDefaultSectionSize(108)
        self.kaytekrani.horizontalHeader().setHighlightSections(False)
        self.kaytekrani.horizontalHeader().setMinimumSectionSize(66)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/osmaa/OneDrive/Masaüstü/5.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.ad.raise_()
        self.soyad.raise_()
        self.frame.raise_()
        self.cinsiyet.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.egitimturu.raise_()
        self.frame_4.raise_()
        self.dogumtarihi.raise_()
        self.horizontalLayoutWidget.raise_()
        self.kaytekrani.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "ÖĞRENCİ KAYIT SİSTEMİ"))
        self.label_3.setText(_translate("MainWindow", "AD:"))
        self.label_4.setText(_translate("MainWindow", "SOYAD:"))
        self.label_5.setText(_translate("MainWindow", "TC:"))
        self.cinsiyet.setTitle(_translate("MainWindow", "CİNSİYET"))
        self.erkek.setText(_translate("MainWindow", "ERKEK"))
        self.kadin.setText(_translate("MainWindow", "KADIN"))
        self.label_6.setText(_translate("MainWindow", "DOĞUM YERİ:"))
        self.label_7.setText(_translate("MainWindow", "BÖLÜM:"))
        self.egitimturu.setTitle(_translate("MainWindow", "EĞİTİM TÜRÜ"))
        self.orgun.setText(_translate("MainWindow", "ÖRGÜN"))
        self.io.setText(_translate("MainWindow", "İÖ"))
        self.label_8.setText(_translate("MainWindow", "DOĞUM TARİHİ"))
        self.kayitekle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.kayitsil.setText(_translate("MainWindow", "KAYIT SİL"))
        item = self.kaytekrani.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ad"))
        item = self.kaytekrani.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Soyad"))
        item = self.kaytekrani.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tc.No"))
        item = self.kaytekrani.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cinsiyet"))
        item = self.kaytekrani.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Doğum Yeri"))
        item = self.kaytekrani.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Doğum Tarih"))
        item = self.kaytekrani.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Bölüm"))
        item = self.kaytekrani.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Eğitim Türü"))
