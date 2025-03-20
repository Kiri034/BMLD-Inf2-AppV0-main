# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# Überprüfen, ob die Session-State-Variable 'data' initialisiert ist
import streamlit as st
import pandas as pd

if 'data' not in st.session_state:
    st.session_state['data'] = []

st.title("Werte")

st.write("Hier können Sie den Verlauf ihrer Resultate sehen.")

# Debugging: Zeige den Inhalt von st.session_state['data']
st.write("Debug: Inhalt von st.session_state['data']:", st.session_state['data'])

# Überprüfe, ob Daten vorhanden sind
if 'data' in st.session_state and st.session_state['data']:
    df = pd.DataFrame(st.session_state['data'])
    df['Datum'] = pd.to_datetime(df['Datum']).dt.strftime('%d.%m.%Y %H:%M:%S')
    st.dataframe(df, use_container_width=True)
else:
    st.write("Es sind noch keine Resultate verfügbar.")