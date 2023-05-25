import streamlit as st
import controllers.veiculocontroller as veiculocontroller
import models.Veiculo as veiculo
import streamlit.components.v1 as components
from os import write

def Anunciar():


    idAlteracao = st.experimental_get_query_params()
    veiculoRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        veiculoRecuperado = veiculocontroller.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[veiculoRecuperado.id]
        )
        st.title("Anunciar Veículo")
    else:
        st.title("Cadastrar Veículo")

    st.markdown("""
    <style>
    button.step-up {display: none;}
    button.step-down {display: none;}
    div[data-baseweb] {border-radius: 4px;}
    </style>""",
    unsafe_allow_html=True)
    with st.form(key = "include_veiculo"):
        listVehicles = ["Carro", "Motocicleta"]
        if(veiculoRecuperado == None):
            input_tipo = st.selectbox(label = "Insira o tipo de veículo", options = ["Carro", "Motocicleta"])
            input_modelo = st.text_input(label = "Insira o modelo")
            input_marca = st.text_input(label = "Insira a fabricante")
            input_ano = st.number_input(label = "Insira o ano de fabricação", format = "%d", max_value=2024)
            input_quilometragem = st.number_input(label = "Insira a quilometragem (em milhares de km)", format = "%d", step=1)
            input_preco = st.number_input(label="Insira o preço do veículo", format="%.2f")
            input_button_submit = st.form_submit_button("Criar anúncio")
        else:
            input_tipo = st.selectbox(label = "Insira o tipo de veículo", options = listVehicles,index = listVehicles.index(veiculoRecuperado.tipo))
            input_modelo = st.text_input(label = "Insira o modelo",value = veiculoRecuperado.modelo)
            input_marca = st.text_input(label = "Insira a fabricante",value = veiculoRecuperado.marca)
            input_ano = st.number_input(label = "Insira o ano de fabricação",value =veiculoRecuperado.ano , format = "%d", max_value=2024)
            input_quilometragem = st.number_input(label = "Insira a quilometragem (em milhares de km)",value = veiculoRecuperado.quilometragem, format = "%d", step=1)
            input_preco = st.number_input(label="Insira o preço do veículo",value = veiculoRecuperado.preco, format="%.2f")
            input_button_submit = st.form_submit_button("Alterar anúncio")

    if input_button_submit:
        veiculo.tipo = input_tipo
        veiculo.modelo = input_modelo
        veiculo.marca = input_marca
        veiculo.ano = input_ano
        veiculo.quilometragem = input_quilometragem
        veiculo.preco = input_preco
        if(veiculoRecuperado == None):
            veiculocontroller.Incluir(veiculo)
            st.success("Veículo cadastrado com sucesso")
        else:
            veiculo.id = veiculoRecuperado.id
            st.experimental_set_query_params()
            veiculocontroller.Alterar(veiculo)
            st.success("Veículo alterado com sucesso")
            


