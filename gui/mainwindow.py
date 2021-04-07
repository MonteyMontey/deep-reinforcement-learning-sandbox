# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        GUI.resize(1100, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
        GUI.setSizePolicy(sizePolicy)
        GUI.setMinimumSize(QtCore.QSize(0, 0))
        GUI.setMaximumSize(QtCore.QSize(4096, 2160))
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slowRenderingCheckBox = QtWidgets.QCheckBox(self.envGroupBox)
        self.slowRenderingCheckBox.setChecked(True)
        self.slowRenderingCheckBox.setObjectName("slowRenderingCheckBox")
        self.buttonGroup = QtWidgets.QButtonGroup(GUI)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.slowRenderingCheckBox)
        self.horizontalLayout.addWidget(self.slowRenderingCheckBox)
        self.fastRenderingCheckBox = QtWidgets.QCheckBox(self.envGroupBox)
        self.fastRenderingCheckBox.setObjectName("fastRenderingCheckBox")
        self.buttonGroup.addButton(self.fastRenderingCheckBox)
        self.horizontalLayout.addWidget(self.fastRenderingCheckBox)
        self.noRenderingCheckBox = QtWidgets.QCheckBox(self.envGroupBox)
        self.noRenderingCheckBox.setObjectName("noRenderingCheckBox")
        self.buttonGroup.addButton(self.noRenderingCheckBox)
        self.horizontalLayout.addWidget(self.noRenderingCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
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
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mplWidget = MplWidget(self.learningGraphGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy)
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
        self.snake_config_page = QtWidgets.QWidget()
        self.snake_config_page.setObjectName("snake_config_page")
        self.formLayout = QtWidgets.QFormLayout(self.snake_config_page)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.snake_config_page)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridSizeComboBox = QtWidgets.QComboBox(self.snake_config_page)
        self.gridSizeComboBox.setMaxVisibleItems(8)
        self.gridSizeComboBox.setObjectName("gridSizeComboBox")
        self.gridSizeComboBox.addItem("")
        self.gridSizeComboBox.addItem("")
        self.gridSizeComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gridSizeComboBox)
        self.label_4 = QtWidgets.QLabel(self.snake_config_page)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.snakeVisionComboBox = QtWidgets.QComboBox(self.snake_config_page)
        self.snakeVisionComboBox.setObjectName("snakeVisionComboBox")
        self.snakeVisionComboBox.addItem("")
        self.snakeVisionComboBox.addItem("")
        self.snakeVisionComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.snakeVisionComboBox)
        self.envStackedWidget.addWidget(self.snake_config_page)
        self.breakout_config_page = QtWidgets.QWidget()
        self.breakout_config_page.setObjectName("breakout_config_page")
        self.formLayout_4 = QtWidgets.QFormLayout(self.breakout_config_page)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.breakout_config_page)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.paddleSizeSpinBox = QtWidgets.QSpinBox(self.breakout_config_page)
        self.paddleSizeSpinBox.setMinimum(3)
        self.paddleSizeSpinBox.setMaximum(30)
        self.paddleSizeSpinBox.setProperty("value", 15)
        self.paddleSizeSpinBox.setObjectName("paddleSizeSpinBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.paddleSizeSpinBox)
        self.envStackedWidget.addWidget(self.breakout_config_page)
        self.pong_config_page = QtWidgets.QWidget()
        self.pong_config_page.setObjectName("pong_config_page")
        self.envStackedWidget.addWidget(self.pong_config_page)
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
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.algComboBox)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.algStackedWidget = QtWidgets.QStackedWidget(self.configGroupBox)
        self.algStackedWidget.setObjectName("algStackedWidget")
        self.DDDQNConfigPage = QtWidgets.QWidget()
        self.DDDQNConfigPage.setObjectName("DDDQNConfigPage")
        self.formLayout_3 = QtWidgets.QFormLayout(self.DDDQNConfigPage)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.learningRateDoubleSpinBoxDDDQN = QtWidgets.QDoubleSpinBox(self.DDDQNConfigPage)
        self.learningRateDoubleSpinBoxDDDQN.setDecimals(6)
        self.learningRateDoubleSpinBoxDDDQN.setMinimum(1e-06)
        self.learningRateDoubleSpinBoxDDDQN.setMaximum(1.0)
        self.learningRateDoubleSpinBoxDDDQN.setSingleStep(1e-06)
        self.learningRateDoubleSpinBoxDDDQN.setProperty("value", 0.001)
        self.learningRateDoubleSpinBoxDDDQN.setObjectName("learningRateDoubleSpinBoxDDDQN")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.learningRateDoubleSpinBoxDDDQN)
        self.label_5 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gammaDoubleSpinBoxDDDQN = QtWidgets.QDoubleSpinBox(self.DDDQNConfigPage)
        self.gammaDoubleSpinBoxDDDQN.setDecimals(4)
        self.gammaDoubleSpinBoxDDDQN.setMinimum(0.9)
        self.gammaDoubleSpinBoxDDDQN.setMaximum(1.0)
        self.gammaDoubleSpinBoxDDDQN.setSingleStep(0.001)
        self.gammaDoubleSpinBoxDDDQN.setProperty("value", 0.99)
        self.gammaDoubleSpinBoxDDDQN.setObjectName("gammaDoubleSpinBoxDDDQN")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gammaDoubleSpinBoxDDDQN)
        self.label_6 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.batchSizeSpinBoxDDDQN = QtWidgets.QSpinBox(self.DDDQNConfigPage)
        self.batchSizeSpinBoxDDDQN.setMinimum(8)
        self.batchSizeSpinBoxDDDQN.setMaximum(256)
        self.batchSizeSpinBoxDDDQN.setProperty("value", 32)
        self.batchSizeSpinBoxDDDQN.setObjectName("batchSizeSpinBoxDDDQN")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.batchSizeSpinBoxDDDQN)
        self.label_9 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.epsilonDoubleSpinBoxDDDQN = QtWidgets.QDoubleSpinBox(self.DDDQNConfigPage)
        self.epsilonDoubleSpinBoxDDDQN.setMinimum(0.5)
        self.epsilonDoubleSpinBoxDDDQN.setMaximum(1.0)
        self.epsilonDoubleSpinBoxDDDQN.setSingleStep(0.01)
        self.epsilonDoubleSpinBoxDDDQN.setProperty("value", 1.0)
        self.epsilonDoubleSpinBoxDDDQN.setObjectName("epsilonDoubleSpinBoxDDDQN")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.epsilonDoubleSpinBoxDDDQN)
        self.label_8 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.epsilonDecDoubleSpinBoxDDDQN = QtWidgets.QDoubleSpinBox(self.DDDQNConfigPage)
        self.epsilonDecDoubleSpinBoxDDDQN.setDecimals(6)
        self.epsilonDecDoubleSpinBoxDDDQN.setMinimum(1e-06)
        self.epsilonDecDoubleSpinBoxDDDQN.setMaximum(1.0)
        self.epsilonDecDoubleSpinBoxDDDQN.setSingleStep(1e-06)
        self.epsilonDecDoubleSpinBoxDDDQN.setProperty("value", 1e-05)
        self.epsilonDecDoubleSpinBoxDDDQN.setObjectName("epsilonDecDoubleSpinBoxDDDQN")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.epsilonDecDoubleSpinBoxDDDQN)
        self.label_7 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.epsilonMinSpinBoxDDDQN = QtWidgets.QDoubleSpinBox(self.DDDQNConfigPage)
        self.epsilonMinSpinBoxDDDQN.setDecimals(3)
        self.epsilonMinSpinBoxDDDQN.setMinimum(0.001)
        self.epsilonMinSpinBoxDDDQN.setMaximum(0.2)
        self.epsilonMinSpinBoxDDDQN.setSingleStep(0.001)
        self.epsilonMinSpinBoxDDDQN.setProperty("value", 0.01)
        self.epsilonMinSpinBoxDDDQN.setObjectName("epsilonMinSpinBoxDDDQN")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.epsilonMinSpinBoxDDDQN)
        self.label_10 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.layer1SpinBoxDDDQN = QtWidgets.QSpinBox(self.DDDQNConfigPage)
        self.layer1SpinBoxDDDQN.setMinimum(16)
        self.layer1SpinBoxDDDQN.setMaximum(1024)
        self.layer1SpinBoxDDDQN.setProperty("value", 64)
        self.layer1SpinBoxDDDQN.setObjectName("layer1SpinBoxDDDQN")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.layer1SpinBoxDDDQN)
        self.label_11 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.layer2SpinBoxDDDQN = QtWidgets.QSpinBox(self.DDDQNConfigPage)
        self.layer2SpinBoxDDDQN.setMinimum(16)
        self.layer2SpinBoxDDDQN.setMaximum(1024)
        self.layer2SpinBoxDDDQN.setProperty("value", 32)
        self.layer2SpinBoxDDDQN.setObjectName("layer2SpinBoxDDDQN")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.layer2SpinBoxDDDQN)
        self.tauDoubleSpinBoxDDDQN = QtWidgets.QDoubleSpinBox(self.DDDQNConfigPage)
        self.tauDoubleSpinBoxDDDQN.setDecimals(5)
        self.tauDoubleSpinBoxDDDQN.setMinimum(1e-05)
        self.tauDoubleSpinBoxDDDQN.setMaximum(0.1)
        self.tauDoubleSpinBoxDDDQN.setSingleStep(0.0001)
        self.tauDoubleSpinBoxDDDQN.setProperty("value", 0.001)
        self.tauDoubleSpinBoxDDDQN.setObjectName("tauDoubleSpinBoxDDDQN")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.tauDoubleSpinBoxDDDQN)
        self.label_20 = QtWidgets.QLabel(self.DDDQNConfigPage)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.algStackedWidget.addWidget(self.DDDQNConfigPage)
        self.DDPGConfigPage = QtWidgets.QWidget()
        self.DDPGConfigPage.setObjectName("DDPGConfigPage")
        self.formLayout_6 = QtWidgets.QFormLayout(self.DDPGConfigPage)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_21 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_21.setObjectName("label_21")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.learningRateAlphaDoubleSpinBoxDDPG = QtWidgets.QDoubleSpinBox(self.DDPGConfigPage)
        self.learningRateAlphaDoubleSpinBoxDDPG.setDecimals(6)
        self.learningRateAlphaDoubleSpinBoxDDPG.setMinimum(1e-06)
        self.learningRateAlphaDoubleSpinBoxDDPG.setMaximum(1.0)
        self.learningRateAlphaDoubleSpinBoxDDPG.setSingleStep(1e-06)
        self.learningRateAlphaDoubleSpinBoxDDPG.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.learningRateAlphaDoubleSpinBoxDDPG.setProperty("value", 0.001)
        self.learningRateAlphaDoubleSpinBoxDDPG.setObjectName("learningRateAlphaDoubleSpinBoxDDPG")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.learningRateAlphaDoubleSpinBoxDDPG)
        self.label_27 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_27.setObjectName("label_27")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.gammaDoubleSpinBoxDDPG = QtWidgets.QDoubleSpinBox(self.DDPGConfigPage)
        self.gammaDoubleSpinBoxDDPG.setDecimals(4)
        self.gammaDoubleSpinBoxDDPG.setMinimum(0.9)
        self.gammaDoubleSpinBoxDDPG.setMaximum(1.0)
        self.gammaDoubleSpinBoxDDPG.setSingleStep(0.001)
        self.gammaDoubleSpinBoxDDPG.setProperty("value", 0.99)
        self.gammaDoubleSpinBoxDDPG.setObjectName("gammaDoubleSpinBoxDDPG")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gammaDoubleSpinBoxDDPG)
        self.label_26 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_26.setObjectName("label_26")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.batchSizeSpinBoxDDPG = QtWidgets.QSpinBox(self.DDPGConfigPage)
        self.batchSizeSpinBoxDDPG.setMinimum(8)
        self.batchSizeSpinBoxDDPG.setMaximum(256)
        self.batchSizeSpinBoxDDPG.setProperty("value", 32)
        self.batchSizeSpinBoxDDPG.setObjectName("batchSizeSpinBoxDDPG")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.batchSizeSpinBoxDDPG)
        self.label_25 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.tauDoubleSpinBoxDDPG = QtWidgets.QDoubleSpinBox(self.DDPGConfigPage)
        self.tauDoubleSpinBoxDDPG.setDecimals(5)
        self.tauDoubleSpinBoxDDPG.setMinimum(1e-05)
        self.tauDoubleSpinBoxDDPG.setMaximum(0.1)
        self.tauDoubleSpinBoxDDPG.setSingleStep(0.0001)
        self.tauDoubleSpinBoxDDPG.setProperty("value", 0.001)
        self.tauDoubleSpinBoxDDPG.setObjectName("tauDoubleSpinBoxDDPG")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tauDoubleSpinBoxDDPG)
        self.label_23 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_23.setObjectName("label_23")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.layer1SpinBoxDDPG = QtWidgets.QSpinBox(self.DDPGConfigPage)
        self.layer1SpinBoxDDPG.setMinimum(16)
        self.layer1SpinBoxDDPG.setMaximum(1024)
        self.layer1SpinBoxDDPG.setProperty("value", 64)
        self.layer1SpinBoxDDPG.setObjectName("layer1SpinBoxDDPG")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.layer1SpinBoxDDPG)
        self.label_22 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_22.setObjectName("label_22")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.layer2SpinBoxDDPG = QtWidgets.QSpinBox(self.DDPGConfigPage)
        self.layer2SpinBoxDDPG.setMinimum(16)
        self.layer2SpinBoxDDPG.setMaximum(1024)
        self.layer2SpinBoxDDPG.setProperty("value", 32)
        self.layer2SpinBoxDDPG.setObjectName("layer2SpinBoxDDPG")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.layer2SpinBoxDDPG)
        self.learningRateBetaDoubleSpinBoxDDPG = QtWidgets.QDoubleSpinBox(self.DDPGConfigPage)
        self.learningRateBetaDoubleSpinBoxDDPG.setDecimals(6)
        self.learningRateBetaDoubleSpinBoxDDPG.setMinimum(1e-06)
        self.learningRateBetaDoubleSpinBoxDDPG.setMaximum(1.0)
        self.learningRateBetaDoubleSpinBoxDDPG.setSingleStep(1e-06)
        self.learningRateBetaDoubleSpinBoxDDPG.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.learningRateBetaDoubleSpinBoxDDPG.setProperty("value", 0.001)
        self.learningRateBetaDoubleSpinBoxDDPG.setObjectName("learningRateBetaDoubleSpinBoxDDPG")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.learningRateBetaDoubleSpinBoxDDPG)
        self.label_34 = QtWidgets.QLabel(self.DDPGConfigPage)
        self.label_34.setObjectName("label_34")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.algStackedWidget.addWidget(self.DDPGConfigPage)
        self.SACConfigPage = QtWidgets.QWidget()
        self.SACConfigPage.setObjectName("SACConfigPage")
        self.formLayout_7 = QtWidgets.QFormLayout(self.SACConfigPage)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_24 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_24.setObjectName("label_24")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_28 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_28.setObjectName("label_28")
        self.formLayout_7.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_30 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_30.setObjectName("label_30")
        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.label_31 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_31.setObjectName("label_31")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.label_29 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_29.setObjectName("label_29")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.label_32 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_32.setObjectName("label_32")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.label_33 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_33.setObjectName("label_33")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.learningRateAlphaDoubleSpinBoxSAC = QtWidgets.QDoubleSpinBox(self.SACConfigPage)
        self.learningRateAlphaDoubleSpinBoxSAC.setDecimals(6)
        self.learningRateAlphaDoubleSpinBoxSAC.setMinimum(1e-06)
        self.learningRateAlphaDoubleSpinBoxSAC.setMaximum(1.0)
        self.learningRateAlphaDoubleSpinBoxSAC.setSingleStep(1e-06)
        self.learningRateAlphaDoubleSpinBoxSAC.setProperty("value", 0.001)
        self.learningRateAlphaDoubleSpinBoxSAC.setObjectName("learningRateAlphaDoubleSpinBoxSAC")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.learningRateAlphaDoubleSpinBoxSAC)
        self.gammaDoubleSpinBoxSAC = QtWidgets.QDoubleSpinBox(self.SACConfigPage)
        self.gammaDoubleSpinBoxSAC.setDecimals(4)
        self.gammaDoubleSpinBoxSAC.setMinimum(0.9)
        self.gammaDoubleSpinBoxSAC.setMaximum(1.0)
        self.gammaDoubleSpinBoxSAC.setSingleStep(0.001)
        self.gammaDoubleSpinBoxSAC.setProperty("value", 0.99)
        self.gammaDoubleSpinBoxSAC.setObjectName("gammaDoubleSpinBoxSAC")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gammaDoubleSpinBoxSAC)
        self.tauDoubleSpinBoxSAC = QtWidgets.QDoubleSpinBox(self.SACConfigPage)
        self.tauDoubleSpinBoxSAC.setDecimals(5)
        self.tauDoubleSpinBoxSAC.setMinimum(1e-05)
        self.tauDoubleSpinBoxSAC.setMaximum(0.1)
        self.tauDoubleSpinBoxSAC.setSingleStep(0.0001)
        self.tauDoubleSpinBoxSAC.setProperty("value", 0.001)
        self.tauDoubleSpinBoxSAC.setObjectName("tauDoubleSpinBoxSAC")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tauDoubleSpinBoxSAC)
        self.batchSizeSpinBoxSAC = QtWidgets.QSpinBox(self.SACConfigPage)
        self.batchSizeSpinBoxSAC.setMinimum(8)
        self.batchSizeSpinBoxSAC.setMaximum(256)
        self.batchSizeSpinBoxSAC.setProperty("value", 32)
        self.batchSizeSpinBoxSAC.setObjectName("batchSizeSpinBoxSAC")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.batchSizeSpinBoxSAC)
        self.rewardScaleSpinBoxSAC = QtWidgets.QSpinBox(self.SACConfigPage)
        self.rewardScaleSpinBoxSAC.setMinimum(1)
        self.rewardScaleSpinBoxSAC.setMaximum(50)
        self.rewardScaleSpinBoxSAC.setProperty("value", 5)
        self.rewardScaleSpinBoxSAC.setObjectName("rewardScaleSpinBoxSAC")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rewardScaleSpinBoxSAC)
        self.layer1SpinBoxSAC = QtWidgets.QSpinBox(self.SACConfigPage)
        self.layer1SpinBoxSAC.setMinimum(16)
        self.layer1SpinBoxSAC.setMaximum(1024)
        self.layer1SpinBoxSAC.setProperty("value", 64)
        self.layer1SpinBoxSAC.setObjectName("layer1SpinBoxSAC")
        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.layer1SpinBoxSAC)
        self.layer2spinBoxSAC = QtWidgets.QSpinBox(self.SACConfigPage)
        self.layer2spinBoxSAC.setMinimum(16)
        self.layer2spinBoxSAC.setMaximum(1024)
        self.layer2spinBoxSAC.setProperty("value", 32)
        self.layer2spinBoxSAC.setObjectName("layer2spinBoxSAC")
        self.formLayout_7.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.layer2spinBoxSAC)
        self.label_35 = QtWidgets.QLabel(self.SACConfigPage)
        self.label_35.setObjectName("label_35")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.learningRateBetaDoubleSpinBoxSAC = QtWidgets.QDoubleSpinBox(self.SACConfigPage)
        self.learningRateBetaDoubleSpinBoxSAC.setDecimals(6)
        self.learningRateBetaDoubleSpinBoxSAC.setMinimum(1e-06)
        self.learningRateBetaDoubleSpinBoxSAC.setMaximum(1.0)
        self.learningRateBetaDoubleSpinBoxSAC.setSingleStep(1e-06)
        self.learningRateBetaDoubleSpinBoxSAC.setProperty("value", 0.001)
        self.learningRateBetaDoubleSpinBoxSAC.setObjectName("learningRateBetaDoubleSpinBoxSAC")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.learningRateBetaDoubleSpinBoxSAC)
        self.algStackedWidget.addWidget(self.SACConfigPage)
        self.verticalLayout.addWidget(self.algStackedWidget)
        self.buttonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonsHorizontalLayout.setObjectName("buttonsHorizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.configGroupBox)
        self.startButton.setObjectName("startButton")
        self.buttonsHorizontalLayout.addWidget(self.startButton)
        self.pauseButton = QtWidgets.QPushButton(self.configGroupBox)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setObjectName("pauseButton")
        self.buttonsHorizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.configGroupBox)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self.buttonsHorizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.buttonsHorizontalLayout)
        self.leftVerticalLayout.addWidget(self.configGroupBox)
        self.gridLayout_4.addLayout(self.leftVerticalLayout, 0, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 3)
        GUI.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(GUI)
        self.statusBar.setObjectName("statusBar")
        GUI.setStatusBar(self.statusBar)
        self.actionSaveModel = QtWidgets.QAction(GUI)
        self.actionSaveModel.setEnabled(False)
        self.actionSaveModel.setObjectName("actionSaveModel")
        self.actionLoad_Model = QtWidgets.QAction(GUI)
        self.actionLoad_Model.setObjectName("actionLoad_Model")
        self.actionLoadModel = QtWidgets.QAction(GUI)
        self.actionLoadModel.setObjectName("actionLoadModel")

        self.retranslateUi(GUI)
        self.envStackedWidget.setCurrentIndex(0)
        self.gridSizeComboBox.setCurrentIndex(1)
        self.snakeVisionComboBox.setCurrentIndex(1)
        self.algStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "Reinforcement Learning Sandbox (Alpha)"))
        self.envGroupBox.setTitle(_translate("GUI", "Environment"))
        self.slowRenderingCheckBox.setText(_translate("GUI", "Slow Rendering (Slow)"))
        self.fastRenderingCheckBox.setText(_translate("GUI", "Fast Rendering (Fast)"))
        self.noRenderingCheckBox.setText(_translate("GUI", "No Rendering (Fastest)"))
        self.learningGraphGroupBox.setTitle(_translate("GUI", "Learning Graph"))
        self.configGroupBox.setTitle(_translate("GUI", "Configuration"))
        self.envLabel.setText(_translate("GUI", "Environment: "))
        self.envComboBox.setItemText(0, _translate("GUI", "Snake"))
        self.envComboBox.setItemText(1, _translate("GUI", "Breakout"))
        self.envComboBox.setItemText(2, _translate("GUI", "Pong"))
        self.label.setText(_translate("GUI", "Grid Size: "))
        self.gridSizeComboBox.setItemText(0, _translate("GUI", "5x5"))
        self.gridSizeComboBox.setItemText(1, _translate("GUI", "7x7"))
        self.gridSizeComboBox.setItemText(2, _translate("GUI", "9x9"))
        self.label_4.setText(_translate("GUI", "Snake Vision: "))
        self.snakeVisionComboBox.setCurrentText(_translate("GUI", "2"))
        self.snakeVisionComboBox.setItemText(0, _translate("GUI", "1"))
        self.snakeVisionComboBox.setItemText(1, _translate("GUI", "2"))
        self.snakeVisionComboBox.setItemText(2, _translate("GUI", "3"))
        self.label_3.setText(_translate("GUI", "Paddle Size: "))
        self.algLabel.setText(_translate("GUI", "RL-Algorithm: "))
        self.algComboBox.setItemText(0, _translate("GUI", "DDDQN"))
        self.algComboBox.setItemText(1, _translate("GUI", "DDPG"))
        self.algComboBox.setItemText(2, _translate("GUI", "SAC"))
        self.label_2.setText(_translate("GUI", "Learning Rate: "))
        self.label_5.setText(_translate("GUI", "Gamma: "))
        self.label_6.setText(_translate("GUI", "Batch Size: "))
        self.label_9.setText(_translate("GUI", "Epsilon Start:"))
        self.label_8.setText(_translate("GUI", "Epsilon Decrease: "))
        self.label_7.setText(_translate("GUI", "Epsilon Min: "))
        self.label_10.setText(_translate("GUI", "Layer 1 Neurons: "))
        self.label_11.setText(_translate("GUI", "Layer 2 Neurons: "))
        self.label_20.setText(_translate("GUI", "Tau:"))
        self.label_21.setText(_translate("GUI", "Learning Rate (Alpha): "))
        self.label_27.setText(_translate("GUI", "Gamma: "))
        self.label_26.setText(_translate("GUI", "Batch Size:"))
        self.label_25.setText(_translate("GUI", "Tau: "))
        self.label_23.setText(_translate("GUI", "Layer 1 Neurons: "))
        self.label_22.setText(_translate("GUI", "Layer 2 Neurons: "))
        self.label_34.setText(_translate("GUI", "Learning Rate (Beta): "))
        self.label_24.setText(_translate("GUI", "Learning Rate (Alpha): "))
        self.label_28.setText(_translate("GUI", "Layer 2 Neurons: "))
        self.label_30.setText(_translate("GUI", "Layer 1 Neurons: "))
        self.label_31.setText(_translate("GUI", "Reward Scale: "))
        self.label_29.setText(_translate("GUI", "Tau: "))
        self.label_32.setText(_translate("GUI", "Batch Size: "))
        self.label_33.setText(_translate("GUI", "Gamma: "))
        self.label_35.setText(_translate("GUI", "Learning Rate (Beta): "))
        self.startButton.setText(_translate("GUI", "Start"))
        self.pauseButton.setText(_translate("GUI", "Pause"))
        self.stopButton.setText(_translate("GUI", "Stop"))
        self.actionSaveModel.setText(_translate("GUI", "Save Model..."))
        self.actionLoad_Model.setText(_translate("GUI", "Load Model"))
        self.actionLoadModel.setText(_translate("GUI", "Open Model..."))
from .mplwidget import MplWidget
