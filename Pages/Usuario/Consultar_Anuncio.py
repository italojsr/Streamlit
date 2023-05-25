import streamlit as st
import controllers.veiculocontroller as veiculocontroller
import models.Veiculo as veiculo
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write
import Pages.Usuario.Anunciar as Anuncio

def Consultar_Anuncios():

    paramId = st.experimental_get_query_params()
    if(paramId == {}):
        st.title("Consulta de Anúncios")
        # Construindo as colunas da tabela com o streamlit
        colunas = st.columns(9)
        nomes_colunas = ['Nº','Tipo','Modelo','Marca','Ano','Quilometragem','Preço']
        for col, nome_coluna in zip(colunas,nomes_colunas):
            col.write(nome_coluna)

        # Pegando os itens do bd e colocando na tabela
        for item in veiculocontroller.SelecionarTodos(): 
            col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
            col1.write(item.id)
            col2.write(item.tipo)
            col3.write(item.modelo)
            col4.write(item.marca)
            col5.write(item.ano)
            col6.write(item.quilometragem)
            col7.write(item.preco)
            button_space_excluir = col8.empty()
            on_click_excluir = button_space_excluir.button('Excluir','btnExcluirAnuncio' + str(item.id))
            button_space_alterar = col9.empty()
            on_click_alterar = button_space_alterar.button('Alterar',  'btnAlterarAnuncio' + str(item.id))

            if on_click_excluir:
                veiculocontroller.Deletar(item.id)
                button_space_excluir.button('Excluído')
            if on_click_alterar:
                st.experimental_set_query_params(
                    id = [item.id] #Enviar o id do veículo que vai ser alterado para a home page
                )
                st.experimental_rerun()
    else:
        on_click_voltar = st.button('Voltar')
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        Anuncio.Anunciar()

    
