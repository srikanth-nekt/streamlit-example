import streamlit as st
import pandas as pd
# import pyxlsb

import streamlit_authenticator as stauth

# from streamlit_authenticator import Authenticator

import yaml
from yaml.loader import SafeLoader

st.set_page_config(
   page_title="VI Dashboards",
   page_icon="VI",
   layout="wide",
   initial_sidebar_state="expanded",
)

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

is_arl = 'arl' in username
is_sup = 'super' in username

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'KPI Dashboard *{name}*')
    df = pd.read_csv("GG_17.csv")
    # df = pd.read_excel("GG_17.xlsb")
    if is_arl:
        st.write(df.loc[df['ARL'] == name])
    elif is_sup:
        st.write(df.loc[df['FL  And SM Name'] == name])
        # print(df.columns)
    else:
        st.write(df)
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')



