import streamlit as st
import pandas as pd
import numpy as np

st.write("""
#  Hello world
""")
a= st.number_input("NUMBER_1", min_value=0.0,max_value=2000000000.0)
b= st.number_input("NUMBER_2", min_value=0.0,max_value=2000000000.0)
c= st.number_input("NUMBER_3", min_value=0.0,max_value=2000000000.0)
st.write(a)
