# Yer İstasyonu Yazılımı (Ground Station)

![Ground Station Banner](assets/banner.png)

<div align="center">

![Language](https://img.shields.io/badge/Language-Python%203-blue)
![GUI](https://img.shields.io/badge/Framework-PyQt5-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

## 📌 Hakkında
Bu proje, **Teknofest Roket Yarışması** kapsamında geliştirilen roketin uçuş verilerini (telemetri) anlık olarak almak, görselleştirmek ve kaydetmek için tasarlanmış profesyonel bir yer istasyonu yazılımıdır. Roket ve faydalı yükten gelen telemetri verilerini gerçek zamanlı olarak alır, TEKNOFEST'in resmi yer istasyonuna aktarır ve görselleştirir.

---

## 📸 Ekran Görüntüleri

<table align="center">
  <tr>
    <td align="center">
      <img src="https://user-images.githubusercontent.com/96130124/230311087-ecfb6409-4e6f-4962-84a1-6cf7552a0008.png" alt="Ana Ekran" width="700"/>
      <br/>
      <b>Ana Kontrol Paneli</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://user-images.githubusercontent.com/96130124/230311111-53267551-550e-41d4-b866-f125eb5ca949.png" alt="Bağlantı Ekranı" width="700"/>
      <br/>
      <b>Port Bağlantı Ayarları</b>
    </td>
  </tr>
</table>

---

## ✨ Özellikler

- **Gerçek Zamanlı Veri Görselleştirme**
  - İrtifa, hız, ivme ve sıcaklık grafikleri
  - Gyro (açısal hız) verileri
  - Sensör değerlerinin anlık gösterimi
- **Harita Entegrasyonu**
  - Folium kütüphanesi ile interaktif harita
  - Roket ve faydalı yük konumlarının canlı takibi
- **Seri Port İletişimi**
  - XBee/LoRa modülleri üzerinden veri okuma
  - Ayarlanabilir baud rate ve port seçenekleri
- **TEKNOFEST Veri Formatı**
  - Resmi protokole uygun paket oluşturma ve checksum hesaplama
- **Durum Takibi**
  - Roket durumunu (Rampa, Yükselme, Paraşüt, İniş) izleme
  - Manuel paraşüt tetikleme kontrolleri

## 🛠 Gereksinimler

Proje aşağıdaki Python kütüphanelerini kullanır (detaylar için `requirements.txt`):
- `Python 3.7+`
- `PyQt5`: Grafik Arayüz (GUI)
- `PySerial`: Seri Port iletişimi
- `Folium`: Harita
- `PyQtGraph`: Gerçek zamanlı grafikler
- `PyQtWebEngine`: Harita motoru

## 📥 Kurulum & Çalıştırma

1. **Repoyu Klonlayın**:
   ```bash
   git clone https://github.com/bahattinyunus/Teknofest_roket_Yer_istasyonu_yazilimi.git
   cd Teknofest_roket_Yer_istasyonu_yazilimi
   ```

2. **Bağımlılıkları Yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı Başlatın**:
   ```bash
   python main.py
   ```
   *(Alternatif olarak `python yeristasyonu.py`)*

## 🎯 Kullanım

1. **Port Ayarları**: Menüden COM portunu ve Baud Rate'i seçip "Bağlan" deyin.
2. **İzleme**: Bağlantı sonrası veriler grafiklere ve haritaya otomatik akar.
3. **Kontrol**: Paraşüt tetikleme butonları aktif hale gelir.

## 🗂️ Dosya Yapısı

```
├── main.py                          # Ana uygulama dosyası
├── yeristasyonu.py                  # Ana pencere UI mantığı
├── bağlantı_penceresi.py           # Port ayarları mantığı
├── data.py                          # Veri paketleme ve protokol
├── assets/                          # Görsel varlıklar (Banner vb.)
└── requirements.txt                 # Bağımlılık listesi
```

## 🎓 Teknik Detaylar
- **Mimari**: MVC (Model-View-Controller) yapısı
- **İş Parçacığı**: Thread-safe veri işleme ve GUI güncelleme

## 🤝 Katkıda Bulunma
Katkılarınızı bekliyoruz! Lütfen `CONTRIBUTING.md` dosyasını inceleyin.

## 📄 Lisans
Bu proje **MIT Lisansı** ile korunmaktadır. Detaylar için `LICENSE` dosyasına bakınız.

---

<div align="center">

### 🔗 İlgili Projeler
**[🚀 Roket Aviyonik Yazılımı](https://github.com/koesan/Teknofest_roket_ana_aviyonik_kodu)**

*Bu proje Teknofest Roket Yarışması için geliştirilmiştir.*
**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

</div>
