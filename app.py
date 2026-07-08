import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import docx

# Page Config
st.set_page_config(page_title="MTT Global Business Hub", layout="wide")

# Styling: Dark Theme + Golden Accents
st.markdown("""
    <style>
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    h1 {color: #FFD700 !important; text-align: center;}
    div[data-baseweb="input"], div[data-baseweb="select"] {background-color: #1E1E1E !important; border: 1px solid #FFD700 !important;}
    label {color: #FFD700 !important; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

st.title("MTT Global Business Hub 🌍")

# Global Data Lists
currencies = ["USD ($)", "SAR (ر.س)", "PKR (Rs)", "EUR (€)", "GBP (£)", "AED (د.إ)", "INR (₹)", "JPY (¥)", "CAD ($)", "AUD ($)", "MXN ($)"]
languages = ["English", "Urdu", "Arabic", "Spanish", "French", "Chinese", "Hindi", "German", "Turkish", "Russian"]

# Database Init
if 'sales' not in st.session_state:
    st.session_state.sales = pd.DataFrame(columns=['Date', 'Item', 'Rate', 'Qty', 'Total', 'Currency'])

# Dual Layout
col_receipt, col_dash = st.columns([1, 1])

# --- LEFT COLUMN: RECEIPT GENERATOR ---
with col_receipt:
    st.header("🧾 Create Receipt")
    logo = st.file_uploader("Upload Logo", type=['png', 'jpg'])
    shop_name = st.text_input("Shop Name")
    prod_file = st.file_uploader("Upload Product File (Excel/CSV/Word)", type=['xlsx', 'csv', 'docx'])
    
    product_name = st.text_input("Product Name")
    rate = st.number_input("Rate", min_value=0.0)
    qty = st.number_input("Quantity", min_value=1)
    currency = st.selectbox("Currency", currencies)
    lang = st.selectbox("Language", languages)
    
    if st.button("Generate Receipt"):
        total = rate * qty
        new_entry = {'Date': datetime.now(), 'Item': product_name, 'Rate': rate, 'Qty': qty, 'Total': total, 'Currency': currency}
        st.session_state.sales = pd.concat([st.session_state.sales, pd.DataFrame([new_entry])], ignore_index=True)
        st.success("Receipt Created!")

# --- RIGHT COLUMN: CHECK & BALANCE ---
with col_dash:
    st.header("📊 Check & Balance")
    if not st.session_state.sales.empty:
        st.dataframe(st.session_state.sales)
        st.metric("Total Revenue", f"{st.session_state.sales['Total'].sum():,.2f}")
    else:
        st.info("Sales history empty.")
