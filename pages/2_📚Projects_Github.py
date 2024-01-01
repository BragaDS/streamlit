import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center;'>My Projects</h1>", unsafe_allow_html=True)
st.write("##")

# Carregar a imagem
image = Image.open('img/abtest.png')
cluster_image = Image.open('img/clusteri.png')
fetal_health_image = Image.open('img/class.png')
cohort = Image.open('img/cohort.png')
churn = Image.open('img/churn.png')
churn_cluster = Image.open('img/churn_cluster.png')

# Criar colunas
col1, col2 = st.columns((1, 1))

# Coluna 1
with col1:
    st.image(image, use_column_width=True)
    st.subheader("AB TEST")
    st.markdown("""
        The A/B test is a methodology of experimentation in marketing that compares two versions of an element, such as an ad, to identify which yields better results. Utilizing statistical analyses, it aids in optimizing strategies based on the actual performance of the target audience.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/ab_test)")

    st.image(fetal_health_image, use_column_width=True)
    st.subheader("Fetal Health Classification")
    st.markdown("""
        The Fetal Health Classification project utilizes machine learning to predict the health status of fetuses based on features extracted from Cardiotocogram (CTG) exams. The classification model employs algorithms optimized through hyperparameter tuning and evaluates its performance using metrics such as accuracy, precision, recall, and F1-score. The objective is to contribute to efforts in reducing child and maternal mortality by providing accurate predictions for fetal health.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/fetal_classification)")

    st.image(churn, use_column_width=True)
    st.subheader("Churn Prediction Project")
    st.markdown("""
        The Churn Prediction project aims to forecast customer churn using advanced machine learning techniques. By leveraging algorithms such as XGBoost and Random Forest, the model analyzes various features to predict the likelihood of customers leaving. The project explores the impact of outlier removal, pre-processing, and the effectiveness of different algorithms. The results are detailed in a comprehensive conclusion, providing insights into model performance and recommendations for further enhancements.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/churn)")


# Coluna 2
with col2:
    st.image(cluster_image, use_column_width=True)
    st.subheader("Cluster Analysis")
    st.markdown("""
        The cluster analysis involves grouping similar data points together to identify patterns and relationships within the dataset. In this project, K-means clustering was applied to categorize credit card customers based on their features. This method helps in understanding customer segments and tailoring strategies accordingly.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/Customer-Clustering)")

    st.image(cohort, use_column_width=True)
    st.subheader("Cohort Analysis")
    st.markdown("""
        The cohort analysis comprises grouping related data points to uncover insights and connections within the dataset. For this analysis, a cohort-based approach was employed, utilizing methods like retention rates and cohort indices. These techniques allow us to discern patterns in customer behavior over time, providing valuable insights for strategic decision-making.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/cohort)")

    st.image(churn_cluster, use_column_width=True)
    st.subheader("Churn Prediction Project")
    st.markdown("""
        The Churn Prediction project with Cluster Analysis utilizes machine learning techniques to forecast customer churn. The project incorporates algorithms like XGBoost, explores the impact of outlier removal, and leverages cluster analysis for customer segmentation. The results provide valuable insights into churn patterns and recommendations for targeted retention strategies.
    """)
    st.markdown("[Visit Github](https://github.com/BragaDS/churn_clustering/blob/master/churn_clustering.ipynb)")
