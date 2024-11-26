import os
import pandas as pd
import streamlit as st

# Função para processar os arquivos CSV
def processar_csv(arquivos_csv, caminho_consolidado, porcentagem_limite):
    # Lista para armazenar os DataFrames de cada arquivo
    dataframes = []
    
    # Se não houver arquivos CSV, mostrar um erro
    if not arquivos_csv:
        st.error("Nenhum arquivo CSV foi carregado!")
        return None
    
    # Iterar por todos os arquivos CSV
    for arquivo in arquivos_csv:
        # Carregar o arquivo CSV em um DataFrame e adicionar à lista
        try:
            df = pd.read_csv(arquivo, encoding='latin1', sep=';')
            dataframes.append(df)
            st.write(f"Arquivo carregado com sucesso: {arquivo.name}")
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo {arquivo.name}: {e}")
    
    # Verificar se a lista de DataFrames não está vazia
    if not dataframes:
        st.error("Nenhum arquivo foi carregado corretamente.")
        return None
    
    # Concatenar todos os DataFrames em um único
    dados_consolidados = pd.concat(dataframes, ignore_index=True)

    # Criar o diretório para o arquivo consolidado, se não existir
    if not os.path.exists(caminho_consolidado):
        os.makedirs(caminho_consolidado)
    
    # Caminho para salvar o arquivo consolidado
    caminho_saida = os.path.join(caminho_consolidado, 'consolidado.csv')
    
    # Salvar o arquivo consolidado
    dados_consolidados.to_csv(caminho_saida, index=False, encoding='latin1', sep=';')
    
    # Retornar os dados consolidados
    return dados_consolidados

# Função para processar os dados e calcular as porcentagens
def calcular_porcentagem(dados):
    # Converter a coluna VALOR para float
    dados['VALOR'] = dados['VALOR'].str.replace('.', '', regex=False)
    dados['VALOR'] = dados['VALOR'].str.replace(',', '.', regex=False)
    dados["VALOR"] = dados["VALOR"].astype(float)
    
    # Converter a coluna COMPETENCIA para datetime
    dados['COMPETENCIA'] = pd.to_datetime(dados['COMPETENCIA'], dayfirst=True, errors='coerce')
    
    # Agrupar os dados e somar os valores por IDFUNCIONAL, NOME_SERVIDOR e COMPETENCIA
    dados_agrupados = dados.groupby(['IDFUNCIONAL', 'NOME_SERVIDOR', 'COMPETENCIA']).agg({'VALOR': 'sum'}).reset_index()
    
    # Ordenar os dados por IDFUNCIONAL, NOME_SERVIDOR e COMPETENCIA
    dados_agrupados = dados_agrupados.sort_values(by=['IDFUNCIONAL', 'NOME_SERVIDOR', 'COMPETENCIA'])
    
    # Calcular o valor do mês anterior
    dados_agrupados['VALOR_MES_ANTERIOR'] = dados_agrupados.groupby(['IDFUNCIONAL', 'NOME_SERVIDOR'])['VALOR'].shift(1)
    
    # Calcular a porcentagem de diferença entre o valor do mês atual e o anterior
    dados_agrupados['PORCENTAGEM_DIFERENCA'] = (
        (dados_agrupados['VALOR'] - dados_agrupados['VALOR_MES_ANTERIOR'])
        / dados_agrupados['VALOR_MES_ANTERIOR']
    ) * 100
    
    # Arredondar a porcentagem de diferença para 2 casas decimais
    dados_agrupados['PORCENTAGEM_DIFERENCA'] = dados_agrupados['PORCENTAGEM_DIFERENCA'].round(2)
    
    # Substituir valores infinitos e NaN
    dados_agrupados['PORCENTAGEM_DIFERENCA'] = dados_agrupados['PORCENTAGEM_DIFERENCA'].replace([float('inf'), -float('inf')], pd.NA)
    dados_agrupados = dados_agrupados.dropna(subset=['PORCENTAGEM_DIFERENCA'])
    
    # Filtrar os resultados pela porcentagem limite
    resultados_filtrados = dados_agrupados[dados_agrupados['PORCENTAGEM_DIFERENCA'] > porcentagem_limite]
    
    return resultados_filtrados

# Configuração do Streamlit
st.title("Processamento de Dados CSV - Auxílio Transporte")

# **Seleção de arquivos CSV via o file uploader**
arquivos_csv = st.file_uploader("Carregar arquivos CSV", type=["csv"], accept_multiple_files=True)

# **Entrada da porcentagem limite para o filtro**
porcentagem_limite = st.number_input("Informe a porcentagem limite para filtrar os dados:", min_value=0, max_value=100, value=50)

# Diretório para o arquivo consolidado
caminho_consolidado = r'C:\Users\wokra\Desktop\Anderson\Auxilio\Folha Auxílo Transporte\consolidado'

# Processar os arquivos e calcular os resultados
if arquivos_csv:
    # Chamar a função para processar os arquivos e criar o consolidado
    dados_consolidados = processar_csv(arquivos_csv, caminho_consolidado, porcentagem_limite)
    
    if dados_consolidados is not None:
        # Calcular a porcentagem e filtrar os resultados
        resultados_filtrados = calcular_porcentagem(dados_consolidados)
        
        if not resultados_filtrados.empty:
            # Exibir os resultados filtrados no Streamlit
            st.write(f"Resultados filtrados (porcentagem maior que {porcentagem_limite}%)")
            st.dataframe(resultados_filtrados)
            
            # Botão para baixar o arquivo CSV com os resultados
            resultado_final = os.path.join(caminho_consolidado, 'resultado.csv')
            resultados_filtrados.to_csv(resultado_final, index=False, sep=";", encoding='latin1')
            st.download_button(
                label="Baixar arquivo filtrado",
                data=open(resultado_final, "rb").read(),
                file_name="resultado.csv",
                mime="text/csv"
            )
        else:
            st.write("Nenhum dado atendendo ao filtro de porcentagem foi encontrado.")
