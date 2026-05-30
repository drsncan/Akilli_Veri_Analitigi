# train.py - 1. Gün: Model Eğitimi
import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("📊 Veri seti yükleniyor...")
data = load_breast_cancer()
X = data.data
y = data.target

# Veriyi eğitim ve test olarak ayırıyoruz (%80 eğitim, %20 test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🧠 Makine Öğrenmesi Modeli (Random Forest) eğitiliyor...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Modelin başarısını test edelim
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"✅ Model başarıyla eğitildi! Doğruluk Oranı (Accuracy): %{accuracy * 100:.2f}")

# Eğitilen modeli API'de kullanmak üzere diske kaydediyoruz
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("💾 Model 'model.pkl' olarak kaydedildi.")