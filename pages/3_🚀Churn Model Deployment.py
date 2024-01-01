import streamlit as st
import numpy as np
import pandas as pd
import joblib
from PIL import Image

# Carregar modelos e outros dados necessários
scaler = joblib.load("model/churn_scaler_model.joblib")
pca = joblib.load("model/churn_pca_model.joblib")
kmeans = joblib.load("model/churn_kmeans_model.joblib")
xgb = joblib.load("model/churn_xgb_model.joblib")

# Títulos e mapeamentos
st.title("🚀 Churn Analysis and Customer Segmentation: Unveiling Patterns with Machine Learning 🚀")

gender_mapping = {'Feminino': 0, 'Masculino': 1}
country_mapping = {'França': 0, 'Alemanha': 1, 'Espanha': 2}

# Entrada de dados do usuário
credit_score = st.number_input("Pontuação de Crédito", min_value=0)
country = st.selectbox("Selecione o País", ["França", "Alemanha", "Espanha"])
gender = st.radio("Selecione seu gênero", ["Masculino", "Feminino"])
age = st.number_input("Idade", min_value=18)
tenure = st.number_input("Tempo de Relacionamento com o Banco", min_value=0, max_value=10)
balance = st.number_input("Saldo em conta", format="%.2f", step=0.01)
products_number = st.number_input("Numero de serviços com o Banco", min_value=1, max_value=4)
credit_card = st.radio("Possui cartão de crédito?", ["Sim", "Não"])
active_member = st.radio("É um membro ativo?", ["Sim", "Não"])
estimated_salary = st.number_input("Salario estimado", format="%.2f", step=0.01)

# Aplicar mapeamento
gender_numeric = gender_mapping[gender]
country_numeric = country_mapping[country]

# Criar DataFrame para XGBoost
data_xgb = {
    'credit_score': [credit_score],
    'country': [country_numeric],
    'gender': [gender_numeric],
    'age': [age],
    'tenure': [tenure],
    'balance': [balance],
    'products_number': [products_number],
    'credit_card': [1 if credit_card == 'Sim' else 0],
    'active_member': [1 if active_member == 'Sim' else 0],
    'estimated_salary': [estimated_salary]
}

# Criar DataFrame para KMeans
data_kmeans = {
    'credit_score': [credit_score],
    'country': [country_numeric],
    'gender': [gender_numeric],
    'age': [age],
    'tenure': [tenure],
    'balance': [balance],
    'products_number': [products_number],
    'credit_card': [1 if credit_card == 'Sim' else 0],
    'active_member': [1 if active_member == 'Sim' else 0],
    'estimated_salary': [estimated_salary]
}
df_xgb = pd.DataFrame(data_xgb)
df_kmeans = pd.DataFrame(data_kmeans)

# Aplicar escala aos dados para KMeans
df_scaled_kmeans = pd.DataFrame(scaler.transform(df_kmeans))

# Aplicar PCA para KMeans
df_pca_kmeans = pd.DataFrame(pca.transform(df_scaled_kmeans))

# Aplicar KMeans
group = kmeans.predict(df_pca_kmeans)

# Adicionar a coluna 'group' ao DataFrame df_xgb
df_xgb['group'] = group + 1

# Exibir o grupo atribuído pelo KMeans
st.write("Grupo atribuído pelo KMeans:", group[0]+1)

# Prever a probabilidade de churn com modelo XGBoost usando df_xgb
proba_churn = xgb.predict_proba(df_xgb)[:, 1]
# Adicionar a coluna 'proba_churn' ao DataFrame df_xgb
df_xgb['proba_churn'] = proba_churn

# Exibir a probabilidade de churn

# Definir o limiar para interpretar a probabilidade
limiar_churn = 0.5

# Exibir a probabilidade de churn
# Definir o limiar para interpretar a probabilidade
limiar_churn = 0.5

# Exibir a probabilidade de churn com estilização
formatted_proba_churn = f"{proba_churn[0]*100:.2f}%"
st.markdown(f"<p style='color: {'red' if proba_churn[0] > limiar_churn else 'green'};'>Probabilidade de Churn (XGBoost): {formatted_proba_churn}</p>", unsafe_allow_html=True)


# Verificar se a probabilidade de churn é maior que o limiar
if proba_churn[0] > limiar_churn:
    # Cliente propenso a sair
    st.markdown("**Este cliente está propenso a sair.**", unsafe_allow_html=True)
else:
    # Cliente não propenso a sair
    st.markdown("**Este cliente não está propenso a sair.**", unsafe_allow_html=True)





# Carregar imagens geradas no notebook
image_path_bar_chart = "img/bar_cluster.png"
image_path_scatter_plot = "img/Cluster_Churn.png"

# Exibir título do relatório
st.title("Entenda seu Grupo")

# Seção 4.1: Clustering Analysis
st.header("4.1 Análise de Agrupamento (Clustering)")

st.markdown("""
Em nossa exploração de churn de clientes, utilizamos Análise de Componentes Principais (PCA) e agrupamento KMeans para identificar grupos distintos dentro dos dados. O gráfico de dispersão subsequente ilustrou esses clusters, revelando padrões significativos. Após uma análise mais detalhada, ficou evidente que os grupos 3 e 2 exibiram uma menor suscetibilidade ao churn.

## Gráfico de Barras
Para visualizar a distribuição de clientes em diferentes clusters, empregamos um gráfico de barras. Essa visualização forneceu uma visão clara da porcentagem de clientes em cada cluster.

## Gráficos Adicionais
Após nossa análise inicial e conclusões, examinamos a distribuição de características-chave dentro de cada cluster identificado. Os histogramas confirmaram descobertas anteriores, como o Grupo 3 exibindo taxas de churn mais baixas. Além disso, o Grupo 3 tende a ter indivíduos mais jovens, e aqueles com saldos mais baixos são menos propensos a cancelar. Essas informações oferecem uma compreensão mais rica dos fatores que contribuem para a retenção de clientes em clusters específicos, confirmando as tendências identificadas por meio da análise de boxplot.

À medida que as empresas buscam implementar estratégias direcionadas, essas percepções refinadas podem orientar uma tomada de decisão mais eficaz e fomentar abordagens centradas no cliente.

## Conclusão
Nossa análise, apoiada por métricas, enfatiza percepções chave nas dinâmicas de churn de clientes. Os resultados do agrupamento destacaram grupos específicos, como os grupos 3 e 2, com porcentagens de churn mais baixas. Munidas dessa compreensão, as empresas podem formular estratégias direcionadas para reter clientes e aprimorar a satisfação geral.

As porcentagens de churn para cada grupo são as seguintes:

- Grupo 1: 22.90%
- Grupo 2: 17.58%
- Grupo 3: 13.43%
- Grupo 4: 26.31%

Essas métricas oferecem uma perspectiva detalhada das propensões variadas para churn em diferentes segmentos de clientes, confirmando as conclusões derivadas da análise de boxplot.
""")

# Inserir gráfico de barras
st.image(Image.open(image_path_bar_chart), caption='Gráfico de Barras - Distribuição de Churn por Grupo', use_column_width=True)

# Inserir gráfico de dispersão com clusters marcados por churn
st.image(Image.open(image_path_scatter_plot), caption='Gráfico de Dispersão com Clusters Marcados por Churn', use_column_width=True)