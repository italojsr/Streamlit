import streamlit as st
import controllers.usuariocontroller as usuariocontroller
import models.Usuario as usuario
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write
import Pages.Usuario.Cadastrar as Cadastro

def Consultar():
    # Construindo as colunas da tabela com o streamlit
    colunas = st.columns(6)
    nomes_colunas = ['CPF','Nome','Email','Telefone','Excluir','Alterar']
    for col, nome_coluna in zip(colunas,nomes_colunas):
        col.write(nome_coluna)

    # Pegando os itens do bd e colocando na tabela
    for item in usuariocontroller.SelecionarTodos(): 
        col1,col2,col3,col4,col5,col6 = st.columns(6)
        col1.write(item.cpf)
        col2.write(item.nome)
        col3.write(item.email)
        col4.write(item.telefone)
        button_space_excluir = col5.empty()
        on_click_excluir = button_space_excluir.button('Excluir','btnExcluir' + str(item.cpf))
        button_space_alterar = col6.empty()
        on_click_alterar = button_space_alterar.button('Alterar',  'btnAlterar' + str(item.cpf))

        if on_click_excluir:
            usuariocontroller.Deletar(item.cpf)
            button_space_excluir.button('Excluído')
        if on_click_alterar:
            st.experimental_set_query_params(
                cpf = [item.cpf]
            )

    
    # st.title("Consultar")

    # costumerList = []

    # for item in usuariocontroller.SelecionarTodos():
    #     costumerList.append([item.cpf,item.nome,item.email,item.telefone])

    # df = pd.DataFrame(costumerList,columns = ["CPF","Nome","Email","Telefone"])

    # st.table(df)
    