import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

st.sidebar.write("Choose your agents.")

menu = ["Arbitrageurs only","Liquidity Providers only","Both"]
choice = st.sidebar.selectbox('agent type:', menu)

if choice =="Arbitrageurs only":
	st.sidebar.slider("How many Arbitrageurs?",0,10000)
elif choice =="Liquidity Providers only":
	st.sidebar.slider("How many Liquidity Providers?",0,10000)
elif choice =="Both":
	st.sidebar.slider("How many Arbitrageurs?",0,10000)
	st.sidebar.slider("How many Liquidity Providers?",0,10000)
	st.sidebar.slider("How many Mixed?",0,10000)
else:
	pass

volatility = st.sidebar.slider("Volatility:",0,100)

value = st.slider("label:",0,1000)

x = np.linspace(1,100,1000)
arr = np.piecewise(x, [x < 25,((x < 45)&(x>=25)),((x < 50)&(x>=45)), x >= 50], [lambda x: (50*random.randint(100-volatility,100))/(100*x), lambda x: (value+(400*random.randint(100-volatility,100)/100))/x, lambda x: 400/x, lambda x: 900/x])
fig, ax = plt.subplots()
ax.plot(arr)

st.pyplot(fig)
