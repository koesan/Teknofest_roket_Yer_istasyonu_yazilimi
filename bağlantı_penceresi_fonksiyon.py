# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 06:37:07 2023
@author: baris
"""

#bağlantı penceresine işlev ekleme

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtSerialPort import QSerialPortInfo
from bağlantı_penceresi import  Ui_OtherWindow

class OtherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.other_window = Ui_OtherWindow()
        self.ui_other = Ui_OtherWindow()
        self.ui_other.setupUi(self)
        self.listSerialPorts()
        self.ui_other.tamam.clicked.connect(self.get_arguman)
        

    def get_arguman(self):
        self.port_read = str(self.ui_other.com.currentText())
        self.baud_read = str(self.ui_other.bound.currentText())
        self.port_write = str(self.ui_other.com_2.currentText())
        self.baud_write = str(self.ui_other.bound_2.currentText())
        self.close()
        
        
    def listSerialPorts(self):
        self.ui_other.com.clear()
        self.ui_other.com_2.clear()
        serialPortInfo=QSerialPortInfo()
        for serialPort in serialPortInfo.availablePorts():
            self.ui_other.com.addItem(serialPort.portName())
            self.ui_other.com_2.addItem(serialPort.portName())