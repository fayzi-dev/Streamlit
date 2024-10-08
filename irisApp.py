import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write('**Iris App Create By** fayzi.dev')

st.sidebar.header('User Selection Parameters')

def user_input():
    sepal_length = st.sidebar.slider('Sepal Length', min_value=1, max_value=10)
    sepal_width = st.sidebar.slider('Sepal width', min_value=1, max_value=5)
    petal_length = st.sidebar.slider('petal Length', min_value=1, max_value=10)
    petal_width = st.sidebar.slider('petal width', min_value=1, max_value=5)
    data = {
        'sepal_length':sepal_length,
        'sepal_width': sepal_width,
        'petal_length':petal_length,
        'petal_width':petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features
df_input_user = user_input()

st.subheader('User Input  Parameters')
st.write(df_input_user)


iris = pd.read_csv('/home/m-fayzi/Desktop/Streamlit/Datasets/iris.csv')
# st.dataframe(iris)
X = iris.iloc[:, 0:-1].values
y = iris.iloc[:, -1].values
# st.dataframe(X)
# st.dataframe(y)

classefier = RandomForestClassifier()
classefier.fit(X, y)

y_pred = classefier.predict(df_input_user)
pred_proba = classefier.predict_proba(df_input_user)

st.subheader('Class Label and Their Corresponding Index Number')
target_name = ['Setosa','Versicolor','Virginica']
target = pd.DataFrame(target_name)
st.write(target)


st.subheader('Prediction')
# st.write(iris.columns[y_pred])
st.write(y_pred)

st.subheader('Prediction Probability')
st.write(pred_proba)



