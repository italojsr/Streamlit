import streamlit as st
import controllers.usuariocontroller as usuariocontroller
import models.Usuario as usuario
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write


def Cadastrar():


    #Página de Alteração:
    cpfAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    usuarioRecuperado = None

    if(cpfAlteracao.get('cpf') != None):
        st.experimental_set_query_params()
        cpfAlteracao = cpfAlteracao.get('cpf')[0]
        usuarioRecuperado = usuariocontroller.SelecionarByCpf(cpfAlteracao)
        st.experimental_set_query_params(
            cpf = usuarioRecuperado.cpf
        )
        st.title('Alterar Cliente')

    else:
        st.title('Cadastro')
              
    with st.form(key = "include_cliente"):
        if(usuarioRecuperado == None):
            input_name = st.text_input(label="Insira seu nome de usuário")
            input_cpf = st.text_input(label = "Insira seu cpf")
            input_email = st.text_input(label = "Insira seu email")
            input_telefone = st.text_input(label = "Insira seu telefone")
            input_button_submit = st.form_submit_button('Cadastrar')
        else:
            input_name = st.text_input(label="Insira seu nome de usuário",value=usuarioRecuperado.nome)
            input_cpf = st.text_input(label = "Insira seu cpf",value=usuarioRecuperado.cpf)
            input_email = st.text_input(label = "Insira seu email",value =usuarioRecuperado.email)
            input_telefone = st.text_input(label = "Insira seu telefone",value = usuarioRecuperado.telefone)
            input_button_submit = st.form_submit_button('Alterar')


    if input_button_submit:

        usuario.cpf = input_cpf
        usuario.nome = input_name
        usuario.telefone = input_telefone
        usuario.email = input_email

        if usuarioRecuperado == None:
            usuariocontroller.Incluir(usuario)
            st.success("Cadastro efetuado com sucesso")
        else:
            st.experimental_set_query_params()
            usuariocontroller.Alterar(usuario)
            st.success("Usuário alterado com sucesso")
