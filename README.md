# 🧠 Akıllı Veri Analitiği ve Makine Öğrenmesi API

Bu proje, Bulut Bilişim dersi kapsamında Scikit-learn ile eğitilmiş bir makine öğrenmesi modelinin (Göğüs Kanseri Teşhis) Flask API kullanılarak bulut ortamında (Azure) barındırılmasını sağlamaktadır.

## 📅 Proje Günlüğü

### 1. Gün: Model Eğitimi ve Yerel API Kurulumu
* Python ve Scikit-learn kullanılarak Random Forest sınıflandırma modeli eğitildi.
* Modelin doğruluk oranı test edildi ve bulutta kullanılmak üzere `.pkl` formatında diske kaydedildi.
* Flask framework'ü kullanılarak modelin dışarıdan JSON verisi alıp tahmin üretebileceği bir RESTful API (`app.py`) oluşturuldu.
* **Sonraki Adım:** Uygulamanın Azure App Service üzerine dağıtılması (Deployment).