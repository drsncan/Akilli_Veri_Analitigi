# app.py - 1. Gün: Flask API Kurulumu
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Eğitilmiş modeli yüklüyoruz
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mesaj": "Akıllı Veri Analitiği API'sine Hoş Geldiniz!",
        "durum": "Aktif",
        "kullanim": "Tahmin yapmak için /predict endpoint'ine POST isteği atın."
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Kullanıcıdan gelen JSON verisini alıyoruz
        data = request.get_json()
        features = data['features']
        
        # Modeli kullanarak tahmin yapıyoruz
        prediction = model.predict(np.array([features]))
        
        # Sonucu (0: Kötü Huylu/Malignant, 1: İyi Huylu/Benign) string'e çeviriyoruz
        sonuc = "İyi Huylu (Benign)" if prediction[0] == 1 else "Kötü Huylu (Malignant) - Riskli"
        
        return jsonify({"tahmin": sonuc, "durum": "basarili"})
    except Exception as e:
        return jsonify({"hata": str(e), "durum": "basarisiz"})

if __name__ == '__main__':
    # Bulut dağıtımı için host '0.0.0.0' olmalı
    app.run(host='0.0.0.0', port=5000, debug=True)