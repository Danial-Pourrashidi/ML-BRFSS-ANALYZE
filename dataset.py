import pandas as pd
import numpy as np

def generate_synthetic_brfss(num_samples=2000, output_file='brfss2024.csv'):
    """
    Kocaeli Üniversitesi Makine Öğrenmesi projesi için BRFSS formatında
    sentetik bir test veri seti oluşturan fonksiyon.
    Gerçek veri setindeki eksik değerler (NaN) ve özel kodlar (7, 9 vb.) 
    bilinçli olarak modele test amaçlı eklenmiştir.
    """
    print(f"{num_samples} satırlık sentetik BRFSS verisi oluşturuluyor...")
    np.random.seed(42)

    # _BMI5: Vücut Kitle İndeksi (BRFSS'de 2 ondalık tam sayı olarak tutulur, örn 28.50 -> 2850)
    # Sağlıklı, kilolu ve obez dağılımlarını simüle etmek için normal dağılım
    bmi = np.random.normal(loc=2800, scale=600, size=num_samples)
    
    # EXERANY2: Son 30 günde egzersiz yapma durumu
    # 1: Evet, 2: Hayır, 7: Bilmiyorum, 9: Reddedildi, np.nan: Boş
    exerany2 = np.random.choice(
        [1, 2, 7, 9, np.nan], 
        size=num_samples, 
        p=[0.65, 0.25, 0.03, 0.02, 0.05]
    )

    # FRUIT2: Günde/Haftada/Ayda meyve tüketimi (101: Günde 1, 202: Haftada 2 vb. 300: Hiç, 777/999: Hata)
    fruit2 = np.random.choice(
        [101, 102, 105, 201, 202, 205, 300, 777, 999, np.nan], 
        size=num_samples,
        p=[0.2, 0.2, 0.1, 0.15, 0.1, 0.1, 0.1, 0.02, 0.01, 0.02]
    )

    # VEGETAB2: Sebze tüketimi (Benzer mantık)
    vegetab2 = np.random.choice(
        [101, 102, 105, 201, 202, 205, 300, 777, 999, np.nan], 
        size=num_samples,
        p=[0.15, 0.25, 0.1, 0.15, 0.1, 0.1, 0.1, 0.02, 0.01, 0.02]
    )

    # PA1MIN_: Haftalık fiziksel aktivite dakikası
    # Ortalama 150 dakika, standart sapma 80
    pa1min = np.random.normal(loc=150, scale=80, size=num_samples)
    # Negatif dakikaları sıfırla
    pa1min = np.clip(pa1min, 0, None)
    # Rastgele bazı değerleri NaN yap (Ölçülmemiş)
    pa1min[np.random.choice([True, False], size=num_samples, p=[0.05, 0.95])] = np.nan

    # DataFrame oluşturma
    df = pd.DataFrame({
        '_BMI5': np.round(bmi),
        'EXERANY2': exerany2,
        'FRUIT2': fruit2,
        'VEGETAB2': vegetab2,
        'PA1MIN_': np.round(pa1min)
    })

    # Dosyayı kaydetme
    df.to_csv(output_file, index=False)
    print(f"Veri boyutu: {df.shape}")