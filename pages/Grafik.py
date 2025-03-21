# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# Here starts the graph page
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime

# Initialisiere st.session_state['data'], falls es nicht existiert
if 'data' not in st.session_state:
    st.session_state['data'] = []

st.title("Graph der Erythrozyten-Indizes")

# Debugging: Zeige den Inhalt von st.session_state['data']
st.write("Debug: Inhalt von st.session_state['data']:", st.session_state['data'])

if not st.session_state['data']:
    st.write("Es sind keine Daten verfügbar, um die Grafik zu erstellen.")
else:
    # Erstelle einen DataFrame aus den gespeicherten Daten
    df = pd.DataFrame(st.session_state['data'])

    # Überprüfen, ob die erforderlichen Spalten vorhanden sind
    required_columns = ['Datum', 'MCV', 'MCH', 'MCHC']
    if not all(col in df.columns for col in required_columns):
        st.write("Die erforderlichen Spalten sind in den Daten nicht vorhanden.")
    else:
        # Konvertiere die Datumsspalte in ein reines Datumsformat
        df['Datum'] = pd.to_datetime(df['Datum'], errors='coerce').dt.date
        df = df.dropna(subset=['Datum'])

        # Erstelle den Scatterplot
        fig, ax = plt.subplots()
        ax.scatter(df['Datum'], df['MCV'], c='blue', label='MCV')
        ax.scatter(df['Datum'], df['MCH'], c='green', label='MCH')
        ax.scatter(df['Datum'], df['MCHC'], c='red', label='MCHC')
        ax.set_xlabel('Datum')
        ax.set_ylabel('Werte')
        ax.legend()
        plt.xticks(rotation=45)  
        st.pyplot(fig)

        # Option zum Herunterladen der Grafik
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        file_name = f"scatter_plot_{datetime.now().strftime('%Y%m%d')}.png"
        st.download_button(
            label="Download Plot",
            data=buf,
            file_name=file_name,
            mime='image/png'
        )