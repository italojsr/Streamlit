import streamlit as st
import controllers.usuariocontroller as usuariocontroller
import controllers.veiculocontroller as veiculocontroller
import models.Usuario as usuario
import models.Veiculo as veiculo
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write
import Pages.Usuario.Cadastrar as Cadastro
import Pages.Usuario.Consultar as Consulta
import Pages.Usuario.Anunciar as Anuncio
import Pages.Usuario.Consultar_Anuncio as Consulta_Anuncio




st.sidebar.title("Tela Inicial")
PageClient = st.sidebar.selectbox('Usuário',['Cadastrar','Consultar','Criar Anúncio','Consultar Anúncios'])


if PageClient == 'Cadastrar':
    st.experimental_set_query_params()
    Cadastro.Cadastrar()

elif PageClient == 'Consultar':
    Consulta.Consultar()

elif PageClient == 'Criar Anúncio':
    st.experimental_set_query_params()
    Anuncio.Anunciar()

elif PageClient == 'Consultar Anúncios':
    Consulta_Anuncio.Consultar_Anuncios()




