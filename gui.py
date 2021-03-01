# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.setEnabled(True)
        GUI.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
        GUI.setSizePolicy(sizePolicy)
        GUI.setMinimumSize(QtCore.QSize(1000, 800))
        GUI.setMaximumSize(QtCore.QSize(1000, 800))
        self.centralwidget = QtWidgets.QWidget(GUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rightVerticalLayout = QtWidgets.QVBoxLayout()
        self.rightVerticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.rightVerticalLayout.setSpacing(6)
        self.rightVerticalLayout.setObjectName("rightVerticalLayout")
        self.envGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.envGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.envGroupBox.setFlat(False)
        self.envGroupBox.setCheckable(False)
        self.envGroupBox.setChecked(False)
        self.envGroupBox.setObjectName("envGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.envGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.envView = QtWidgets.QGraphicsView(self.envGroupBox)
        self.envView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.envView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.envView.setLineWidth(1)
        self.envView.setMidLineWidth(0)
        self.envView.setObjectName("envView")
        self.verticalLayout_2.addWidget(self.envView)
        self.rightVerticalLayout.addWidget(self.envGroupBox)
        self.learningGraphGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.learningGraphGroupBox.setObjectName("learningGraphGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.learningGraphGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mplWidget = MplWidget(self.learningGraphGroupBox)
        self.mplWidget.setObjectName("mplWidget")
        self.verticalLayout_3.addWidget(self.mplWidget)
        self.rightVerticalLayout.addWidget(self.learningGraphGroupBox)
        self.rightVerticalLayout.setStretch(0, 1)
        self.rightVerticalLayout.setStretch(1, 1)
        self.gridLayout_4.addLayout(self.rightVerticalLayout, 0, 1, 1, 1)
        self.leftVerticalLayout = QtWidgets.QVBoxLayout()
        self.leftVerticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.leftVerticalLayout.setObjectName("leftVerticalLayout")
        self.configGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.configGroupBox.setObjectName("configGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.configGroupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.configFormLayout = QtWidgets.QFormLayout()
        self.configFormLayout.setContentsMargins(-1, 0, 0, -1)
        self.configFormLayout.setVerticalSpacing(10)
        self.configFormLayout.setObjectName("configFormLayout")
        self.envLabel = QtWidgets.QLabel(self.configGroupBox)
        self.envLabel.setObjectName("envLabel")
        self.configFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.envLabel)
        self.envComboBox = QtWidgets.QComboBox(self.configGroupBox)
        self.envComboBox.setObjectName("envComboBox")
        self.envComboBox.addItem("")
        self.envComboBox.addItem("")
        self.envComboBox.addItem("")
        self.configFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.envComboBox)
        self.verticalLayout.addLayout(self.configFormLayout)
        self.envStackedWidget = QtWidgets.QStackedWidget(self.configGroupBox)
        self.envStackedWidget.setObjectName("envStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayout = QtWidgets.QFormLayout(self.page)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridSizeComboBox = QtWidgets.QComboBox(self.page)
        self.gridSizeComboBox.setObjectName("gridSizeComboBox")
        self.gridSizeComboBox.addItem("")
        self.gridSizeComboBox.addItem("")
        self.gridSizeComboBox.addItem("")
        self.gridSizeComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gridSizeComboBox)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.snakeVisionComboBox = QtWidgets.QComboBox(self.page)
        self.snakeVisionComboBox.setObjectName("snakeVisionComboBox")
        self.snakeVisionComboBox.addItem("")
        self.snakeVisionComboBox.addItem("")
        self.snakeVisionComboBox.addItem("")
        self.snakeVisionComboBox.addItem("")
        self.snakeVisionComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.snakeVisionComboBox)
        self.envStackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.page_2)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.envStackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.envStackedWidget)
        self.line = QtWidgets.QFrame(self.configGroupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.algLabel = QtWidgets.QLabel(self.configGroupBox)
        self.algLabel.setObjectName("algLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.algLabel)
        self.algComboBox = QtWidgets.QComboBox(self.configGroupBox)
        self.algComboBox.setObjectName("algComboBox")
        self.algComboBox.addItem("")
        self.algComboBox.addItem("")
        self.algComboBox.addItem("")
        self.algComboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.algComboBox)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.algStackedWidget = QtWidgets.QStackedWidget(self.configGroupBox)
        self.algStackedWidget.setObjectName("algStackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.algStackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.page_4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page_4)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.learningRateDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_4)
        self.learningRateDoubleSpinBox.setDecimals(4)
        self.learningRateDoubleSpinBox.setMinimum(0.0001)
        self.learningRateDoubleSpinBox.setMaximum(1.0)
        self.learningRateDoubleSpinBox.setSingleStep(0.0001)
        self.learningRateDoubleSpinBox.setProperty("value", 0.001)
        self.learningRateDoubleSpinBox.setObjectName("learningRateDoubleSpinBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.learningRateDoubleSpinBox)
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gammaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_4)
        self.gammaDoubleSpinBox.setDecimals(4)
        self.gammaDoubleSpinBox.setMinimum(0.9)
        self.gammaDoubleSpinBox.setMaximum(1.0)
        self.gammaDoubleSpinBox.setSingleStep(0.001)
        self.gammaDoubleSpinBox.setProperty("value", 0.99)
        self.gammaDoubleSpinBox.setObjectName("gammaDoubleSpinBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gammaDoubleSpinBox)
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.batchSizeSpinBox = QtWidgets.QSpinBox(self.page_4)
        self.batchSizeSpinBox.setMinimum(1)
        self.batchSizeSpinBox.setMaximum(256)
        self.batchSizeSpinBox.setProperty("value", 32)
        self.batchSizeSpinBox.setObjectName("batchSizeSpinBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.batchSizeSpinBox)
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.epsilonDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_4)
        self.epsilonDoubleSpinBox.setMaximum(1.0)
        self.epsilonDoubleSpinBox.setSingleStep(0.01)
        self.epsilonDoubleSpinBox.setProperty("value", 1.0)
        self.epsilonDoubleSpinBox.setObjectName("epsilonDoubleSpinBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.epsilonDoubleSpinBox)
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.epsilonDecDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_4)
        self.epsilonDecDoubleSpinBox.setDecimals(6)
        self.epsilonDecDoubleSpinBox.setMaximum(1.0)
        self.epsilonDecDoubleSpinBox.setSingleStep(1e-06)
        self.epsilonDecDoubleSpinBox.setProperty("value", 1e-06)
        self.epsilonDecDoubleSpinBox.setObjectName("epsilonDecDoubleSpinBox")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.epsilonDecDoubleSpinBox)
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.epsilonMinSpinBox = QtWidgets.QDoubleSpinBox(self.page_4)
        self.epsilonMinSpinBox.setMaximum(1.0)
        self.epsilonMinSpinBox.setSingleStep(0.001)
        self.epsilonMinSpinBox.setProperty("value", 0.01)
        self.epsilonMinSpinBox.setObjectName("epsilonMinSpinBox")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.epsilonMinSpinBox)
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.layer1SpinBox = QtWidgets.QSpinBox(self.page_4)
        self.layer1SpinBox.setMinimum(1)
        self.layer1SpinBox.setMaximum(1024)
        self.layer1SpinBox.setProperty("value", 64)
        self.layer1SpinBox.setObjectName("layer1SpinBox")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.layer1SpinBox)
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.layer2SpinBox = QtWidgets.QSpinBox(self.page_4)
        self.layer2SpinBox.setMinimum(1)
        self.layer2SpinBox.setMaximum(1024)
        self.layer2SpinBox.setProperty("value", 32)
        self.layer2SpinBox.setObjectName("layer2SpinBox")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.layer2SpinBox)
        self.algStackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.algStackedWidget)
        self.buttonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonsHorizontalLayout.setObjectName("buttonsHorizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.configGroupBox)
        self.startButton.setObjectName("startButton")
        self.buttonsHorizontalLayout.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(self.configGroupBox)
        self.pauseButton.setObjectName("pauseButton")
        self.buttonsHorizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.configGroupBox)
        self.stopButton.setObjectName("stopButton")
        self.buttonsHorizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.buttonsHorizontalLayout)
        self.leftVerticalLayout.addWidget(self.configGroupBox)
        self.gridLayout_4.addLayout(self.leftVerticalLayout, 0, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 3)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setRowStretch(0, 6)
        GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        GUI.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(GUI)
        self.statusBar.setObjectName("statusBar")
        GUI.setStatusBar(self.statusBar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(GUI)
        self.envStackedWidget.setCurrentIndex(0)
        self.gridSizeComboBox.setCurrentIndex(1)
        self.snakeVisionComboBox.setCurrentIndex(1)
        self.algStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "Capstone Project"))
        self.envGroupBox.setTitle(_translate("GUI", "Environment"))
        self.learningGraphGroupBox.setTitle(_translate("GUI", "Learning Graph"))
        self.configGroupBox.setTitle(_translate("GUI", "Configuration"))
        self.envLabel.setText(_translate("GUI", "Environment: "))
        self.envComboBox.setItemText(0, _translate("GUI", "Snake"))
        self.envComboBox.setItemText(1, _translate("GUI", "Breakout"))
        self.envComboBox.setItemText(2, _translate("GUI", "Pong"))
        self.label.setText(_translate("GUI", "Grid Size: "))
        self.gridSizeComboBox.setItemText(0, _translate("GUI", "3x3"))
        self.gridSizeComboBox.setItemText(1, _translate("GUI", "5x5"))
        self.gridSizeComboBox.setItemText(2, _translate("GUI", "7x7"))
        self.gridSizeComboBox.setItemText(3, _translate("GUI", "9x9"))
        self.label_4.setText(_translate("GUI", "Snake Vision: "))
        self.snakeVisionComboBox.setItemText(0, _translate("GUI", "1"))
        self.snakeVisionComboBox.setItemText(1, _translate("GUI", "2"))
        self.snakeVisionComboBox.setItemText(2, _translate("GUI", "3"))
        self.snakeVisionComboBox.setItemText(3, _translate("GUI", "4"))
        self.snakeVisionComboBox.setItemText(4, _translate("GUI", "5"))
        self.label_3.setText(_translate("GUI", "Paddle Size: "))
        self.algLabel.setText(_translate("GUI", "RL-Algorithm: "))
        self.algComboBox.setItemText(0, _translate("GUI", "DQN"))
        self.algComboBox.setItemText(1, _translate("GUI", "DDDQN"))
        self.algComboBox.setItemText(2, _translate("GUI", "DDPG"))
        self.algComboBox.setItemText(3, _translate("GUI", "SAC"))
        self.label_2.setText(_translate("GUI", "Learning Rate: "))
        self.label_5.setText(_translate("GUI", "Gamma: "))
        self.label_6.setText(_translate("GUI", "Batch Size: "))
        self.label_9.setText(_translate("GUI", "Epsilon Start:"))
        self.label_8.setText(_translate("GUI", "Epsilon Decrease: "))
        self.label_7.setText(_translate("GUI", "Epsilon Min: "))
        self.label_10.setText(_translate("GUI", "Layer 1 Neurons: "))
        self.label_11.setText(_translate("GUI", "Layer 2 Neurons: "))
        self.startButton.setText(_translate("GUI", "Start"))
        self.pauseButton.setText(_translate("GUI", "Pause"))
        self.stopButton.setText(_translate("GUI", "Stop"))
        self.menuFile.setTitle(_translate("GUI", "File"))
        self.menuEdit.setTitle(_translate("GUI", "Edit"))
        self.menuAbout.setTitle(_translate("GUI", "Documentation"))
from mplwidget import MplWidget
