import streamlit as st
import pandas as pd

st.title("Global Receipt Generator")

# 1. Excel/CSV Upload Feature
st.subheader("Upload Rate List (Optional)")
uploaded_file = st.file_uploader("Upload your item list (Excel or CSV)", type=['csv', 'xlsx'])

# 2. Global Currencies List
currencies = [
    "SAR (Saudi Riyal)", "PKR (Pakistani Rupee)", "USD (US Dollar)", 
    "EUR (Euro)", "GBP (British Pound)", "CNY (Chinese Yuan)", 
    "AED (UAE Dirham)", "INR (Indian Rupee)", "TRY (Turkish Lira)", 
    "JPY (Japanese Yen)", "CAD (Canadian Dollar)", "AUD (Australian Dollar)"
]

# Inputs
shop_name = st.text_input("Shop Name / 店铺名称")
customer_name = st.text_input("Customer Name / 客户姓名")
item = st.text_input("Item Name / 商品名称")
price = st.number_input("Price / 价格", min_value=0.0)
currency = st.selectbox("Select Currency / 选择货币", currencies)

if st.button("Generate Receipt / 生成收据"):
    receipt = f"""
    --- RECEIPT / 收据 ---
    Shop: {shop_name}
    Customer: {customer_name}
    Item: {item}
    Price: {price} {currency}
    --- Thank You / 谢谢 ---
    """
    st.text(receipt)
