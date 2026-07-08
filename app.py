import streamlit as st
import pandas as pd

st.set_page_config(page_title="MTT Global Receipt Generator", layout="centered")

# Theme Control
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("<style>.stApp {background-color: #121212; color: white;}</style>", unsafe_allow_html=True)

st.title("MTT Global Receipt Generator")

# Logo Handling
uploaded_logo = st.file_uploader("Upload your Shop Logo (Optional)", type=['png', 'jpg', 'jpeg'])
if uploaded_logo:
    st.image(uploaded_logo, width=100)
else:
    try:
        st.image("logo.png", width=100) # Default logo
    except:
        st.write("No logo found.")

# Shop Details
shop_name = st.text_input("Enter Shop Name")
currency = st.selectbox("Currency", ["USD ($)", "SAR (ر.س)", "PKR (Rs)", "AED (د.إ)"])
item = st.text_input("Item Name")
price = st.number_input("Price", min_value=0.0)

if st.button("Generate Receipt"):
    receipt = f"""
    --- RECEIPT ---
    Shop: {shop_name if shop_name else "Generic Shop"}
    Item: {item}
    Price: {price} {currency}
    ----------------
    Powered by MTT Global
    """
    st.text(receipt)
