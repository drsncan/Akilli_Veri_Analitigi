# app.py - Kurşun Geçirmez Versiyon
from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
import traceback

app = Flask(__name__)

model = None
hata_mesaji = "Bilinmeyen bir hata oluştu."

# Dosya yolunu Azure'un dizin yapısına uygun hale getiriyoruz
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')

# Modeli güvenli bir şekilde yüklemeyi deniyoruz (Uygulamanın çökmesini engeller)
try:
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        hata_mesaji = "Yok, sistem kusursuz çalışıyor."
    else:
        hata_mesaji = f"Dosya bulunamadı! Aranan yol: {model_path}"
except Exception as e:
    hata_mesaji = f"Model yüklenirken kod hatası: {str(e)}\n{traceback.format_exc()}"


@app.route('/', methods=['GET'])
def home():
    # Eğer model yüklenemediyse bize hatayı açıkça göstersin
    if model is None:
        return jsonify({
            "durum": "KRİTİK HATA",
            "mesaj": "Model yüklenemediği için API başlatılamadı.",
            "detay": hata_mesaji
        })
        
    return jsonify({
        "mesaj": "Akıllı Veri Analitiği API'sine Hoş Geldiniz!",
        "durum": "Aktif",
        "kullanim": "Tahmin yapmak için /predict endpoint'ine POST isteği atın.",
        "model_yolu": model_path
    })

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"durum": "basarisiz", "hata": "Sunucuda model bulunmuyor."})

    try:
        data = request.get_json()
        features = data['features']
        
        prediction = model.predict(np.array([features]))
        sonuc = "İyi Huylu (Benign)" if prediction[0] == 1 else "Kötü Huylu (Malignant) - Riskli"
        
        return jsonify({"tahmin": sonuc, "durum": "basarili"})
    except Exception as e:
        return jsonify({"hata": str(e), "durum": "basarisiz"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)