# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======


# Here starts the actual app

import streamlit as st
import pandas as pd

st.title("Werte")

st.write("Hier können Sie den Verlauf ihrer Resultate sehen.")

# Überprüfe, ob Daten vorhanden sind
if 'data' in st.session_state and st.session_state.data:
    # Erstelle einen DataFrame aus den gespeicherten Daten
    df = pd.DataFrame(st.session_state.data)
    
    # Formatierung der Datumsspalte (Datum und Uhrzeit anzeigen)
    df['Datum'] = pd.to_datetime(df['Datum']).dt.strftime('%d.%m.%Y %H:%M:%S')
    
    # Zeige die Tabelle an
    st.dataframe(df, use_container_width=True)
else:
    st.write("Es sind noch keine Resultate verfügbar.")