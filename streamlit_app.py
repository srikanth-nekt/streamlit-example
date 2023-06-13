import os
import streamlit as st
import pandas as pd
# import pyxlsb

import streamlit_authenticator as stauth

# from streamlit_authenticator import Authenticator

import yaml
from yaml.loader import SafeLoader

import streamlit as st

st.set_page_config(
   page_title="VI Dashboards",
   page_icon="VI",
   layout="wide",
   initial_sidebar_state="expanded",
)

vi_s_cols = [
'Store Name',
'GG Tgt', 'GG FTD', 'GG  MTD', '% Ach GG',
'Churn MTD', '% SR',
'MNP Tgt', 'FTD MNP', 'MTD MNP', '% Ach MNP',
'CONS Tgt', 'FTD Cons', 'MTD Cons', '% Ach Cons',
'IOIP Tgt', 'FTD IOIP', 'MTD IOIP', '% Ach IOIP',
'COCP Tgt', 'FTD COCP', 'MTD COCP', '% Ach COCP',
'Fam Tgt', 'FTD Fam', 'MTD Fam', '% Ach Fam',
'SME+SoHo Tgt', 'FTD SME', 'MTD SME',
'CONS Fresh Tgt', 'FTD Cons Fresh', 'MTD Cons Fresh', '% Ach Cons Fresh',
'CONS MNP Tgt', 'FTD MNP', 'MTD MNP', '% Ach Cons MNP',
'CONS P2P Tgt', 'FTD Cons P2P', 'MTD Cons P2P', '% Ach Cons P2P'
]


path = os.path.dirname(__file__)
my_file = os.path.join(path, 'config.yaml')
with open(my_file) as file:
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

    st.write(f'VI S Dashboard *{name}*')
    # df = pd.read_csv("GG_17.csv")
    my_csv = os.path.join(path, 'Vi_S.csv')
    df = pd.read_csv(my_csv)
    df.columns = df.columns.str.replace('\n', ' ')
    # df = pd.read_excel("GG_17.xlsb")
    if is_arl:
        df = df.loc[df['ARL'] == name]
        st.write(df[[col for col in df.columns if col in vi_s_cols]])
    elif is_sup:
        df = df.loc[df['FL  And SM Name'] == name]
        st.write(df[[col for col in df.columns if col in vi_s_cols]])
        # print(df.columns)
    else:
        st.write(df[[col for col in df.columns if col in vi_s_cols]])

    authenticator.logout('Logout', 'main')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

