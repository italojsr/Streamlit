import streamlit as st
import controllers.usuariocontroller as usuariocontroller
import models.Usuario as usuario
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write


def Cadastrar():

    st.title("Cadastro")
    with st.form(key = "include_cliente"):
        input_name = st.text_input(label="Insira seu nome de usuário")
        input_cpf = st.text_input(label = "Insira seu cpf")
        input_email = st.text_input(label = "Insira seu email")
        input_telefone = st.text_input(label = "Insira seu telefone")
        input_button_submit = st.form_submit_button("Criar conta")



    if input_button_submit:
        usuario.cpf = input_cpf
        usuario.nome = input_name
        usuario.telefone = input_telefone
        usuario.email = input_email

        usuariocontroller.Incluir(usuario)
        st.success("Cadastro efetuado com sucesso")