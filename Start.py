
import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="workspace")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )


# here starts our app

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

st.title("Anämie-App")

st.markdown("""
#### App-Beschreibung
Version 0.1 der Anämie-App für den Kurs Informatik 2. 
Diese App unterstützt Fachpersonen bei der Diagnose von Anämien, indem sie präzise Laborwerte analysiert und interpretiert.  
Die App ist anhand der folgenden Formel programmiert:
- **MCV** = Referenzbereich (80-100 fl)
- **MCH** = Hämoglobin/RbC (27-34 pg)
- **MCHC** = Hämoglobin/Hkt (32-36 g/dl)
""")


st.write("Link zur App: https://workspace-elena-kirisha.streamlit.app/")


st.markdown("""
#### Autoren

- **Elena Müller** (muellel3@students.zhaw.ch)
- **Kirisha Tharmaratnam** (tharmkir@students.zhaw.ch)
""")