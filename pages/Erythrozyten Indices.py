# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# Here starts the actual app
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime
from utils.data_manager import DataManager

st.title("Erythrozyten Indices")

# Initialize session state to store past values
if 'data' not in st.session_state:
    st.session_state.data = []

# Input fields for user to enter values
hb = st.number_input("Hämoglobin (g/dL)", min_value=0.0, format="%.2f")
rbc = st.number_input("Erythrozytenzahl (10^12/L)", min_value=0.0, format="%.2f")
hct = st.number_input("Hämatokrit (%)", min_value=0.0, format="%.2f")

def classify_condition(mcv, mch, mchc):
    size_condition = "Normozytär"
    color_condition = "Normochrom"
    
    if mcv < 80:
        size_condition = "Mikrozytär"
    elif mcv > 100:
        size_condition = "Makrozytär"
    
    if mch < 27 or mchc < 33:
        color_condition = "Hypochrom"
    elif mch > 32 or mchc > 36:
        color_condition = "Hyperchrom"
    
    return f"{color_condition}, {size_condition}"

# Calculate Erythrozyten Indices

# Append new data to the session state DataFrame
if 'data_df' not in st.session_state:
    st.session_state['data_df'] = pd.DataFrame(columns=['Datum', 'MCV', 'MCH', 'MCHC', 'Resultat'])

if st.button("Daten speichern", key="save_button", help="Speichern Sie die aktuellen Daten", use_container_width=True):
    if hb > 0 and rbc > 0 and hct > 0:
        mcv = (hct / rbc) * 10
        mch = (hb / rbc) * 10
        mchc = (hb / hct) * 100
        result = classify_condition(mcv, mch, mchc)

        new_record = {
            'Datum': datetime.now(),
            'MCV': mcv,
            'MCH': mch,
            'MCHC': mchc,
            'Resultat': result
        }
        st.session_state['data_df'] = st.session_state['data_df'].append(new_record, ignore_index=True)
        DataManager().append_record(new_record)
        st.success("Daten erfolgreich gespeichert!")
    else:
        st.error("Bitte geben Sie gültige Werte für Hämoglobin, Erythrozytenzahl und Hämatokrit ein.")

# CSS to style the button in red and make it smaller
st.markdown("""
    <style>
    .stButton button {
        background-color: red;
        color: white;
        font-size: 10px;  /* Reduced font size */
        padding: 4px 8px;  /* Reduced padding */
    }
    </style>
    """, unsafe_allow_html=True)

# Create a scatter plot of past values
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    df['Datum'] = df['Datum'].dt.date  # Convert datetime to date to remove time
    fig, ax = plt.subplots()
    ax.scatter(df['Datum'], df['MCV'], c='blue', label='MCV')
    ax.scatter(df['Datum'], df['MCH'], c='green', label='MCH')
    ax.scatter(df['Datum'], df['MCHC'], c='red', label='MCHC')
    ax.set_xlabel('Datum')
    ax.set_ylabel('Werte')
    ax.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    st.pyplot(fig)

    # Option to download the plot
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    st.download_button(
        label="Download Plot",
        data=buf,
        file_name='scatter_plot.png',
        mime='image/png'
    )

def fig_to_image(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf
