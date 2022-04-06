# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(5, 5, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.taskScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskScrollArea.sizePolicy().hasHeightForWidth())
        self.taskScrollArea.setSizePolicy(sizePolicy)
        self.taskScrollArea.setMinimumSize(QtCore.QSize(150, 0))
        self.taskScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taskScrollArea.setWidgetResizable(True)
        self.taskScrollArea.setObjectName("taskScrollArea")
        self.taskScrollContents = QtWidgets.QWidget()
        self.taskScrollContents.setGeometry(QtCore.QRect(0, 0, 150, 335))
        self.taskScrollContents.setObjectName("taskScrollContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.taskScrollContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.taskScrollArea.setWidget(self.taskScrollContents)
        self.gridLayout.addWidget(self.taskScrollArea, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.taskInfoScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.taskInfoScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taskInfoScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.taskInfoScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.taskInfoScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.taskInfoScrollArea.setWidgetResizable(True)
        self.taskInfoScrollArea.setObjectName("taskInfoScrollArea")
        self.taskInfoScrollContents = QtWidgets.QWidget()
        self.taskInfoScrollContents.setGeometry(QtCore.QRect(0, 0, 402, 335))
        self.taskInfoScrollContents.setObjectName("taskInfoScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.taskInfoScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.taskTitle = QtWidgets.QLabel(self.taskInfoScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskTitle.sizePolicy().hasHeightForWidth())
        self.taskTitle.setSizePolicy(sizePolicy)
        self.taskTitle.setObjectName("taskTitle")
        self.verticalLayout_2.addWidget(self.taskTitle)
        self.taskDescription = QtWidgets.QLabel(self.taskInfoScrollContents)
        self.taskDescription.setWordWrap(True)
        self.taskDescription.setObjectName("taskDescription")
        self.verticalLayout_2.addWidget(self.taskDescription)
        self.markAsDoneButton = QtWidgets.QPushButton(self.taskInfoScrollContents)
        self.markAsDoneButton.setObjectName("markAsDoneButton")
        self.verticalLayout_2.addWidget(self.markAsDoneButton)
        self.taskInfoScrollArea.setWidget(self.taskInfoScrollContents)
        self.gridLayout.addWidget(self.taskInfoScrollArea, 3, 1, 1, 1)
        self.orgLabel = QtWidgets.QLabel(self.centralwidget)
        self.orgLabel.setObjectName("orgLabel")
        self.gridLayout.addWidget(self.orgLabel, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 22))
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
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.taskTitle.setText(_translate("MainWindow", "TextLabel"))
        self.taskDescription.setText(_translate("MainWindow", "TextLabel"))
        self.markAsDoneButton.setText(_translate("MainWindow", "Mark as done"))
        self.orgLabel.setText(_translate("MainWindow", "Org"))
