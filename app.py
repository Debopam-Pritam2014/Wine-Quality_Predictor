import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('ann_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
st.title('Wine Quality Predictor')
col1, col2, col3 = st.columns(3)

with col1:
    va=st.number_input('Volatile Acidity:',min_value=0.08, max_value=1.1,value=0.08,format="%.3f")
with col2:
    den=st.number_input('Density:',min_value=0.98, max_value=1.03, value=0.98,format="%.5f")
with col3:
    fso=st.number_input('Free SO2:', min_value=2.0, max_value=289.0, value=2.0)

col4, col5, col6 = st.columns(3)

with col4:
    fa=st.number_input('Fixed Acidity', min_value=3.8, max_value=14.2, value=3.8)
with col5:
    ph= st.number_input('pH', min_value=2.72, max_value=3.82, value=2.72)
with col6:
    al=st.number_input('Alcohol', min_value=8.0, max_value=14.2, value=8.0)

col7, col8, col9 = st.columns(3)

with col7:
   ca= st.number_input('Citric Acid',min_value=0.0, max_value=1.66, value=0.0,format="%.2f")
with col8:
    sul=st.number_input('Sulphates', min_value=0.22, max_value=1.08, value=0.22,format="%.2f")
with col9:
    tso=st.number_input('Total SO2', min_value=9.0, max_value=440.0, value=9.0)

col10, col11=st.columns(2)

with col10:
    rs=st.number_input('Residual Sugar', min_value=0.6, max_value=65.8, value=0.6)

with col11:
    cl=st.number_input('Chlorides', min_value=0.009, max_value=0.346, value=0.009,format="%.3f")

inp_arr=np.array([va,den,fso,fa,ph,al,ca,sul,tso,rs,cl])
if st.button('Click here to Predict'):
    inp_arr=inp_arr.reshape(1, -1)
    inp_arr=scaler.transform(inp_arr)

    pred= model.predict(inp_arr)
    y_pred=np.argmax(pred,axis=1)
    st.header('Predicted Quality: '+str(int(y_pred+3)))
