import streamlit as st

st.title('Welcome to my first App')

name = st.text_input("Enter your name :")
fname= st.text_input("Enter your Father name")
addr = st.text_area("Enter your Address")
classdata= st.selectbox("Enter your class :",(1,2,3,4,5))

button = st.button("Done")
if button:
    st.markdown(f"""
    Name = {name}
    Father Name={fname}
    Address = {addr}
    Class = {classdata}
""")