import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import streamlit as st



st.code('This is code ...')
st.text('This is Text ...')
st.title('This is a title')
st.markdown('# Heading in Markdown')
st.header('Header')
st.subheader('Sub Header')
st.latex(r'''
        a + ar + a r^4 + a r^8
         ''')
st.write('Can display many things')


df =pd.read_csv('Datasets/iris.csv')
st.dataframe(df)
# st.table(df)



from PIL import Image
img = Image.open('img.jpg')
st.image(img)
