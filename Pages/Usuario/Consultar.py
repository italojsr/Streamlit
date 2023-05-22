import streamlit as st
import controllers.usuariocontroller as usuariocontroller
import models.Usuario as usuario
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from os import write
import Pages.Usuario.Cadastrar as Cadastro

def Consultar():
    st.title("Consultar")

    costumerList = []

    for item in usuariocontroller.SelecionarTodos():
        costumerList.append([item.cpf,item.nome,item.email,item.telefone])

    df = pd.DataFrame(costumerList,columns = ["CPF","Nome","Email","Telefone"])

    st.table(df)