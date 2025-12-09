import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(page_title="Shopping Spending Level Predictor", layout="centered")
st.title("🛍️ Shopping Spending Level Prediction App")
st.write("Müşteri bilgilerini girerek harcama seviyesini tahmin edin.")

# -------------------------
# 1️⃣ GİRİŞ FORMU
# -------------------------
st.header("📋 Müşteri Bilgisi Girişi")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender", ['Male', 'Female'])
    category = st.selectbox("Category", [
        'Clothing', 'Electronics', 'Food', 'Cosmetics', 'Shoes', 'Accessories'
    ])
    quantity = st.number_input("Quantity", min_value=1, max_value=50, value=1)

with col2:
    price = st.number_input("Price", min_value=1.0, max_value=20000.0, value=100.0)
    payment_method = st.selectbox("Payment Method", [
        'Credit Card', 'Cash', 'E-Wallet', 'Debit Card'
    ])
    shopping_mall = st.selectbox("Shopping Mall", [
        'Mall of Istanbul', 'Aqua Florya', 'Cevahir', 'Forum Istanbul', 
        'Emaar Square', 'Kanyon'
    ])

# -------------------------
# 2️⃣ FEATURE ENGINEERING
# -------------------------
st.header("⚙️ Otomatik Feature Engineering")

total_spent = quantity * price
avg_price = total_spent / quantity
mall_variety = 1   # Placeholder

st.write(f"**Total Spent:** {total_spent}")
st.write(f"**Average Price:** {avg_price}")
st.write(f"**Mall Variety:** {mall_variety}")

# -------------------------
# 3️⃣ MODEL YÜKLEME
# -------------------------
model = joblib.load("../models/model.pkl")

# Input dataframe
input_df = pd.DataFrame([{
    "age": age,
    "quantity": quantity,
    "price": price,
    "gender": gender,
    "category": category,
    "payment_method": payment_method,
    "shopping_mall": shopping_mall
}])

# -------------------------
# 4️⃣ TAHMİN BUTONU
# -------------------------
st.header("🔮 Spending Level Tahmini")

if st.button("Tahmin Al"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Spending Level: {prediction[0]}")

st.write("---")
st.write("📌 *Bu uygulama makine öğrenimi tabanlı harcama seviyesi tahmini yapacaktır.*")
