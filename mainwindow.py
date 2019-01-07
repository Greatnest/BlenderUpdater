# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Fri Aug  3 15:34:51 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 550))
        MainWindow.setMaximumSize(QtCore.QSize(700, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/appicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Back.setGeometry(QtCore.QRect(6, 481, 131, 35))
        self.btn_Back.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Back.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/images/Actions-arrow-left-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Back.setIcon(icon1)
        self.btn_Back.setObjectName("btn_Back")
        self.btn_Check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Check.setGeometry(QtCore.QRect(560, 481, 131, 35))
        self.btn_Check.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/images/Refresh-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Check.setIcon(icon2)
        self.btn_Check.setAutoDefault(False)
        self.btn_Check.setDefault(False)
        self.btn_Check.setObjectName("btn_Check")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(140, 431, 551, 30))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.lbl_task = QtWidgets.QLabel(self.centralwidget)
        self.lbl_task.setGeometry(QtCore.QRect(10, 435, 121, 20))
        self.lbl_task.setStyleSheet("")
        self.lbl_task.setObjectName("lbl_task")
        self.lbl_available = QtWidgets.QLabel(self.centralwidget)
        self.lbl_available.setGeometry(QtCore.QRect(6, 25, 645, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbl_available.setFont(font)
        self.lbl_available.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_available.setObjectName("lbl_available")
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(657, 10, 35, 35))
        self.btn_about.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/images/Information-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon3)
        self.btn_about.setIconSize(QtCore.QSize(24, 24))
        self.btn_about.setCheckable(False)
        self.btn_about.setChecked(False)
        self.btn_about.setObjectName("btn_about")
        self.frm_start = QtWidgets.QFrame(self.centralwidget)
        self.frm_start.setGeometry(QtCore.QRect(6, 50, 686, 271))
        self.frm_start.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_start.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_start.setObjectName("frm_start")
        self.lbl_start = QtWidgets.QLabel(self.frm_start)
        self.lbl_start.setGeometry(QtCore.QRect(90, 70, 491, 41))
        self.lbl_start.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_start.setWordWrap(True)
        self.lbl_start.setObjectName("lbl_start")
        self.line_path = QtWidgets.QLineEdit(self.frm_start)
        self.line_path.setGeometry(QtCore.QRect(80, 160, 491, 35))
        self.line_path.setObjectName("line_path")
        self.btn_path = QtWidgets.QPushButton(self.frm_start)
        self.btn_path.setGeometry(QtCore.QRect(576, 160, 35, 35))
        self.btn_path.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/images/Open-folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_path.setIcon(icon4)
        self.btn_path.setObjectName("btn_path")
        self.label = QtWidgets.QLabel(self.frm_start)
        self.label.setGeometry(QtCore.QRect(190, 130, 311, 20))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(110, 435, 24, 24))
        self.btn_cancel.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/images/Cancel-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon5)
        self.btn_cancel.setObjectName("btn_cancel")
        self.frm_progress = QtWidgets.QFrame(self.centralwidget)
        self.frm_progress.setGeometry(QtCore.QRect(6, 50, 686, 251))
        self.frm_progress.setStyleSheet("")
        self.frm_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_progress.setObjectName("frm_progress")
        self.lbl_download_pic = QtWidgets.QLabel(self.frm_progress)
        self.lbl_download_pic.setGeometry(QtCore.QRect(40, 50, 24, 24))
        self.lbl_download_pic.setText("")
        self.lbl_download_pic.setObjectName("lbl_download_pic")
        self.lbl_extract_pic = QtWidgets.QLabel(self.frm_progress)
        self.lbl_extract_pic.setGeometry(QtCore.QRect(40, 80, 24, 24))
        self.lbl_extract_pic.setText("")
        self.lbl_extract_pic.setObjectName("lbl_extract_pic")
        self.lbl_copy_pic = QtWidgets.QLabel(self.frm_progress)
        self.lbl_copy_pic.setGeometry(QtCore.QRect(40, 110, 24, 24))
        self.lbl_copy_pic.setText("")
        self.lbl_copy_pic.setObjectName("lbl_copy_pic")
        self.lbl_downloading = QtWidgets.QLabel(self.frm_progress)
        self.lbl_downloading.setGeometry(QtCore.QRect(70, 50, 561, 24))
        self.lbl_downloading.setStyleSheet("")
        self.lbl_downloading.setObjectName("lbl_downloading")
        self.lbl_extraction = QtWidgets.QLabel(self.frm_progress)
        self.lbl_extraction.setGeometry(QtCore.QRect(70, 80, 221, 24))
        self.lbl_extraction.setObjectName("lbl_extraction")
        self.lbl_copying = QtWidgets.QLabel(self.frm_progress)
        self.lbl_copying.setGeometry(QtCore.QRect(70, 110, 181, 24))
        self.lbl_copying.setObjectName("lbl_copying")
        self.lbl_clean_pic = QtWidgets.QLabel(self.frm_progress)
        self.lbl_clean_pic.setGeometry(QtCore.QRect(40, 140, 24, 24))
        self.lbl_clean_pic.setText("")
        self.lbl_clean_pic.setObjectName("lbl_clean_pic")
        self.lbl_cleanup = QtWidgets.QLabel(self.frm_progress)
        self.lbl_cleanup.setGeometry(QtCore.QRect(70, 140, 171, 24))
        self.lbl_cleanup.setObjectName("lbl_cleanup")
        self.btngrp_filter = QtWidgets.QGroupBox(self.centralwidget)
        self.btngrp_filter.setGeometry(QtCore.QRect(200, 455, 307, 61))
        self.btngrp_filter.setObjectName("btngrp_filter")
        self.btn_osx = QtWidgets.QPushButton(self.btngrp_filter)
        self.btn_osx.setGeometry(QtCore.QRect(227, 30, 75, 23))
        self.btn_osx.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/images/Apple-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_osx.setIcon(icon6)
        self.btn_osx.setCheckable(True)
        self.btn_osx.setAutoExclusive(True)
        self.btn_osx.setObjectName("btn_osx")
        self.btn_windows = QtWidgets.QPushButton(self.btngrp_filter)
        self.btn_windows.setGeometry(QtCore.QRect(79, 30, 75, 23))
        self.btn_windows.setAutoFillBackground(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/images/Windows-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_windows.setIcon(icon7)
        self.btn_windows.setCheckable(True)
        self.btn_windows.setAutoExclusive(True)
        self.btn_windows.setFlat(False)
        self.btn_windows.setObjectName("btn_windows")
        self.btn_allos = QtWidgets.QPushButton(self.btngrp_filter)
        self.btn_allos.setGeometry(QtCore.QRect(5, 30, 75, 23))
        self.btn_allos.setStyleSheet("")
        self.btn_allos.setCheckable(True)
        self.btn_allos.setChecked(True)
        self.btn_allos.setAutoExclusive(True)
        self.btn_allos.setObjectName("btn_allos")
        self.btn_linux = QtWidgets.QPushButton(self.btngrp_filter)
        self.btn_linux.setGeometry(QtCore.QRect(153, 30, 75, 23))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/images/Linux-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_linux.setIcon(icon8)
        self.btn_linux.setCheckable(True)
        self.btn_linux.setAutoExclusive(True)
        self.btn_linux.setObjectName("btn_linux")
        self.btn_oneclick = QtWidgets.QPushButton(self.centralwidget)
        self.btn_oneclick.setGeometry(QtCore.QRect(260, 480, 191, 35))
        self.btn_oneclick.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/images/Actions-quickopen-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_oneclick.setIcon(icon9)
        self.btn_oneclick.setObjectName("btn_oneclick")
        self.lbl_quick = QtWidgets.QLabel(self.centralwidget)
        self.lbl_quick.setGeometry(QtCore.QRect(290, 460, 131, 20))
        self.lbl_quick.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_quick.setObjectName("lbl_quick")
        self.lbl_caution = QtWidgets.QLabel(self.centralwidget)
        self.lbl_caution.setGeometry(QtCore.QRect(6, 3, 645, 20))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbl_caution.setFont(font)
        self.lbl_caution.setAutoFillBackground(True)
        self.lbl_caution.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_caution.setObjectName("lbl_caution")
        self.btn_newVersion = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newVersion.setGeometry(QtCore.QRect(500, 10, 151, 35))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/images/software-update-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_newVersion.setIcon(icon10)
        self.btn_newVersion.setIconSize(QtCore.QSize(24, 24))
        self.btn_newVersion.setCheckable(False)
        self.btn_newVersion.setChecked(False)
        self.btn_newVersion.setObjectName("btn_newVersion")
        self.btn_execute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_execute.setGeometry(QtCore.QRect(260, 480, 191, 35))
        self.btn_execute.setStyleSheet("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/images/Blender-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_execute.setIcon(icon11)
        self.btn_execute.setObjectName("btn_execute")
               
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Overmind Studios BlenderUpdater", None, -1))
        self.btn_Back.setText(QtWidgets.QApplication.translate("MainWindow", "Back", None, -1))
        self.btn_Check.setText(QtWidgets.QApplication.translate("MainWindow", "Version Check", None, -1))
        self.lbl_task.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lbl_available.setText(QtWidgets.QApplication.translate("MainWindow", "Available versions from buildbot:", None, -1))
        self.btn_about.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.lbl_start.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Press &quot;Version Check&quot; to get a list of the most current buildbot versions.</p></body></html>", None, -1))
        self.line_path.setText(QtWidgets.QApplication.translate("MainWindow", "not set", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Choose path (must be an existing folder):", None, -1))
        self.lbl_downloading.setText(QtWidgets.QApplication.translate("MainWindow", "Downloading", None, -1))
        self.lbl_extraction.setText(QtWidgets.QApplication.translate("MainWindow", "Extraction", None, -1))
        self.lbl_copying.setText(QtWidgets.QApplication.translate("MainWindow", "Copying files", None, -1))
        self.lbl_cleanup.setText(QtWidgets.QApplication.translate("MainWindow", "Cleaning up", None, -1))
        self.btngrp_filter.setTitle(QtWidgets.QApplication.translate("MainWindow", "Filter results", None, -1))
        self.btn_osx.setText(QtWidgets.QApplication.translate("MainWindow", "OSX", None, -1))
        self.btn_windows.setText(QtWidgets.QApplication.translate("MainWindow", "Windows", None, -1))
        self.btn_allos.setText(QtWidgets.QApplication.translate("MainWindow", "all OS", None, -1))
        self.btn_linux.setText(QtWidgets.QApplication.translate("MainWindow", "Linux", None, -1))
        self.btn_oneclick.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Use last used settings to update blender. Uses the path in the above text field and specified version on the button.", None, -1))
        self.btn_oneclick.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.lbl_quick.setText(QtWidgets.QApplication.translate("MainWindow", "Quick Update", None, -1))
        self.lbl_caution.setText(QtWidgets.QApplication.translate("MainWindow", " These builds are not as stable as releases, use at your own risk.", None, -1))
        self.btn_newVersion.setToolTip(QtWidgets.QApplication.translate("MainWindow", "New version available", None, -1))
        self.btn_newVersion.setText(QtWidgets.QApplication.translate("MainWindow", "New version available", None, -1))
        self.btn_execute.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Run downloaded Blender version", None, -1))
        self.btn_execute.setText(QtWidgets.QApplication.translate("MainWindow", "Run Blender", None, -1))

import res_rc
