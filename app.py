import streamlit as st

def main():
    st.header("This is header")
    name = st.text_input("Enter your name")
    st.button("Display my name")
main()