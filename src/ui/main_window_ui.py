# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_files/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(5, 5, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.taskInfoScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.taskInfoScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taskInfoScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.taskInfoScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.taskInfoScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.taskInfoScrollArea.setWidgetResizable(True)
        self.taskInfoScrollArea.setObjectName("taskInfoScrollArea")
        self.taskInfoScrollContents = QtWidgets.QWidget()
        self.taskInfoScrollContents.setGeometry(QtCore.QRect(0, 0, 455, 431))
        self.taskInfoScrollContents.setObjectName("taskInfoScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.taskInfoScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.taskTitle = QtWidgets.QLabel(self.taskInfoScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskTitle.sizePolicy().hasHeightForWidth())
        self.taskTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.taskTitle.setFont(font)
        self.taskTitle.setObjectName("taskTitle")
        self.verticalLayout_2.addWidget(self.taskTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.assignInfo = QtWidgets.QLabel(self.taskInfoScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.assignInfo.sizePolicy().hasHeightForWidth())
        self.assignInfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.assignInfo.setFont(font)
        self.assignInfo.setObjectName("assignInfo")
        self.verticalLayout_2.addWidget(self.assignInfo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.assignedDate = QtWidgets.QLabel(self.taskInfoScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assignedDate.sizePolicy().hasHeightForWidth())
        self.assignedDate.setSizePolicy(sizePolicy)
        self.assignedDate.setObjectName("assignedDate")
        self.verticalLayout_2.addWidget(self.assignedDate)
        self.doneDate = QtWidgets.QLabel(self.taskInfoScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doneDate.sizePolicy().hasHeightForWidth())
        self.doneDate.setSizePolicy(sizePolicy)
        self.doneDate.setObjectName("doneDate")
        self.verticalLayout_2.addWidget(self.doneDate)
        self.line_2 = QtWidgets.QFrame(self.taskInfoScrollContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.taskDescription = QtWidgets.QLabel(self.taskInfoScrollContents)
        self.taskDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.taskDescription.setWordWrap(True)
        self.taskDescription.setObjectName("taskDescription")
        self.verticalLayout_2.addWidget(self.taskDescription)
        self.markAsDoneButton = QtWidgets.QPushButton(self.taskInfoScrollContents)
        self.markAsDoneButton.setObjectName("markAsDoneButton")
        self.verticalLayout_2.addWidget(self.markAsDoneButton)
        self.taskInfoScrollArea.setWidget(self.taskInfoScrollContents)
        self.gridLayout.addWidget(self.taskInfoScrollArea, 2, 2, 2, 1)
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.orgLabel = QtWidgets.QLabel(self.centralwidget)
        self.orgLabel.setObjectName("orgLabel")
        self.gridLayout.addWidget(self.orgLabel, 1, 0, 1, 1)
        self.taskScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskScrollArea.sizePolicy().hasHeightForWidth())
        self.taskScrollArea.setSizePolicy(sizePolicy)
        self.taskScrollArea.setMinimumSize(QtCore.QSize(175, 0))
        self.taskScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taskScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.taskScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.taskScrollArea.setWidgetResizable(True)
        self.taskScrollArea.setObjectName("taskScrollArea")
        self.taskScrollContents = QtWidgets.QWidget()
        self.taskScrollContents.setGeometry(QtCore.QRect(0, 0, 161, 411))
        self.taskScrollContents.setObjectName("taskScrollContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.taskScrollContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.taskScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(161, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.taskScrollArea.setWidget(self.taskScrollContents)
        self.gridLayout.addWidget(self.taskScrollArea, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(0, 50))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 22))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        self.menuTasks = QtWidgets.QMenu(self.menubar)
        self.menuTasks.setObjectName("menuTasks")
        self.menuOrganizations = QtWidgets.QMenu(self.menubar)
        self.menuOrganizations.setObjectName("menuOrganizations")
        self.menuChange_current_organization = QtWidgets.QMenu(self.menuOrganizations)
        self.menuChange_current_organization.setObjectName("menuChange_current_organization")
        self.menuAssign_a_member_as_admin = QtWidgets.QMenu(self.menuOrganizations)
        self.menuAssign_a_member_as_admin.setEnabled(False)
        self.menuAssign_a_member_as_admin.setObjectName("menuAssign_a_member_as_admin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSign_out = QtWidgets.QAction(MainWindow)
        self.actionSign_out.setEnabled(True)
        self.actionSign_out.setObjectName("actionSign_out")
        self.actionAssign_a_new_task = QtWidgets.QAction(MainWindow)
        self.actionAssign_a_new_task.setEnabled(False)
        self.actionAssign_a_new_task.setObjectName("actionAssign_a_new_task")
        self.actionJoin_organization_or_create_a_new_one = QtWidgets.QAction(MainWindow)
        self.actionJoin_organization_or_create_a_new_one.setObjectName("actionJoin_organization_or_create_a_new_one")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionTest_2 = QtWidgets.QAction(MainWindow)
        self.actionTest_2.setObjectName("actionTest_2")
        self.menuAccount.addAction(self.actionSign_out)
        self.menuTasks.addAction(self.actionAssign_a_new_task)
        self.menuChange_current_organization.addAction(self.actionTest)
        self.menuAssign_a_member_as_admin.addAction(self.actionTest_2)
        self.menuOrganizations.addAction(self.actionJoin_organization_or_create_a_new_one)
        self.menuOrganizations.addSeparator()
        self.menuOrganizations.addAction(self.menuChange_current_organization.menuAction())
        self.menuOrganizations.addSeparator()
        self.menuOrganizations.addAction(self.menuAssign_a_member_as_admin.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())
        self.menubar.addAction(self.menuOrganizations.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.taskTitle.setText(_translate("MainWindow", "TaskTitle"))
        self.assignInfo.setText(_translate("MainWindow", "AssignInfo"))
        self.assignedDate.setText(_translate("MainWindow", "AssignedDate"))
        self.doneDate.setText(_translate("MainWindow", "DoneDate"))
        self.taskDescription.setText(_translate("MainWindow", "TextLabel"))
        self.markAsDoneButton.setText(_translate("MainWindow", "Mark as done"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.orgLabel.setText(_translate("MainWindow", "Org"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.menuTasks.setTitle(_translate("MainWindow", "Tasks"))
        self.menuOrganizations.setTitle(_translate("MainWindow", "Organizations"))
        self.menuChange_current_organization.setTitle(_translate("MainWindow", "Change current organization"))
        self.menuAssign_a_member_as_admin.setTitle(_translate("MainWindow", "Assign a member as admin"))
        self.actionSign_out.setText(_translate("MainWindow", "Sign out"))
        self.actionAssign_a_new_task.setText(_translate("MainWindow", "Assign a new task"))
        self.actionAssign_a_new_task.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionJoin_organization_or_create_a_new_one.setText(_translate("MainWindow", "Join organization or create a new one"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionTest_2.setText(_translate("MainWindow", "Test"))
