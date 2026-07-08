import streamlit as st

st.title("Global Receipt Generator | 全球收据生成器")

# Inputs
shop_name = st.text_input("Shop Name / 店铺名称")
customer_name = st.text_input("Customer Name / 客户姓名")
item = st.text_input("Item / 商品名称")
price = st.number_input("Price / 价格")

# Currency Selector
currency = st.selectbox("Select Currency / 选择货币", 
                        ["SAR (Saudi Riyal)", "PKR (Pakistani Rupee)", 
                         "USD ($)", "EUR (€)", "GBP (£)", "CNY (Chinese Yuan)"])

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
