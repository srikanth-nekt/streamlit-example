import streamlit as st
import pandas as pd
# import pyxlsb

import streamlit_authenticator as stauth

# from streamlit_authenticator import Authenticator

import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# authenticator = Authenticate(
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'KPI Dashboard *{name}*')
    df = pd.read_csv("GG_17.csv")
    # df = pd.read_excel("GG_17.xlsb")

    # st.table(df)
    st.write(df)
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
