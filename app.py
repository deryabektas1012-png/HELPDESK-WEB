import streamlit as st

st.title("AI Helpdesk Demo")

ticket = st.text_area("Enter your ticket:")

if st.button("Predict"):
    text = ticket.lower()

    if "wifi" in text:
        st.success("Category: Network")
    elif "password" in text:
        st.success("Category: Account")
    elif "printer" in text:
        st.success("Category: Device")
    else:
        st.success("Category: General")
