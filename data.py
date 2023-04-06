# -*- coding: utf-8 -*-

#teknofestin yer istasyonu veri formatı'nın python kodu

import struct

sayac = 0

def float_to_byte(x):
    x = bytearray(struct.pack("f", x))  
    #[x] = struct.unpack('f', ba) byte ı float yapar
    return x
    
def toplam_hesapla(olusturalacak_paket):
    toplam = 0
    i = 4
    while i<75:
        toplam += olusturalacak_paket[i]
        i+=1
        
    return toplam % 256; 

def paket(takım_id,irtifa,gps_irtifa,enlem,boylam,faydalıyük_gps_irtifa,faydalıyük_enlem,faydalıyük_boylam,gyro_x,gyro_y,gyro_z,ivme_x,ivme_y,ivme_z,açı,paraşüt_durum):
   global sayac
   
   olusturalacak_paket = []
   olusturalacak_paket_1 = []
   olusturalacak_paket_2 = []
   olusturalacak_paket.append(0xFF)
   olusturalacak_paket.append(0xFF)
   olusturalacak_paket.append(0x54) 
   olusturalacak_paket.append(0x52)
    
   olusturalacak_paket.append(takım_id)
   olusturalacak_paket.append(sayac)
   
   if sayac == 255:
       sayac = 0
   else:
       sayac += 1
   
   irtifa = float_to_byte(irtifa)
   olusturalacak_paket.append(irtifa[0])
   olusturalacak_paket.append(irtifa[1])
   olusturalacak_paket.append(irtifa[2])
   olusturalacak_paket.append(irtifa[3])
    
   gps_irtifa = float_to_byte(gps_irtifa)
   olusturalacak_paket.append(gps_irtifa[0])
   olusturalacak_paket.append(gps_irtifa[1])
   olusturalacak_paket.append(gps_irtifa[2])
   olusturalacak_paket.append(gps_irtifa[3])
    
   enlem = float_to_byte(enlem)
   olusturalacak_paket.append(enlem[0])
   olusturalacak_paket.append(enlem[1])
   olusturalacak_paket.append(enlem[2])
   olusturalacak_paket.append(enlem[3])
    
   boylam = float_to_byte(boylam)
   olusturalacak_paket.append(boylam[0])
   olusturalacak_paket.append(boylam[1])
   olusturalacak_paket.append(boylam[2])
   olusturalacak_paket.append(boylam[3])
    
   faydalıyük_gps_irtifa = float_to_byte(faydalıyük_gps_irtifa)
   olusturalacak_paket.append(faydalıyük_gps_irtifa[0])
   olusturalacak_paket.append(faydalıyük_gps_irtifa[1])
   olusturalacak_paket.append(faydalıyük_gps_irtifa[2])
   olusturalacak_paket.append(faydalıyük_gps_irtifa[3])
    
   faydalıyük_enlem = float_to_byte(faydalıyük_enlem)
   olusturalacak_paket.append(faydalıyük_enlem[0])
   olusturalacak_paket.append(faydalıyük_enlem[1])
   olusturalacak_paket.append(faydalıyük_enlem[2])
   olusturalacak_paket.append(faydalıyük_enlem[3])
    
   faydalıyük_boylam = float_to_byte(faydalıyük_boylam)
   olusturalacak_paket.append(faydalıyük_boylam[0])
   olusturalacak_paket.append(faydalıyük_boylam[1])
   olusturalacak_paket.append(faydalıyük_boylam[2])
   olusturalacak_paket.append(faydalıyük_boylam[3])

   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
    
   olusturalacak_paket.append(0x00)
   
   
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
    
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
   olusturalacak_paket.append(0x00)
    
   gyro_x = float_to_byte(gyro_x)
   olusturalacak_paket.append(gyro_x[0])
   olusturalacak_paket.append(gyro_x[1])
   olusturalacak_paket.append(gyro_x[2])
   olusturalacak_paket.append(gyro_x[3])
    
   gyro_y = float_to_byte(gyro_y)
   olusturalacak_paket.append(gyro_y[0])
   olusturalacak_paket.append(gyro_y[1])
   olusturalacak_paket.append(gyro_y[2])
   olusturalacak_paket.append(gyro_y[3])
    
   gyro_z = float_to_byte(gyro_z)
   olusturalacak_paket.append(gyro_z[0])
   olusturalacak_paket.append(gyro_z[1])
   olusturalacak_paket.append(gyro_z[2])
   olusturalacak_paket.append(gyro_z[3])
    
   ivme_x = float_to_byte(ivme_x)
   olusturalacak_paket.append(ivme_x[0])
   olusturalacak_paket.append(ivme_x[1])
   olusturalacak_paket.append(ivme_x[2])
   olusturalacak_paket.append(ivme_x[3])
    
   ivme_y = float_to_byte(ivme_y)
   olusturalacak_paket.append(ivme_y[0])
   olusturalacak_paket.append(ivme_y[1])
   olusturalacak_paket.append(ivme_y[2])
   olusturalacak_paket.append(ivme_y[3])
    
   ivme_z = float_to_byte(ivme_z)
   olusturalacak_paket.append(ivme_z[0])
   olusturalacak_paket.append(ivme_z[1])
   olusturalacak_paket.append(ivme_z[2])
   olusturalacak_paket.append(ivme_z[3])
   
   açı = float_to_byte(açı)
   olusturalacak_paket.append(açı[0])
   olusturalacak_paket.append(açı[1])
   olusturalacak_paket.append(açı[2])
   olusturalacak_paket.append(açı[3])
    
   olusturalacak_paket.append(paraşüt_durum) # Durum bilgisi = Iki parasut de tetiklenmedi
     
   olusturalacak_paket.append(toplam_hesapla(olusturalacak_paket)) # Check_sum = check_sum_hesapla()
   olusturalacak_paket.append(0x0D) #Sabit
   olusturalacak_paket.append(0x0A) # Sabit
   
   olusturalacak_paket_1 = olusturalacak_paket[:39]
   olusturalacak_paket_2 = olusturalacak_paket[39:]
   return olusturalacak_paket_1, olusturalacak_paket_2
