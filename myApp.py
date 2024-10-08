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


st.button('Click Here')
st.checkbox('Check')
st.radio('Radio', ['male','female'])
st.selectbox('Select', ['Yes', 'No'])
st.multiselect('Multiple Selection', ['Machin learning Enginear', 'PHP', 'ASP','HTML 5'])
st.slider('Slide', min_value=1, max_value=10)
st.select_slider('Slide to Select', options=['Low','Medium', 'Large', 'Very Large'])
st.text_input('Enter Text')
st.number_input('Enter a Number')
st.text_area('Text Area')
st.date_input('Date')
st.file_uploader('Select File')
st.color_picker('Color Picker')

#Progress Bar
import time
progress_text = 'Operation in progress. Please wait.'
bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.2)
    bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
bar.empty()

st.button('Rerun')

st.balloons()

st.error('Error Mess')
st.warning('warning Mess')
st.info('info Mess')
st.success('success Mess')