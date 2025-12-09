\# Customer Shopping Istanbul



\## Proje Açıklaması

Bu proje, İstanbul'daki alışveriş verilerini kullanarak müşterilerin harcama seviyesini (Low, Medium, High) tahmin eden bir makine öğrenimi uygulamasıdır.



\## Kullanılan Veri

\- Dataset: müşteri alışveriş kayıtları (.csv)

\- Feature’lar:

&nbsp; - age

&nbsp; - gender

&nbsp; - category

&nbsp; - quantity

&nbsp; - price

&nbsp; - payment\_method

&nbsp; - shopping\_mall

\- Target: Spending\_level (Low, Medium, High)



\## Pipeline ve Model



1\. \*\*Ön İşleme\*\*

&nbsp;  - Numeric feature: StandardScaler

&nbsp;  - Categorical feature: OneHotEncoder



2\. \*\*Model\*\*

&nbsp;  - Logistic Regression (Optuna ile hiperparametre optimizasyonu yapıldı)



3\. \*\*Train/Validation Split\*\*

&nbsp;  - %80 Train / %20 Validation



Model pipeline `models/model.pkl` olarak kaydedildi ve Streamlit uygulaması ile kullanılabilir.





\## Kullanım



1\. Conda environment’i aktif et:

```bash

conda activate istanbul\_shopping\_env





\## Repo Yapısı

customer\_shopping\_istanbul/

├── data/             # Dataset

├── docs/             # Markdown notlar / kısa doküman

├── models/           # model.pkl

├── notebooks/        # EDA ve final pipeline notebook

├── src/

│   └── app.py        # Streamlit uygulaması

├── README.md

└── requirements.txt





\## İletişim

Proje ile ilgili sorular için: izzetozdemir2022@gmail.com













