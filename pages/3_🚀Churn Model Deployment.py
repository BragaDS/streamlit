import streamlit as st
import pandas as pd
import os

# Função para criar diretórios
def criar_diretorios(caminho_pasta, caminho_consolidado):
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
    if not os.path.exists(caminho_consolidado):
        os.makedirs(caminho_consolidado)

# Função para processar e consolidar dados
def processar_csv(caminho_pasta, caminho_consolidado, porcentagem_limite):
    # Lista para armazenar os DataFrames de cada arquivo
    dataframes = []

    # Iterar por todos os arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.csv'):  # Verificar se o arquivo é um CSV
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            # Carregar o arquivo CSV em um DataFrame e adicionar à lista
            df = pd.read_csv(caminho_arquivo, encoding='latin1', sep=';')
            dataframes.append(df)

    # Concatenar todos os DataFrames em um único
    dados_consolidados = pd.concat(dataframes, ignore_index=True)

    # Converter valores
    dados_consolidados['VALOR'] = dados_consolidados['VALOR'].str.replace('.', '', regex=False)
    dados_consolidados['VALOR'] = dados_consolidados['VALOR'].str.replace(',', '.', regex=False)
    dados_consolidados["VALOR"] = dados_consolidados["VALOR"].astype(float)

    dados_consolidados['COMPETENCIA'] = pd.to_datetime(dados_consolidados['COMPETENCIA'], dayfirst=True, errors='coerce')

    # Agrupar e calcular
    dados_agrupados = dados_consolidados.groupby(['IDFUNCIONAL', 'NOME_SERVIDOR', 'COMPETENCIA'], as_index=False).agg({'VALOR': 'sum'})

    dados_agrupados['VALOR'] = dados_agrupados['VALOR'].round(2)

    dados_agrupados['VALOR_MES_ANTERIOR'] = dados_agrupados.groupby(['IDFUNCIONAL', 'NOME_SERVIDOR'])['VALOR'].shift(1)

    dados_agrupados['PORCENTAGEM_DIFERENCA'] = ((dados_agrupados['VALOR'] - dados_agrupados['VALOR_MES_ANTERIOR']) / dados_agrupados['VALOR_MES_ANTERIOR']) * 100

    dados_agrupados['PORCENTAGEM_DIFERENCA'] = dados_agrupados['PORCENTAGEM_DIFERENCA'].round(2)

    dados_agrupados['PORCENTAGEM_DIFERENCA'] = dados_agrupados['PORCENTAGEM_DIFERENCA'].replace([float('inf'), -float('inf')], pd.NA)
    dados_agrupados = dados_agrupados.dropna(subset=['PORCENTAGEM_DIFERENCA'])

    # Filtrar resultados conforme a porcentagem
    resultados_filtrados = dados_agrupados[dados_agrupados['PORCENTAGEM_DIFERENCA'] > porcentagem_limite]

    return resultados_filtrados

# Função para salvar o resultado
def salvar_resultado(resultados_filtrados, caminho_saida):
    resultados_filtrados.to_csv(caminho_saida, index=False, sep=";", encoding='latin1')

# Título da aplicação
st.title('Consolidação e Análise de Dados')

# Entrada para o diretório dos arquivos CSV
diretorio_csv = st.text_input("Informe o diretório dos arquivos CSV:", r'C:\Users\wokra\Desktop\Anderson\Auxilio\Folha Auxílo Transporte')

# Entrada para o valor de porcentagem limite
porcentagem_limite = st.number_input("Informe o valor limite de porcentagem:", min_value=0, max_value=100, value=50)

# Botão para iniciar o processamento
if st.button("Processar Arquivos"):
    caminho_consolidado = os.path.join(diretorio_csv, 'consolidado')
    criar_diretorios(diretorio_csv, caminho_consolidado)

    # Processar os arquivos CSV e calcular os resultados
    resultados = processar_csv(diretorio_csv, caminho_consolidado, porcentagem_limite)

    if not resultados.empty:
        # Caminho de saída
        caminho_saida = os.path.join(caminho_consolidado, 'resultado.csv')

        # Salvar o resultado
        salvar_resultado(resultados, caminho_saida)

        # Exibir resultado na tela
        st.write(resultados)

        st.success(f"Resultados filtrados foram salvos em: {caminho_saida}")
    else:
        st.warning("Nenhum resultado encontrado com a porcentagem de diferença maior que o limite especificado.")
