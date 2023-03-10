# -*- coding: utf-8 -*-
import re

# Form implementation generated from reading ui file 'View_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

SECRET = "HITSZ"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Query import Query


class Ui_View_reg(object):
    def __init__(self):
        with open("configs.txt", encoding='utf-8') as file:
            content = file.readlines()

        for line in content:
            if re.search(r"SECRET\s*=\s*\'(.*?)\'", line) is not None:
                n = re.search(r"\'(.*?)\'", line)
                m = n.group(0).strip('\'')
                SECRET = m

    def setupUi(self, View_reg):
        View_reg.setObjectName("View_reg")
        View_reg.resize(613, 545)
        self.View_register = QtWidgets.QWidget(View_reg)
        self.View_register.setObjectName("View_register")
        self.gridLayout = QtWidgets.QGridLayout(self.View_register)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.View_register)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.View_register)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.View_register)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.View_register)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.View_register)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.View_register)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.View_register)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.View_register)
        self.lineEdit_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 8, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.View_register)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.View_register)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.View_register)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.View_register)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)
        View_reg.setCentralWidget(self.View_register)
        self.statusBar = QtWidgets.QStatusBar(View_reg)
        self.statusBar.setObjectName("statusBar")
        View_reg.setStatusBar(self.statusBar)

        self.retranslateUi(View_reg)
        QtCore.QMetaObject.connectSlotsByName(View_reg)

        self.pushButton.clicked.connect(self.register)

    def retranslateUi(self, View_reg):
        _translate = QtCore.QCoreApplication.translate
        View_reg.setWindowTitle(_translate("View_reg", "????????????"))
        self.pushButton.setText(_translate("View_reg", "??????"))
        self.label.setText(_translate("View_reg", "??????"))
        self.label_2.setText(_translate("View_reg", "??????"))
        self.pushButton_2.setText(_translate("View_reg", "??????"))
        self.label_3.setText(_translate("View_reg", "?????????"))
        self.lineEdit_5.setText(_translate("View_reg", "????????????????????????????????????????????????????????????????????????????????????"))
        self.label_4.setText(_translate("View_reg", "?????????"))
        self.label_5.setText(_translate("View_reg", "???????????????"))

    def register(self):
        self.query = Query()
        # ???????????????????????????????????????????????????id????????????????????????
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        username = self.lineEdit_3.text()
        teacherId = self.lineEdit_4.text()
        secret = self.lineEdit_5.text()

        # ?????????????????????????????????
        sql = 'SELECT account,password,teacher_id,user_name FROM users'
        results = self.query.fetch(sql)

        # ??????????????????????????????
        sql2 = 'SELECT teacher_id FROM teachers'
        teacherids = self.query.fetch(sql2)

        flag = True
        for i in results:
            if account == i[0]:
                flag = False
                msg_box = QMessageBox(QMessageBox.Warning, '??????', '??????????????????,???????????????')
                msg_box.exec_()  # ???????????????
                break
            elif username == i[3]:
                flag = False
                msg_box = QMessageBox(QMessageBox.Warning, '??????', '??????????????????????????????????????????')
                msg_box.exec_()  # ???????????????
                break
            elif teacherId == str(i[2]):
                flag = False
                msg_box = QMessageBox(QMessageBox.Warning, '??????', '?????????????????????????????????????????????')
                msg_box.exec_()  # ???????????????
                break

        # ????????????id?????????????????????
        flag2 = False
        for i in teacherids:
            if teacherId == str(i[0]):
                flag2 = True
                break

        if flag:
            if not account.isdigit():
                msg_box2 = QMessageBox(QMessageBox.Warning, '??????????????????', '??????????????????')
                msg_box2.exec_()  # ???????????????
            elif not flag2:
                msg_box2 = QMessageBox(QMessageBox.Warning, '???????????????', '????????????????????????id')
                msg_box2.exec_()  # ???????????????
            elif secret != SECRET:
                sql3 = "INSERT INTO users values ('{}', '{}', '{}', False, {})".format(username,
                                                                                       account,
                                                                                       password,
                                                                                       teacherId)
                self.query.execute(sql3)
            else:
                sql3 = "INSERT INTO users values ('{}', '{}', '{}', True, {})".format(username,
                                                                                      account,
                                                                                      password,
                                                                                      teacherId)
                self.query.execute(sql3)

