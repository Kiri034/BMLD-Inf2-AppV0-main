import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime

st.title('Grafik')

# Überprüfen, ob Daten vorhanden sind
if 'data' not in st.session_state or not st.session_state.data:
    st.write("Es sind keine Daten verfügbar, um die Grafik zu erstellen.")
    st.write("Debug: Keine Daten in st.session_state.data")
else:
    df = pd.DataFrame(st.session_state.data)

    # Debug: Zeige die Spalten und Daten an
    st.write("Debug: Spalten im DataFrame:", df.columns)
    st.write("Debug: Daten im DataFrame:", df)

    # Überprüfen, ob die erforderlichen Spalten vorhanden sind
    required_columns = ['Datum', 'MCV', 'MCH', 'MCHC']
    if not all(col in df.columns for col in required_columns):
        st.write("Die erforderlichen Spalten sind in den Daten nicht vorhanden.")
        st.write("Debug: Fehlende Spalten:", [col for col in required_columns if col not in df.columns])
    else:
        # Debug: Zeige die Werte der Spalte Datum
        st.write("Debug: Werte in der Spalte 'Datum':", df['Datum'])

        # Konvertiere die Datumsspalte in ein reines Datumsformat
        df['Datum'] = pd.to_datetime(df['Datum'], errors='coerce').dt.date
        if df['Datum'].isnull().any():
            st.write("Debug: Ungültige Datumswerte gefunden.")
            df = df.dropna(subset=['Datum'])

        # Erstelle den Scatterplot
        fig, ax = plt.subplots()
        ax.scatter(df['Datum'], df['MCV'], c='blue', label='MCV')
        ax.scatter(df['Datum'], df['MCH'], c='green', label='MCH')
        ax.scatter(df['Datum'], df['MCHC'], c='red', label='MCHC')
        ax.set_xlabel('Datum')
        ax.set_ylabel('Werte')
        ax.legend()
        plt.xticks(rotation=45)  # Drehe die X-Achsen-Beschriftungen
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