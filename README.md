# 🌍 EU27 vs ABD: Enerji Politikaları Analizi

> **Nükleer ve Yenilenebilir Enerji Karşılaştırması**  
> Our World in Data (OWID) gerçek verileri ile Avrupa Birliği ve ABD'nin enerji dönüşüm süreçlerinin analizi

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

## 📋 Proje Hakkında

Bu proje, **Avrupa Birliği (EU27)** ile **ABD**'nin nükleer enerji ve yenilenebilir enerji kullanımının zaman içindeki seyrini analiz eder. **Our World in Data (OWID)** veri setleri kullanılarak gerçek ve güncel verilerle çalışır.

### 🌍 EU27 Nedir?

**EU27**, Avrupa Birliği'nin (European Union) **27 üye ülkesini** temsil eden kısaltmadır. 2020'de Brexit sonrası Birleşik Krallık'ın ayrılmasıyla EU28'den EU27'ye düşmüştür.

#### **EU27 Üye Ülkeleri:**

**Batı Avrupa:** Fransa, Almanya, İtalya, İspanya, Portekiz, Belçika, Hollanda, Lüksemburg, İrlanda

**Kuzey Avrupa:** İsveç, Danimarka, Finlandiya, Estonya, Letonya, Litvanya

**Orta Avrupa:** Avusturya, Çek Cumhuriyeti, Slovakya, Slovenya, Macaristan, Polonya

**Güney Avrupa:** Yunanistan, Hırvatistan, Romanya, Bulgaristan, Malta, Kıbrıs

#### **Enerji Analizinde EU27:**
Projemizde EU27 verisi, bu 27 ülkenin **toplam enerji tüketimi** ve **enerji karışımını** temsil eder. EU27, ABD ile karşılaştırıldığında **yenilenebilir enerji** ve **düşük karbon** konularında daha ileride durmaktadır.

### 🎯 Ana Amaçlar
- EU27 ve ABD'nin enerji politikalarının karşılaştırmalı analizi
- Nükleer enerji kullanım trendlerinin incelenmesi
- Yenilenebilir enerji gelişiminin analizi
- Düşük karbon geçiş süreçlerinin değerlendirilmesi

## 📊 Analiz Sonuçları (2024)

| Enerji Kaynağı | EU27 | ABD | Fark |
|----------------|------|-----|------|
| **Nükleer Enerji** | 10.1% | 7.6% | EU27 +2.5% |
| **Yenilenebilir Enerji** | 22.3% | 12.1% | EU27 +10.2% |
| **Düşük Karbon (Toplam)** | 32.4% | 19.7% | EU27 +12.7% |
| **Fosil Yakıt** | 67.6% | 80.3% | EU27 -12.7% |

### 🔍 Trend Analizi (2015-2024)

#### EU27
- **Nükleer**: 11.8% → 10.1% (▼ -1.7%)
- **Yenilenebilir**: 14.2% → 22.3% (▲ +8.1%)

#### ABD
- **Nükleer**: 8.3% → 7.6% (▼ -0.7%)
- **Yenilenebilir**: 7.2% → 12.1% (▲ +4.9%)

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- pip (Python paket yöneticisi)
- Git

### Adım Adım Kurulum

```bash
# 1. Projeyi klonlayın
git clone https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-.git
cd energy-nuclear-renewable-analysis-

# 2. Sanal ortam oluşturun ve aktifleştirin
make install

# 3. Verileri indirin
make data

# 4. Verileri işleyin
make process
```

## 📁 Proje Yapısı

```
energy-nuclear-renewable-analysis-/
├── 📊 data/                    # Veri dosyaları
│   ├── raw/                   # OWID'den indirilen ham veriler
│   └── processed/             # İşlenmiş veriler
├── 📝 notebooks/              # Jupyter not defterleri
│   └── shale_gas_triple_analysis.ipynb  # 3'lü karşılaştırma analizi
├── 🔧 scripts/                # Python scriptleri
│   ├── download_data.py       # Veri indirme scripti
│   ├── process_data.py        # Veri işleme scripti
│   ├── shale_gas_analysis.py  # Kapsamlı kaya gazı analizi
│   ├── simple_shale_gas_analysis.py  # Basit kaya gazı analizi
│   └── triple_comparison_analysis.py  # 3'lü karşılaştırma analizi
├── 📈 reports/                # Analiz raporları ve grafikler
│   ├── comprehensive_energy_analysis.png  # Kapsamlı enerji analizi
│   ├── energy_analysis.png    # Enerji analizi
│   ├── triple_comparison_analysis.png  # 3'lü karşılaştırma
│   ├── shale_gas_impact.png   # Kaya gazı etkisi
│   ├── shale_gas_analysis.png # Kaya gazı analizi
│   └── simple_gas_analysis.png # Basit gaz analizi
├── 📋 requirements.txt        # Python bağımlılıkları
├── ⚙️ Makefile                # Otomatik işlemler
└── 📖 README.md               # Bu dosya
```

## 🛠️ Kullanım

### Temel Komutlar

```bash
# Sanal ortamı aktifleştir
source .venv/bin/activate

# Veri güncelleme
make data          # OWID'den yeni veri indir
make process       # Verileri işle ve analiz için hazırla

# Jupyter Lab başlat
make notebook

# Rapor üretimi
make report        # HTML rapor oluştur

# Kaya gazı analizi
python scripts/shale_gas_analysis.py          # Kapsamlı kaya gazı analizi
python scripts/triple_comparison_analysis.py  # 3'lü karşılaştırma analizi
```

### Manuel Veri İndirme

```bash
# Sadece veri indirme
python scripts/download_data.py

# Sadece veri işleme
python scripts/process_data.py
```

## 📊 Veri Kaynakları

### Our World in Data (OWID)
- **Enerji Verileri**: [energy-data](https://github.com/owid/energy-data)
- **CO2 Verileri**: [co2-data](https://github.com/owid/co2-data)
- **Ana Site**: [ourworldindata.org/energy](https://ourworldindata.org/energy)

### Veri Kalitesi
- ✅ **Oxford Üniversitesi** projesi
- ✅ **Açık kaynak** metodoloji
- ✅ **Güncel veriler** (1900-2024)
- ✅ **Uluslararası standartlar**
- ✅ **Akademik araştırmalarda** kullanılıyor

## 🔬 Analiz Metodolojisi

### Veri İşleme Süreci
1. **Ham Veri İndirme**: OWID GitHub depolarından otomatik indirme
2. **Veri Temizleme**: Eksik değerler ve tutarsızlıkların giderilmesi
3. **Veri Dönüştürme**: EU27 ve ABD için karşılaştırmalı veri seti oluşturma
4. **Analiz**: Zaman serisi analizi ve trend hesaplamaları

### Kullanılan Teknolojiler
- **Pandas**: Veri manipülasyonu ve analizi
- **Matplotlib/Seaborn**: Görselleştirme
- **NumPy**: Sayısal hesaplamalar
- **Jupyter**: İnteraktif analiz

## 📈 Sonuçlar ve Yorumlar

### EU27'nin Avantajları
- **Yenilenebilir enerji liderliği** (%22.3)
- **Daha hızlı düşük karbon geçişi** (%32.4)
- **Güçlü politika desteği** ve hedefler

### ABD'nin Durumu
- **Yenilenebilir enerji potansiyeli** var
- **Nükleer enerji konusunda muhafazakar** yaklaşım
- **Federal seviyede** tutarlı politika ihtiyacı

### Politika Önerileri
1. **EU27**: Mevcut nükleer reaktörlerin ömür uzatımı
2. **ABD**: Yeni nesil nükleer teknolojiler ve yenilenebilir altyapı
3. **Her iki bölge**: 2050 karbon nötr hedefleri için agresif politikalar

## ⛽ Kaya Gazı (Shale Gas) Analizi

### 🔍 Üçlü Karşılaştırma: Nükleer, Yenilenebilir ve Kaya Gazı

Bu proje artık **kaya gazı (shale gas)** analizini de içermektedir. OWID veri setinde doğal gaz verileri kullanılarak kaya gazı etkisi analiz edilmiştir.

#### 📊 Kaya Gazı Analiz Sonuçları

| Analiz Türü | Açıklama |
|-------------|----------|
| **Shale Gas Revolution (2008)** | ABD'de kaya gazı üretiminin başlangıcı |
| **Pre-2008 vs Post-2008** | Kaya gazı öncesi ve sonrası karşılaştırması |
| **EU27 vs ABD Gas Trends** | Doğal gaz kullanım trendlerinin karşılaştırması |

#### 📈 Yeni Notebook: `shale_gas_triple_analysis.ipynb`

**İçerik:**
- 🌍 **Nükleer Enerji Trendi**: EU27 vs ABD (1990-2024)
- 🌱 **Yenilenebilir Enerji Gelişimi**: Paris Anlaşması etkisi
- ⛽ **Doğal Gaz (Kaya Gazı Proxy)**: Shale Gas Revolution etkisi
- 📊 **2024 Enerji Karışımı**: 3'lü karşılaştırma
- 📋 **İstatistiksel Özet**: Detaylı analiz sonuçları

**Özellikler:**
- ✅ **İki Dilli**: İngilizce ve Türkçe açıklamalar
- ✅ **Görselleştirme**: 4 farklı grafik türü
- ✅ **Interaktif**: Jupyter Notebook formatında
- ✅ **Veri Odaklı**: Gerçek OWID verileri ile

#### 🛠️ Yeni Scriptler

1. **`scripts/shale_gas_analysis.py`**: Kapsamlı kaya gazı analizi
2. **`scripts/simple_shale_gas_analysis.py`**: Basit kaya gazı analizi
3. **`scripts/triple_comparison_analysis.py`**: 3'lü karşılaştırma analizi

#### 📊 Yeni Raporlar

- `reports/triple_comparison_analysis.png`: 3'lü karşılaştırma grafiği
- `reports/shale_gas_impact.png`: Kaya gazı etkisi analizi
- `reports/shale_gas_analysis.png`: Kapsamlı kaya gazı analizi
- `reports/simple_gas_analysis.png`: Basit gaz analizi

### 🎯 Kaya Gazı Analizinin Amacı

1. **ABD Shale Gas Revolution**'ın enerji karışımına etkisini anlamak
2. **EU27 ve ABD** arasındaki doğal gaz kullanım farklarını analiz etmek
3. **Nükleer, Yenilenebilir ve Gaz** enerji kaynaklarının 3'lü karşılaştırmasını yapmak
4. **Enerji politikalarının** farklı yakıt türlerine etkisini değerlendirmek

## 🤝 Katkıda Bulunma

Bu proje açık kaynak! Katkılarınızı bekliyoruz:

1. **Fork** yapın
2. **Feature branch** oluşturun (`git checkout -b feature/amazing-feature`)
3. **Commit** yapın (`git commit -m 'Add amazing feature'`)
4. **Push** yapın (`git push origin feature/amazing-feature`)
5. **Pull Request** oluşturun

## 📝 Lisans

Bu proje [MIT License](LICENSE) altında lisanslanmıştır.

## 👥 Yazar

**Zeynep Ruveyda** - [GitHub](https://github.com/ZeynepRuveyda)

## 🙏 Teşekkürler

- **Our World in Data** ekibine veri setleri için
- **Oxford Üniversitesi**'ne OWID projesi için
- **Açık kaynak topluluğu**na

## 📞 İletişim

- **GitHub Issues**: [Repo Issues](https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-/issues)
- **GitHub Discussions**: [Repo Discussions](https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-/discussions)

---

⭐ **Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!** ⭐

*Son güncelleme: Ağustos 2025*

