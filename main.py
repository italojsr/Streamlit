import streamlit as st

st.title("Cadastro")

with st.form(key = "include_cliente"):
    input_name = st.text_input(label="Insira seu nome de usuário")
    input_cpf = st.text_input(label = "Insira seu cpf")
    input_email = st.text_input(label = "Insira seu email")
    input_telefone = st.text_input(label = "Insira seu telefone")
    input_button_submit = st.form_submit_button("Criar conta")



