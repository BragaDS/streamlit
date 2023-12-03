import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'>My Projects</h1>", unsafe_allow_html=True)
st.write("##")

# Carregar a imagem
image = Image.open('abtest.png')
cluster_image = Image.open('clusteri.png')

# Criar colunas
col1, col2 = st.columns((1, 1))

# Coluna 1
with col1:
    st.image(image, use_column_width=True)
    st.subheader("AB TEST")
    st.markdown("""
        The A/B test is a methodology of experimentation in marketing that compares two versions of an element, such as an ad, to identify which yields better results. Utilizing statistical analyses, it aids in optimizing strategies based on the actual performance of the target audience.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/Teste_AB/blob/main/2testeabyt.ipynb)")

# Coluna 2
with col2:
    st.image(cluster_image, use_column_width=True)
    st.subheader("Cluster Analysis")
    st.markdown("""
        The cluster analysis involves grouping similar data points together to identify patterns and relationships within the dataset. In this project, K-means clustering was applied to categorize credit card customers based on their features. This method helps in understanding customer segments and tailoring strategies accordingly.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/Clusterizacao-de-Clientes/blob/main/1ccyt.ipynb)")

