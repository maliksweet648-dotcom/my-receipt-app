import streamlit as st

# Page Configuration
st.set_page_config(page_title="MTT Global Receipt Generator", layout="centered")

# Styling: Dark Theme, Yellow Text, Black Inputs
st.markdown("""
    <style>
    .stApp {background-color: #0E1117; color: #FFFFFF;}
    h1, h2, h3 {color: #FFD700 !important;}
    div[data-baseweb="input"] {background-color: #1E1E1E !important; border: 1px solid #FFD700 !important;}
    div[data-baseweb="select"] {background-color: #1E1E1E !important; border: 1px solid #FFD700 !important;}
    label {color: #FFFFFF !important; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

st.title("MTT Global Receipt Generator")

# Logo Handling
col1, col2 = st.columns([1, 2])
with col1:
    uploaded_logo = st.file_uploader("Logo", type=['png', 'jpg', 'jpeg'])
with col2:
    shop_name = st.text_input("Enter Shop Name", placeholder="Type your shop name here...")

if uploaded_logo:
    st.image(uploaded_logo, width=120)
elif "logo.png":
    try:
        st.image("logo.png", width=120)
    except:
        st.write("Default logo not found.")

# Data Lists
currencies = ["USD ($)", "SAR (ر.س)", "PKR (Rs)", "EUR (€)", "GBP (£)", "AED (د.إ)", "INR (₹)", "JPY (¥)", "CAD ($)", "AUD ($)", "CHF (Fr)", "CNY (¥)", "TRY (₺)"]
languages = ["English", "Urdu", "Arabic", "Punjabi", "Hindi", "French", "Spanish", "Chinese", "German", "Turkish", "Russian", "Japanese"]

currency = st.selectbox("Select Currency", currencies)
language = st.selectbox("Select Language", languages)
item = st.text_input("Item Name")
price = st.number_input("Price", min_value=0.0)

if st.button("Generate Receipt"):
    st.success(f"Receipt for {shop_name if shop_name else 'Your Shop'}")
    st.write(f"**Item:** {item}")
    st.write(f"**Total:** {price} {currency}")
