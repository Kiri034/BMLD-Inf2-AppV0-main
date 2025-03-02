import streamlit as st
from calculate_indices import calculate_mcv, calculate_mch, calculate_mchc

st.title("Erythrozyten Indices")

# Input fields for user to enter values
hb = st.number_input("Hämoglobin (g/dL)", min_value=0.0, format="%.2f")
rbc = st.number_input("Erythrozytenzahl (10^12/L)", min_value=0.0, format="%.2f")
hct = st.number_input("Hämatokrit (%)", min_value=0.0, format="%.2f")

# Calculate Erythrozyten Indices
if hb > 0 and rbc > 0 and hct > 0:
    mcv = (hct / rbc) * 10
    mch = (hb / rbc) * 10
    mchc = (hb / hct) * 100

    st.write(f"Mittleres korpuskuläres Volumen (MCV): {mcv:.2f} fL")
    st.write(f"Mittleres korpuskuläres Hämoglobin (MCH): {mch:.2f} pg")
    st.write(f"Mittlere korpuskuläre Hämoglobinkonzentration (MCHC): {mchc:.2f} g/dL")
else:
    st.write("Bitte geben Sie gültige Werte für Hämoglobin, Erythrozytenzahl und Hämatokrit ein.")