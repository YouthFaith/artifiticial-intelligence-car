# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Windows(object):
    def setupUi(self, Main_Windows):
        Main_Windows.setObjectName("Main_Windows")
        Main_Windows.resize(485, 407)
        font = QtGui.QFont()
        font.setPointSize(12)
        Main_Windows.setFont(font)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Main_Windows)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.video = QtWidgets.QLabel(Main_Windows)
        self.video.setMinimumSize(QtCore.QSize(200, 200))
        self.video.setMaximumSize(QtCore.QSize(200, 200))
        self.video.setText("")
        self.video.setObjectName("video")
        self.horizontalLayout_7.addWidget(self.video)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Main_Windows)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Main_Windows)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.current_speed = QtWidgets.QLabel(Main_Windows)
        self.current_speed.setMinimumSize(QtCore.QSize(80, 0))
        self.current_speed.setMaximumSize(QtCore.QSize(80, 100))
        self.current_speed.setObjectName("current_speed")
        self.horizontalLayout.addWidget(self.current_speed)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Main_Windows)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.barrier_distance = QtWidgets.QLabel(Main_Windows)
        self.barrier_distance.setMinimumSize(QtCore.QSize(80, 0))
        self.barrier_distance.setMaximumSize(QtCore.QSize(80, 100))
        self.barrier_distance.setObjectName("barrier_distance")
        self.horizontalLayout_2.addWidget(self.barrier_distance)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.manual_driver = QtWidgets.QRadioButton(Main_Windows)
        self.manual_driver.setMinimumSize(QtCore.QSize(0, 20))
        self.manual_driver.setMaximumSize(QtCore.QSize(16777215, 20))
        self.manual_driver.setChecked(True)
        self.manual_driver.setObjectName("manual_driver")
        self.verticalLayout_2.addWidget(self.manual_driver)
        self.automatic_tracing = QtWidgets.QRadioButton(Main_Windows)
        self.automatic_tracing.setMinimumSize(QtCore.QSize(0, 20))
        self.automatic_tracing.setMaximumSize(QtCore.QSize(16777215, 20))
        self.automatic_tracing.setObjectName("automatic_tracing")
        self.verticalLayout_2.addWidget(self.automatic_tracing)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)
        self.LEVEL_1 = QtWidgets.QRadioButton(Main_Windows)
        self.LEVEL_1.setChecked(True)
        self.LEVEL_1.setObjectName("LEVEL_1")
        self.verticalLayout_5.addWidget(self.LEVEL_1)
        self.LEVEL_2 = QtWidgets.QRadioButton(Main_Windows)
        self.LEVEL_2.setObjectName("LEVEL_2")
        self.verticalLayout_5.addWidget(self.LEVEL_2)
        self.LEVEL_3 = QtWidgets.QRadioButton(Main_Windows)
        self.LEVEL_3.setObjectName("LEVEL_3")
        self.verticalLayout_5.addWidget(self.LEVEL_3)
        self.LEVEL_4 = QtWidgets.QRadioButton(Main_Windows)
        self.LEVEL_4.setObjectName("LEVEL_4")
        self.verticalLayout_5.addWidget(self.LEVEL_4)
        self.LEVEL_5 = QtWidgets.QRadioButton(Main_Windows)
        self.LEVEL_5.setObjectName("LEVEL_5")
        self.verticalLayout_5.addWidget(self.LEVEL_5)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem18)
        self.horizontalLayout_8.addLayout(self.verticalLayout_6)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem19)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.group_1 = QtWidgets.QButtonGroup(self)
        self.group_2 = QtWidgets.QButtonGroup(self)
        self.group_1.addButton(self.LEVEL_1, 0)
        self.group_1.addButton(self.LEVEL_2, 1)
        self.group_1.addButton(self.LEVEL_3, 2)
        self.group_1.addButton(self.LEVEL_4, 3)
        self.group_1.addButton(self.LEVEL_5, 4)
        self.group_2.addButton(self.manual_driver, 0)
        self.group_2.addButton(self.automatic_tracing, 1)
        self.manual_driver.setChecked(True)
        self.LEVEL_1.setChecked(True)
        self.LEVELS = [self.LEVEL_1, self.LEVEL_2, self.LEVEL_3, self.LEVEL_4, self.LEVEL_5]
        self.FUNCTIONS = [self.manual_driver, self.automatic_tracing]

        self.retranslateUi(Main_Windows)
        QtCore.QMetaObject.connectSlotsByName(Main_Windows)

    def retranslateUi(self, Main_Windows):
        _translate = QtCore.QCoreApplication.translate
        Main_Windows.setWindowTitle(_translate("Main_Windows", "control_window"))
        self.label_2.setText(_translate("Main_Windows", "W,A,S,D keys control the car movement"))
        self.label.setText(_translate("Main_Windows", "current speed:"))
        self.current_speed.setText(_translate("Main_Windows", "LEVEL 1"))
        self.label_4.setText(_translate("Main_Windows", "barrier distance: "))
        self.barrier_distance.setText(_translate("Main_Windows", "200cm"))
        self.manual_driver.setText(_translate("Main_Windows", "manual driving"))
        self.automatic_tracing.setText(_translate("Main_Windows", "automatic tracing"))
        self.LEVEL_1.setText(_translate("Main_Windows", "LEVEL 1"))
        self.LEVEL_2.setText(_translate("Main_Windows", "LEVEL 2"))
        self.LEVEL_3.setText(_translate("Main_Windows", "LEVEL 3"))
        self.LEVEL_4.setText(_translate("Main_Windows", "LEVEL 4"))
        self.LEVEL_5.setText(_translate("Main_Windows", "LEVEL 5"))