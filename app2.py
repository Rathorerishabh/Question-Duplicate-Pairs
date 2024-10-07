import streamlit as st
import helper
import pickle

# Load your model
model = pickle.load(open('model.pkl','rb'))

# Custom CSS to make the app more visually appealing
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Helvetica';
        text-align: center;
        font-size: 48px;
    }
    .stTextInput {
        font-family: 'Arial';
    }
    .result-header {
        font-size: 30px;
        color: #fff;
        text-align: center;
        background-color: #4CAF50;
        padding: 20px;
        border-radius: 10px;
    }
    .not-duplicate {
        font-size: 30px;
        color: #fff;
        text-align: center;
        background-color: #e74c3c;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.title('🔍 Duplicate Question Detector')

# Description
st.markdown("""
    Welcome to the **Duplicate Question Detector**. This tool helps you determine whether two questions are similar enough to be considered duplicates.  
    Please enter the two questions below and click **Find** to check if they are duplicates.
""")

# Input fields
st.subheader('Enter your Questions:')
col1, col2 = st.columns(2)

with col1:
    q1 = st.text_input('Question 1')
with col2:
    q2 = st.text_input('Question 2')

# Button to perform prediction
if st.button('Find 🔍'):
    if q1 and q2:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]
        
        if result:
            st.markdown('<div class="result-header">🎉 These questions are <b>Duplicate!</b></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="not-duplicate">❌ These questions are <b>Not Duplicate</b></div>', unsafe_allow_html=True)
    else:
        st.error('Please enter both questions to proceed.')

# Footer
st.markdown("""
    ---
    **Note:** This tool is designed to help detect duplicate questions and improve user experience on Q&A platforms like Quora.  
    The prediction is based on a trained machine learning model.
""")
