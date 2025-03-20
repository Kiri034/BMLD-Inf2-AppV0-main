import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime

st.title('Grafik')

# Überprüfen, ob Daten vorhanden sind
if 'data' not in st.session_state or not st.session_state.data:
    st.write("Es sind keine Daten verfügbar, um die Grafik zu erstellen.")
else:
    df = pd.DataFrame(st.session_state.data)

    # Überprüfen, ob die erforderlichen Spalten vorhanden sind
    required_columns = ['Datum', 'MCV', 'MCH', 'MCHC']
    if not all(col in df.columns for col in required_columns):
        st.write("Die erforderlichen Spalten sind in den Daten nicht vorhanden.")
    else:
        df['Datum'] = pd.to_datetime(df['Datum']).dt.date  # Konvertiere Datum in reines Datumsformat
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

# Hilfsfunktion zum Konvertieren einer Figur in ein Bild
def fig_to_image(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf
