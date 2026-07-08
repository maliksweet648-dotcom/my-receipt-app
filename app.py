import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="MTT Global Business Hub", layout="wide")

# Styling
st.markdown("""
    <style>
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    h1 {color: #FFD700 !important; text-align: center;}
    </style>
    """, unsafe_allow_html=True)

st.title("MTT Global Business Hub 🌍")

# Database Initialize
if 'sales' not in st.session_state:
    st.session_state.sales = pd.DataFrame(columns=['Date', 'Item', 'Rate', 'Qty', 'Total'])

# Main Dual Window Layout
col_receipt, col_dash = st.columns([1, 1])

# --- LEFT WINDOW: RECEIPT GENERATOR ---
with col_receipt:
    st.header("🧾 Create Receipt")
    logo = st.file_uploader("Upload Logo", type=['png', 'jpg'])
    shop_name = st.text_input("Shop Name")
    
    # File Uploader for Products (To fetch Item/Rate automatically)
    prod_file = st.file_uploader("Upload Product List (Excel/CSV)", type=['xlsx', 'csv'])
    
    product_name = st.text_input("Product Name")
    rate = st.number_input("Rate", min_value=0.0)
    qty = st.number_input("Quantity", min_value=1)
    
    if st.button("Generate Receipt"):
        total = rate * qty
        new_entry = {'Date': datetime.now(), 'Item': product_name, 'Rate': rate, 'Qty': qty, 'Total': total}
        st.session_state.sales = pd.concat([st.session_state.sales, pd.DataFrame([new_entry])], ignore_index=True)
        
        st.success(f"Receipt for {shop_name} Generated!")
        st.write(f"**Item:** {product_name} | **Total:** {total}")
        st.balloons()

# --- RIGHT WINDOW: LIVE DASHBOARD ---
with col_dash:
    st.header("📊 Check & Balance")
    st.write("Current Inventory & Sales Analytics")
    
    # Logic: Show current sales data
    if not st.session_state.sales.empty:
        st.dataframe(st.session_state.sales)
        st.metric("Total Revenue", f"{st.session_state.sales['Total'].sum():,.2f}")
    else:
        st.info("No sales data yet.")
