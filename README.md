<div align="center">

# Teknofest Roket Yer İstasyonu Yazılımı

[](https://www.python.org/)
[](https://www.riverbankcomputing.com/software/pyqt/)
[](https://pypi.org/project/pyserial/)
[](https://www.teknofest.org/)

A ground station software for real-time data visualization and telemetry, developed for the Türkiye TEKNOFEST Rocket Competition.

TEKNOFEST Roket Yarışması için geliştirilmiş, gerçek zamanlı veri görselleştirme ve telemetri yer istasyonu yazılımı

---

**🚀 [Ana Aviyonik Kodlarına Erişmek İçin Tıklayın](https://github.com/koesan/Teknofest_roket_ana_aviyonik_kodu)**

</div>

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

## 🚀 Proje Hakkında

Bu yazılım, TEKNOFEST Roket Yarışması için Python ve PyQt5 kullanılarak geliştirilmiş profesyonel bir yer istasyonu uygulamasıdır. Roket ve faydalı yükten gelen telemetri verilerini gerçek zamanlı olarak alır, görselleştirir ve TEKNOFEST'in resmi yer istasyonuna aktarır.

## ✨ Özellikler

- **Gerçek Zamanlı Veri Görselleştirme**
  
  - İrtifa, hız ve ivme grafikleri
  - Gyro (açısal hız) verileri
  - GPS konum takibi
  - Sensör değerlerinin anlık gösterimi
- **Harita Entegrasyonu**
  
  - Folium kütüphanesi ile interaktif harita
  - Roket ve faydalı yük konumlarının canlı takibi
  - GPS koordinatlarının harita üzerinde gösterimi
- **Seri Port İletişimi**
  
  - Arduino/mikrodenetleyici ile seri port bağlantısı
  - Ayarlanabilir baud rate ve port seçenekleri
  - Çift yönlü veri iletişimi
- **TEKNOFEST Veri Formatı**
  
  - Resmi TEKNOFEST protokolüne uygun paket oluşturma
  - Otomatik checksum hesaplama
  - İki paket halinde veri gönderimi
- **Paraşüt Kontrol Sistemi**
  
  - Manuel paraşüt tetikleme butonları
  - Paraşüt durumu göstergesi
  - Güvenlik kilidi mekanizması
- **Modern Kullanıcı Arayüzü**
  
  - PyQt5 ile profesyonel tasarım
  - Qt Designer ile özelleştirilebilir UI
  - Koyu tema ve renkli göstergeler

## 📋 Gereksinimler

**Yazılım Gereksinimleri:**

- Python 3.7 veya üzeri
- PyQt5 5.15.9
- PySerial 3.5
- Folium 0.14.0
- PyQtGraph 0.13.2
- PyQtWebEngine 5.15.6
- 

## 🔧 Kurulum

1. **Gerekli Kütüphaneleri Kurun:**
  
  ```bash
  pip install PyQt5==5.15.9 PySerial==3.5 Folium==0.14.0 PyQtGraph==0.13.2 PyQtWebEngine==5.15.6
  ```
  
2. **Projeyi İndirin:**
  
  ```bash
  git clone https://github.com/kullanici/Teknofest_roket_Yer_istasyonu_yazilimi.git
  cd Teknofest_roket_Yer_istasyonu_yazilimi
  ```
  

## 🎯 Kullanım

### Temel Kullanım

1. **Uygulamayı Başlatın:**
  
  ```bash
  python main.py
  ```
  
2. **Port Ayarları:**
  
  - Menüden "Port Ayarları" seçeneğine tıklayın
  - COM portunu ve baud rate'i seçin
  - "Bağlan" butonuna basın
3. **Veri Görüntüleme:**
  
  - Bağlantı kurulduktan sonra veriler otomatik olarak ekranda gösterilir
  - Grafikler gerçek zamanlı olarak güncellenir
  - Harita üzerinde konum canlı olarak işaretlenir
4. **Paraşüt Kontrolü:**
  
  - İlgili paraşüt butonuna tıklayarak manuel tetikleme yapabilirsiniz
  - Durum göstergeleri paraşüt durumunu gösterir

### Arduino Test Kodu

Projeyi test etmek için `yer_istasyonu_arduino_test_kodu.ino` dosyasını Arduino'ya yükleyebilirsiniz. Bu kod, örnek sensör verileri üretir ve seri port üzerinden gönderir.

## 🛠️ UI Özelleştirme

UI'da değişiklik yapmak için:

1. **Qt Designer ile Aç:**
  
  - `yeristasyonu.ui` veya `bağlantı_penceresi.ui` dosyasını Qt Designer ile açın
  - İstediğiniz değişiklikleri yapın
2. **UI'yi Python Koduna Çevir:**
  
  ```bash
  python ui_to_py.py
  ```
  
3. **Grafik Kodlarını Ekle:**
  
  - `grafik.txt` dosyasındaki kodları kopyalayın
  - `yeristasyonu.py` dosyasına uygun yere yapıştırın

## 📊 Veri Formatı

Sistem, TEKNOFEST'in resmi veri formatına uygun şekilde çalışır:

**Gönderilen Veriler:**

- Takım ID
- Paket numarası (sayaç)
- İrtifa (barometrik)
- GPS irtifası
- Enlem ve boylam
- Faydalı yük GPS verileri
- Gyro X, Y, Z değerleri
- İvme X, Y, Z değerleri
- Açı bilgisi
- Paraşüt durumu
- Checksum

## 🗂️ Dosya Yapısı

```
├── main.py                          # Ana uygulama dosyası
├── yeristasyonu.py                  # Ana pencere UI kodları
├── yeristasyonu.ui                  # Ana pencere UI tasarımı
├── bağlantı_penceresi.py           # Port ayarları UI kodları
├── bağlantı_penceresi.ui           # Port ayarları UI tasarımı
├── bağlantı_penceresi_fonksiyon.py # Port ayarları fonksiyonları
├── data.py                          # TEKNOFEST veri paketi oluşturma
├── ui_to_py.py                      # UI'dan Python'a çevirme scripti
├── grafik.txt                       # Grafik kodları şablonu
├── yer_istasyonu_arduino_test_kodu.ino # Arduino test kodu
└── README.md                        # Bu dosya
```

## 🎓 Teknik Detaylar

**Kullanılan Teknolojiler:**

- **PyQt5** - Grafik arayüz geliştirme
- **PySerial** - Seri port iletişimi
- **Folium** - İnteraktif harita oluşturma
- **PyQtGraph** - Gerçek zamanlı grafik çizimi
- **PyQtWebEngine** - Web tabanlı harita entegrasyonu

**Mimari:**

- MVC (Model-View-Controller) yapısı
- Timer tabanlı periyodik güncelleme
- Thread-safe veri işleme
- Modüler ve genişletilebilir tasarım

---

<div align="center">

### 🎯 İlgili Projeler

**[🚀 Roket Aviyonik Yazılımı](https://github.com/koesan/Teknofest_roket_ana_aviyonik_kodu)**  
Roket aviyonik yazılımıdır. Sensör verilerini işler, paraşüt açma görevini gerçekleştirir ve verileri yer istasyonuna iletir. Bu yazılım, roketin görevini güvenli ve başarılı bir şekilde tamamlamasını sağlayan birçok önemli işlevi yerine getirir.

---

**🚀 TEKNOFEST 2023 Roket Yarışması için geliştirilmiştir. İsteyen herkes kullanabilir ve geliştirebilir. 🇹🇷**

**⭐ Bu proje işinize yaradıysa, yıldız vermeyi unutmayın! ⭐**

</div>
