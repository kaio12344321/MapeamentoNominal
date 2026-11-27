import streamlit as st
import pandas as pd
import funcoes

st.title("Sistema de Cadastro de Clientes")

nome = st.text_input("Digite seu nome")
telefone = st.text_input("Digite seu telefone")
endereco = st.text_input("Digite seu endereço")

if st.button("Cadastrar"):
    funcoes.insere_dados(nome, telefone, endereco)
    st.success("Cadastro realizado com sucesso!")

if st.button("Listar Clientes"):
    dados = funcoes.listar_dados()
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereço"])
    st.header("Lista de Clientes Cadastrados")
    st.table(df)
    
