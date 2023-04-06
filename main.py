# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 06:37:07 2023
@author: baris
"""

from PyQt5.QtWidgets import QApplication,QMainWindow
import sys, time, serial, data
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from yeristasyonu import Ui_MainWindow
from bağlantı_penceresi_fonksiyon import OtherWindow
import folium
from folium import plugins

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #----------------------------------------------------------------------
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ates_1.setStyleSheet("background-color: red")
        self.ui.ates_2.setStyleSheet("background-color: red")
        #----------------------------------------------------------------------
        #Timer 
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.goster)
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.portread)
        self.timer3 = QtCore.QTimer()
        self.timer3.timeout.connect(self.portSendData)
        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.harita)
        
        #----------------------------------------------------------------------
        #buton fonksiyonları
        self.ui.action_port_ayarlari.triggered.connect(self.port_ayar)
        self.ui.action_baglan.triggered.connect(self.portConnect)
        self.ui.action_baglant_kes.triggered.connect(self.portDisconnect)
        #----------------------------------------------------------------------
        #Tanımlanan değişkenler
        self.irtifa_dizisi = [0,1]
        self.seri_read = None
        self.seri_write = None
        self.ates1 = False
        self.ates2 = False
        self.veriler = None
        self.paket1 = None
        self.paket2 = None
        self.lan1 = 39.925173282115004
        self.lon1 = 32.8368795246721
        self.paraşüt_durum = 0
        #----------------------------------------------------------------------  
        #harita
        coordinate = (self.lan1, self.lon1)  
        m = folium.Map(zoom_start=15,location=coordinate,position="topright")    
        folium.plugins.Fullscreen().add_to(m)
        folium.Marker(location=[self.lan1,self.lon1]).add_to(m)
        data = m._repr_html_()
        self.ui.webEngineView.setHtml(data)
        
    #Pencere kapatılınca(Çarpıya basılınca) çalışan fonksiyon
    def closeEvent(self, a0):
        self.portDisconnect()
        self.close()
    
    #Menü port ayar penceresi oluşturuluyor
    def port_ayar(self):
        self.other_window = OtherWindow()
        self.other_window.show()
    
    #harityı yenilemek için
    def harita(self):
        self.lan1 = float(self.veriler[2])
        self.lon1 = float(self.veriler[3])
        coordinate = (self.lan1, self.lon1)  
        m = folium.Map(zoom_start=15,location=coordinate, position="topright")    
        plugins.Fullscreen().add_to(m)
        folium.Marker(location=[self.lan1,self.lon1]).add_to(m)
        data = m._repr_html_()
        self.ui.webEngineView.setHtml(data)

    #Serial haperleşmeyi ve timeri durdurarak veri alımını veya iletimini kesiyor
    def portDisconnect(self):
        if  self.seri_read or  self.seri_write is not None: 
            if self.seri_read.isOpen():
                self.seri_read.close()
            if self.seri_write.isOpen():
                self.seri_write.close()
        self.timer1.stop()
        self.timer2.stop()
        self.timer3.stop()
        self.timer4.stop()
    
    #veri, grafik, harita güncelleme
    def goster(self):
        self.ui.data_irtifa.setText(self.veriler[0])
        self.ui.data_enlem.setText(self.veriler[2])
        self.ui.data_boylam.setText(self.veriler[3])
        self.ui.data_ivme_x.setText(self.veriler[4])
        self.ui.data_ivme_y.setText(self.veriler[5])
        self.ui.data_ivme_z.setText(self.veriler[6])
        self.ui.data_gyro_x.setText(self.veriler[7])
        self.ui.data_gyro_y.setText(self.veriler[8])
        self.ui.data_gyro_z.setText(self.veriler[9])
        self.ui.data_hiz.setText("0")
        self.irtifa_dizisi.append(float(self.veriler[0]))
        self.ui.examplePlotWidgetCurve.setData(self.irtifa_dizisi)  
            
        if self.veriler[11] == "1":
            self.ates1 == True
            self.ui.ates_1.setStyleSheet("background-color: green")
        if self.veriler[12] == "1":
            self.ates2 == True
            self.ui.ates_1.setStyleSheet("background-color: green")
            
    #porttan gelen verileri okur        
    def portread(self):
        if self.seri_read.inWaiting():
            paket = self.seri_read.readline()
            paket = paket.decode("ISO-8859-1")
            paket = paket.strip("\r\n")
            paket = paket.split(",")
            self.veriler = paket
        else:
            pass
    
    #Porta veri yazıyor 
    def portSendData(self):
        if self.ates1 and self.ates2 == True:
            self.paraşüt_durum = 1
        paket_1, paket_2 = data.paket(int(self.veriler[16]), float(self.veriler[0]), float(self.veriler[1]), float(self.veriler[2]), float(self.veriler[3]), float(self.veriler[13]), float(self.veriler[14]), float(self.veriler[15]), float(self.veriler[4]), float(self.veriler[5]), float(self.veriler[6]), float(self.veriler[7]), float(self.veriler[8]), float(self.veriler[9]), float(self.veriler[10]), self.paraşüt_durum)
        self.seri_write.write(bytearray(paket_1))
        self.seri_write.write(bytearray(paket_2))
    
    #Yazma ve okuma portunu açıyor ve timerı başlatıyor
    def portConnect(self):
        self.seri_read = serial.Serial(self.other_window.port_read, self.other_window.baud_read, timeout=1)
        self.seri_write = serial.Serial(self.other_window.port_write, self.other_window.baud_write, timeout=1)
        time.sleep(5)
        if self.seri_read.isOpen(): 
            QMessageBox.information(window ,"bilgilendirme", "bağlantı gerçekleşti",QMessageBox.Close)
            self.timer()        
        else:
            QMessageBox.warning(window,"hata", "bağlantı gerçekleştirilmedi!",QMessageBox.Close)
            self.portDisconnect()
    #timer fonksiyonu        
    def timer(self):
        self.timer1.start(1000)
        self.timer2.start(50)
        self.timer3.start(200)
        self.timer4.start(10000)  
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())