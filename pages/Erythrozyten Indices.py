# ====== Start Login Block ======
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import os
import pandas as pd
import streamlit as st
from datetime import datetime

LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# Überprüfen, ob das Verzeichnis 'workspace' existiert, und erstelle es, falls nicht
if not os.path.exists('workspace'):
    os.makedirs('workspace')

# Überprüfen, ob die Datei 'data.csv' existiert, und erstelle sie, falls nicht
if not os.path.exists('workspace/data.csv'):
    st.warning("Die Datei 'data.csv' existiert nicht. Eine leere Datei wird erstellt.")
    df = pd.DataFrame(columns=['Datum', 'MCV', 'MCH', 'MCHC', 'Resultat'])
    df.to_csv('workspace/data.csv', index=False)

# Debugging: Überprüfe, ob die Datei existiert
if os.path.exists('workspace/data.csv'):
    st.write("Die Datei 'data.csv' existiert.")
else:
    st.error("Die Datei 'data.csv' existiert nicht. Bitte überprüfen Sie den Pfad.")

# Here starts the actual app
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
if st.button("Analysieren", key="analyze_button", help="Klicken Sie hier, um die Analyse durchzuführen", use_container_width=True):
    if hb > 0 and rbc > 0 and hct > 0:
        mcv = (hct / rbc) * 10
        mch = (hb / rbc) * 10
        mchc = (hb / hct) * 100

        st.write(f"Mittleres korpuskuläres Volumen (MCV): {mcv:.2f} fL")
        st.write(f"Mittleres korpuskuläres Hämoglobin (MCH): {mch:.2f} pg")
        st.write(f"Mittlere korpuskuläre Hämoglobinkonzentration (MCHC): {mchc:.2f} g/dL")

        result = classify_condition(mcv, mch, mchc)
        
        if result == "Normochrom, Normozytär":
            st.write(f"Resultat: {result}")
        else:
            st.markdown(f"<span style='color:red'>Resultat: {result}</span>", unsafe_allow_html=True)

        # Save the current values to session state
        new_record = {'Datum': datetime.now(), 'MCV': mcv, 'MCH': mch, 'MCHC': mchc, 'Resultat': result}
        st.session_state.data.append(new_record)

        # Debugging: Überprüfe den neuen Datensatz
        st.write("Neuer Datensatz:", new_record)

        # update the data.csv file
        DataManager().append_record(session_state_key='data', record_dict=new_record)

        st.success("Daten erfolgreich gespeichert.")
    else:
        st.error("Bitte geben Sie gültige Werte für Hämoglobin, Erythrozytenzahl und Hämatokrit ein.")