import streamlit as st
import controllers.usuariocontroller as usuariocontroller
import models.Usuario as usuario
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write
import Pages.Usuario.Cadastrar as Cadastro
import Pages.Usuario.Consultar as Consulta




st.sidebar.title("Tela Inicial")
PageClient = st.sidebar.selectbox('Usuário',['Cadastrar','Alterar','Excluir','Consultar'])


if PageClient == 'Cadastrar':
    Cadastro.Cadastrar()

elif PageClient == 'Consultar':
    Consulta.Consultar()





