
# 💸 Gelir Gider Takip Uygulaması - Flutter & FastAPI

Bu proje, kullanıcıların gelir ve gider verilerini kolayca ekleyip takip edebileceği Flutter tabanlı bir arayüz ve FastAPI tabanlı bir backend içerir.

## 1. Gereksinimler

### 1.1 Backend Gereksinimleri
- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite

### 1.2 Frontend Gereksinimleri
- Flutter 3.x
- Android Studio (IDE)
- VS Code (alternatif olarak)
- Google Chrome (web testi için)

---

## 2. Backend (FastAPI) Geliştirme

### 2.1 Proje Yapısı

```
backend/
│
├── main.py
├── models.py
├── database.py
├── crud.py
└── schemas.py
```

### 2.2 Backend'i Başlatma

```bash
uvicorn main:app --reload
```

> Bu komut terminale yazıldığında, backend sunucusu başlatılır. Tarayıcınızda `http://127.0.0.1:8000` adresini açabilirsiniz.

📸 ![image](https://github.com/user-attachments/assets/fc44137c-009b-45e6-8ed7-b91bcbe6cfd0) Terminalde çıkan sonuç ve bağlantı linki

### 2.3 Swagger UI (API Testi)

`http://127.0.0.1:8000/docs` adresinde Swagger UI otomatik olarak açılır. Buradan API’nizi test edebilirsiniz.

📸 ![image](https://github.com/user-attachments/assets/1c5784f5-ed57-4016-9115-032c1dd95cd0) Swagger arayüzü

---

## 3. Flutter Frontend Geliştirme

### 3.1 Flutter Proje Yapısı

```
lib/
│
├── main.dart
├── pages/
│   ├── home_page.dart
│   └── listele_page.dart
├── services/
│   └── api_service.dart
```

📸 ![image](https://github.com/user-attachments/assets/62089ace-afbc-434d-b99e-0af7d45e2815) `api_service.dart` dosyasından bir kesit

### 3.2 Flutter Web'de Test

1. `main.dart` dosyasına gidin.
2. Sağ altta cihaz listesinden `Chrome` seçin.
3. Sağ üstteki ▶️ (Start Debugging) tuşuna basın.

> Uygulama Chrome üzerinde çalışacaktır.

📸 ![image](https://github.com/user-attachments/assets/53c76b3f-fc01-4d82-bb60-b2bccb71ed87) Chrome üzerinde çalışan Flutter uygulaması

---

## 4. Özellikler

- 🟢 Neon yeşil ve 🔴 neon kırmızı renklerle gelir/gider ayrımı
- Mouse üzerine gelindiğinde animasyon
- Kayıt silme fonksiyonu (çöp kutusu animasyonu)
- Koyu tema UI tasarımı
- Responsive yapı

---

## 5. API Servis Dosyası (`api_service.dart`)

Frontend ile backend arasındaki bağlantıyı sağlar. HTTP istekleri burada tanımlanır.

📸 ![image](https://github.com/user-attachments/assets/ebd2bc8d-c79d-4d22-bc2f-6a71a20472bc) `api_service.dart` içeriği VSCode’da

---

## 6. Test ve Yayına Alma

### 6.1 Flutter Web'de Test Etme

```bash
flutter run -d chrome
```

### 6.2 Android APK Oluşturma

```bash
flutter build apk --release
```

### 6.3 Backend'i Yayına Alma

- Geliştirme: `uvicorn main:app --reload`
- Üretim: `gunicorn` ve `nginx` ile dağıtım

---

## 7. Kurulum Adımları

1. Backend klasörüne geç:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
2. Flutter frontend’i çalıştır:
   ```bash
   cd frontend
   flutter pub get
   flutter run -d chrome
   ```

---

## 8. Lisans

MIT Lisansı © 2025

---

## 9. Geliştirici

📌 GitHub: [github.com/tahaefendy](https://github.com/tahaefendy)

💬 Her türlü soru ve öneriniz için Issues kısmını kullanabilirsiniz.
