import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="MTT Global Receipt Generator", layout="wide")

# Styling: Dark Theme, Yellow/Gold/White
st.markdown("""
    <style>
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    h1 {color: #FFD700 !important; text-align: center;}
    div[data-baseweb="input"], div[data-baseweb="select"] {background-color: #1E1E1E !important; border: 1px solid #FFD700 !important;}
    label {color: #FFD700 !important; font-weight: bold;}
    .stDataFrame {background-color: #1E1E1E !important;}
    </style>
    """, unsafe_allow_html=True)

st.title("MTT Global Receipt Generator")

# Global Lists
currencies = [
    "USD ($)", "SAR (ر.س)", "PKR (Rs)", "EUR (€)", "GBP (£)", "AED (د.إ)", "INR (₹)", "JPY (¥)", 
    "CAD ($)", "AUD ($)", "CHF (Fr)", "CNY (¥)", "TRY (₺)", "MXN ($)", "BRL (R$)", "SGD ($)", 
    "ZAR (R)", "KRW (₩)", "THB (฿)", "IDR (Rp)", "MYR (RM)", "RUB (₽)", "QAR (ر.ق)", "KWD (د.ك)"
]

languages = [
    "English", "Urdu", "Arabic", "Spanish", "French", "Chinese", "Hindi", "German", 
    "Japanese", "Portuguese", "Russian", "Korean", "Turkish", "Italian", "Bengali", "Indonesian"
]

# Database
if 'sales' not in st.session_state:
    st.session_state.sales = pd.DataFrame(columns=['Date', 'Item', 'Price', 'Currency'])

# Sidebar: Analytics
st.sidebar.header("📊 Sales Analytics")
time_filter = st.sidebar.selectbox("Filter Sales:", ["24 Hours", "1 Week", "15 Days", "30 Days", "1 Year"])

now = datetime.now()
if time_filter == "24 Hours": mask = st.session_state.sales['Date'] >= (now - timedelta(days=1))
elif time_filter == "1 Week": mask = st.session_state.sales['Date'] >= (now - timedelta(weeks=1))
elif time_filter == "15 Days": mask = st.session_state.sales['Date'] >= (now - timedelta(days=15))
elif time_filter == "30 Days": mask = st.session_state.sales['Date'] >= (now - timedelta(days=30))
else: mask = st.session_state.sales['Date'] >= (now - timedelta(days=365))

total_rev = st.session_state.sales[mask]['Price'].sum()
st.sidebar.metric(f"Total Sales ({time_filter})", f"{total_rev:,.2f}")

# Main Layout
col1, col2 = st.columns([1, 2])
with col1:
    logo = st.file_uploader("Upload Shop Logo", type=['png', 'jpg', 'jpeg'])
    if logo: st.image(logo, width=120)
    elif "logo.png": st.image("logo.png", width=120)

with col2:
    shop_name = st.text_input("Enter Shop Name")
    item = st.text_input("Item Name")
    price = st.number_input("Price", min_value=0.0)
    currency = st.selectbox("Select Currency", currencies)
    lang = st.selectbox("Select Language", languages)

# File Handling (800MB limit supported via config.toml)
st.write("---")
uploaded_file = st.file_uploader("Upload Business File (Excel/CSV/Word)", type=['xlsx', 'csv', 'docx'])
if uploaded_file:
    st.success(f"File '{uploaded_file.name}' ready for processing.")

if st.button("Generate & Save Receipt"):
    new_sale = {'Date': now, 'Item': item, 'Price': price, 'Currency': currency}
    st.session_state.sales = pd.concat([st.session_state.sales, pd.DataFrame([new_sale])], ignore_index=True)
    st.success(f"Receipt generated for {shop_name if shop_name else 'Valued Customer'}!")
    st.balloons()

# Table View
st.write("### Recent Transactions")
st.dataframe(st.session_state.sales.sort_values(by='Date', ascending=False))
