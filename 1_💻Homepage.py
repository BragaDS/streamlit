import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import os

# Se a variável de ambiente ENABLE_ANALYTICS estiver definida como 'true', incluir o código de rastreamento
if os.environ.get('ENABLE_ANALYTICS', '').lower() == 'true':
    st.markdown("""
    <!-- Código de rastreamento do Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-FMHPECVJSG"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-FMHPECVJSG');
    </script>
    """, unsafe_allow_html=True)

# Obtém o diretório do script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Muda o diretório de trabalho para o diretório do script
os.chdir(script_directory)

st.set_page_config(
    page_title="Ramon Braga"
)
#####################
# Header 
st.write('''
# Paulo Ramon Lima Braga
##### *Resume* 
''')

image = Image.open('img/dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am a graduate in Systems Analysis and Development, holding a postgraduate degree in Data Science and Big Data Analytics, complemented by various relevant courses and certifications. Currently serving as a State Military, my role revolves around data-centric activities and statistical analysis.

- My educational foundation and professional experience uniquely position me to navigate the intersection of technology and data-driven decision-making. With expertise in Systems Development and a focus on harnessing insights from extensive datasets, I contribute to meaningful projects that demand a blend of analytical rigor and technological proficiency.

- As a dedicated professional, I am committed to leveraging my skills to meet the challenges of dynamic environments, ensuring optimal solutions through a strategic and data-oriented approach.
''')


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**💿 Higher Education in Systems Analysis and Development**',
'')

txt('**📊 Postgraduate Degree in Data Science and Big Data Analytics**',
'')

#####################
st.markdown('''
## Work Experience
''')

txt('**State Military Officer| Ceará, Brazil**', 'October 2017 - Present')
st.markdown('''
- Executed data-centric activities and statistical analysis, leveraging a background in Systems Analysis and Development. 
- Successfully completed a postgraduate degree in Data Science and Big Data Analytics, enhancing analytical rigor and technological proficiency.
- Contributed to numerous projects, applying expertise in Systems Development to harness insights from extensive datasets.
- Navigated the intersection of technology and data-driven decision-making, ensuring optimal solutions through a strategic and data-oriented approach.
- Acquired various relevant certifications and participated in continuous education courses to stay abreast of technological advancements.
''')

### FUNÇÃO DOWNLOAD

#####################
st.markdown('''
## Courses with Certificates
''')
txt4('CoderHouse', 'Data Analytics', 'https://www.coderhouse.com.br/certificados/63135d3fc70e7f0019cf9b36?lang=pt')
txt4('CoderHouse', 'Data Science - TOP 10', 'https://www.coderhouse.com.br/certificados/6464171e11d21d0002e0aae4?lang=pt')
txt4('CoderHouse', 'Data Scientist Career - TOP 10', 'https://www.coderhouse.com.br/certificados/6464171e11d21d0002e0aae8?lang=pt')
txt4('Data Science Academy', 'Introduction to Data Science', 'https://mycourse.app/pt6ReAuVUY4Xk9kw7')
txt4('Data Science Academy', 'Big Data Fundamentals', 'https://mycourse.app/bSVG6W1CJfGSy79R7')
txt4('Data Science Academy', 'Python Fundamentals for Data Analysis', 'https://mycourse.app/a4et5epm2S1VKA9M8')
txt4('Data Science Academy', 'Data Visualization and Dashboard Design', 'https://mycourse.app/iiUpSaAzYpu9v48N8')
txt4('Data Science Academy', 'Business Analytics', 'https://mycourse.app/wGAJbhvrCM2BPWaK6')
txt4('Data Science Academy', 'Real-Time Big Data Analytics with Python and Spark', 'https://mycourse.app/fHEhAmQMAkXPLFW86')
txt4('Data Science Academy', 'Big Data Analytics with R and Microsoft Azure Machine Learning', 'https://mycourse.app/GB1rRCgFNPKx79Mc9')
txt4('Data Science Academy', 'Machine Learning', 'https://mycourse.app/uKMsRoExPBWBKxN7A')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`, `PowerBI`, `Excel`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Django`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/ramon-braga-894a1125b/')
txt2('Youtube', 'https://www.youtube.com/channel/UCgCegJMWW956kpdczpx2dCw')
