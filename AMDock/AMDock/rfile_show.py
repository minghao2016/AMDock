from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Result_File(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        screen = QDesktopWidget().screenGeometry()
        mysize = self.geometry()
        self.hpos = (screen.width() - mysize.width()) / 2
        self.vpos = 170
        # self.setGeometry(QRect(self.hpos+100, self.vpos, 600, 500))
        self.parent = parent
        self.setModal(False)

        self.setMaximumSize(800,500)
        self.setMinimumSize(700, 400)
        self.setWindowTitle('AMDock: File Result')
        self.setWindowIcon(QIcon(QPixmap("amdock_icon.png")))

        layout = QVBoxLayout()
        self.label = QLabel(self)
        # self.label.setGeometry(QRect(120, 10, 511, 31))
        self.label.setObjectName("label")
        self.label.setText('<html><head/><body><p><span style=\" font-size:24pt;font-weight:600;font-family:times new roman;\
                            text-decoration: underline; color:#000000;\">AMDock</span><br>'
                           '<span style=\" color:#000000;font-size:14pt;font-family:times\">  Assisted Molecular Docking with AutoDock4 and AutoDock Vina</span></p></body></html>')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        layout.addSpacing(35)
        layout1 = QHBoxLayout()
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        self.label_2.setText('Project Name       ')
        layout1.addWidget(self.label_2)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        layout1.addWidget(self.lineEdit)
        layout.addLayout(layout1)
        layout2 = QHBoxLayout()
        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")
        self.label_3.setText('Working Directory')
        layout2.addWidget(self.label_3 )
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        layout2.addWidget(self.lineEdit_2 )
        layout.addLayout(layout2)
        layout3 = QHBoxLayout()
        self.label_4 = QLabel(self)
        self.label_4.setObjectName("label_4")
        self.label_4.setText('Docking Program  ')
        layout3.addWidget(self.label_4)
        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        layout3.addWidget(self.lineEdit_3 )
        layout.addLayout(layout3)
        layout.addSpacing(35)
        layout4 =QHBoxLayout()
        self.label_5 = QLabel(self)
        self.label_5.setObjectName("label_5")
        self.label_5.setText('Ligand')
        layout4.addWidget(self.label_5)
        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        layout4.addWidget(self.lineEdit_4 )
        layout.addLayout(layout4)
        layout5 = QHBoxLayout()
        self.label_6 = QLabel(self)
        self.label_6.setObjectName("label_6")
        self.label_6.setText('Program Mode:')
        layout5.addWidget(self.label_6 )

        self.mode_label = QLabel(self)
        self.mode_label.setGeometry(QRect(80, 190, 120, 17))
        self.mode_label.setObjectName("mode_label")
        layout5.addWidget(self.mode_label )
        layout5.addStretch()
        layout.addLayout(layout5)

        layoutv1 = QVBoxLayout()
        layout7 = QHBoxLayout()
        self.label_7 = QLabel(self)
        self.label_7.setObjectName("label_7")
        self.label_7.setText('Target Protein')
        layout7.addWidget(self.label_7)
        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        layout7.addWidget(self.lineEdit_5 )
        layoutv1.addLayout(layout7)

        layout8 = QHBoxLayout()
        layout8.addSpacing(32)
        self.label_8 = QLabel(self)
        self.label_8.setObjectName("label_8")
        self.label_8.setText('Ligands')
        layout8.addWidget(self.label_8)
        self.lineEdit_6 = QLineEdit(self)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        layout8.addWidget(self.lineEdit_6 )
        layoutv1.addLayout(layout8)


        layout9 = QHBoxLayout()
        layout9.addSpacing(17)
        self.label_9 = QLabel(self)
        self.label_9.setObjectName("label_9")
        self.label_9.setText('Metals(Zn)')
        layout9.addWidget(self.label_9)
        self.lineEdit_7 = QLineEdit(self)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        layout9.addWidget(self.lineEdit_7 )

        layoutv1.addLayout(layout9)
        layoutv1.addSpacing(20)

        layout11 = QHBoxLayout()
        self.label_11 = QLabel(self)
        self.label_11.setObjectName("label_11")
        self.label_11.setText('Best Pose')
        self.lineEdit_9 = QLineEdit(self)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setReadOnly(True)
        layout11.addWidget(self.label_11)
        layout11.addWidget(self.lineEdit_9)
        layoutv1.addLayout(layout11)

        layout10 = QHBoxLayout()
        layout10.addSpacing(4)
        self.label_10 = QLabel(self)
        self.label_10.setObjectName("label_10")
        self.label_10.setText('All Poses')
        self.lineEdit_8 = QLineEdit(self)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        layout10.addWidget(self.label_10)
        layout10.addWidget(self.lineEdit_8)
        layoutv1.addLayout(layout10)

        layoutv2 = QVBoxLayout()
        layout12 = QHBoxLayout()
        self.label_12 = QLabel(self)
        self.label_12.setObjectName("label_12")
        self.label_12.setText('Off-Target Protein')
        self.lineEdit_10 = QLineEdit(self)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setReadOnly(True)
        layout12.addWidget(self.label_12)
        layout12.addWidget(self.lineEdit_10 )
        layoutv2.addLayout(layout12)

        layout13 = QHBoxLayout()
        layout13.addSpacing(36)
        self.label_13 = QLabel(self)
        self.label_13.setObjectName("label_13")
        self.label_13.setText('Ligands')
        layout13.addWidget(self.label_13)
        self.lineEdit_11 = QLineEdit(self)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setReadOnly(True)
        layout13.addWidget(self.lineEdit_11)
        layoutv2.addLayout(layout13)

        layout14 = QHBoxLayout()
        layout14.addSpacing(21)
        self.label_14 = QLabel(self)
        self.label_14.setObjectName("label_14")
        self.label_14.setText('Metals(Zn)')
        layout14.addWidget(self.label_14)
        self.lineEdit_12 = QLineEdit(self)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setReadOnly(True)
        layout14.addWidget(self.lineEdit_12)
        layoutv2.addLayout(layout14)
        layoutv2.addSpacing(20)

        layout16 = QHBoxLayout()
        self.label_16 = QLabel(self)
        self.label_16.setObjectName("label_16")
        self.label_16.setText('Best Pose')
        layout16.addWidget(self.label_16)
        self.lineEdit_14 = QLineEdit(self)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setReadOnly(True)
        layout16.addWidget(self.lineEdit_14)
        layoutv2.addLayout(layout16)

        layout15 =QHBoxLayout()
        layout15.addSpacing(4)
        self.label_15 = QLabel(self)
        self.label_15.setObjectName("label_15")
        self.label_15.setText('All Poses')
        layout15.addWidget(self.label_15 )
        self.lineEdit_13 = QLineEdit(self)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setReadOnly(True)
        layout15.addWidget(self.lineEdit_13)
        layoutv2.addLayout(layout15)

        layouth = QHBoxLayout()
        layouth.addLayout(layoutv1)
        layouth.addSpacing(10)
        layouth.addLayout(layoutv2)
        layout.addLayout(layouth)

        self.setLayout(layout)
        self.finished.connect(self.finish)

    def finish(self):
        self.parent.only_one = 0
