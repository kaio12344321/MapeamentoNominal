import importlib
import streamlit as st
import pandas as pd
import funcoes

# Garante que o Streamlit sempre carregue a versão mais recente do funcoes.py
importlib.reload(funcoes)

st.title("Sistema de Cadastro de Clientes")
st.markdown("---")

if st.button("Limpar Tabela de Clientes"):
    funcoes.limpar_dados_tabela("clientes")  # Limpa a tabela de clientes antes de inserir novos dados



# O file_uploader fica fora do botão para não sumir ao recarregar a página
arquivo = st.file_uploader("Upload de Arquivo XLSX", type=["xlsx"])

if arquivo is not None:
    df = pd.read_excel(arquivo)

    st.write("Pré-visualização dos dados:")
    st.dataframe(df)

    # Verifica se as colunas esperadas existem na planilha
    colunas_esperadas = {'Nome', 'Telefone', 'Endereço'}
    if colunas_esperadas.issubset(df.columns):
        if st.button("Confirmar Cadastro"):
            # Trata células vazias (NaN -> None) e garante que telefone seja texto
            df = df.where(pd.notnull(df), None)

            nome = df['Nome'].astype(str).tolist()
            telefone = df['Telefone'].astype(str).tolist()
            endereco = df['Endereço'].astype(str).tolist()

            funcoes.insere_dados_xlsx(nome, telefone, endereco)
            st.success("Dados do arquivo XLSX inseridos com sucesso!")
    else:
        st.error(
            f"A planilha precisa conter as colunas: {', '.join(colunas_esperadas)}")

st.markdown("---")


if st.button("Listar Clientes"):
    dados = funcoes.listar_dados()
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereço"])
    st.header("Lista de Clientes Cadastrados")
    st.table(df)
