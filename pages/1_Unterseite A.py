import streamlit as st

st.title("Erythrozyten Indices")

# Input fields for user to enter values
hb = st.number_input("Hämoglobin (g/dL)", min_value=0.0, format="%.2f")
rbc = st.number_input("Erythrozytenzahl (10^12/L)", min_value=0.0, format="%.2f")
hct = st.number_input("Hämatokrit (%)", min_value=0.0, format="%.2f")

def classify_condition(mcv, mch, mchc):
    if mcv < 80:
        return "Mikrozytär"
    elif mcv > 100:
        return "Makrozytär"
    elif mch < 27:
        return "Hypochrom"
    elif mch > 34:
        return "Hyperchrom"
    elif mchc < 32:
        return "Hypochrom"
    elif mchc > 36:
        return "Hyperchrom"
    else:
        return "Normozytär"


# Calculate Erythrozyten Indices
if hb > 0 and rbc > 0 and hct > 0:
    mcv = (hct / rbc) * 10
    mch = (hb / rbc) * 10
    mchc = (hb / hct) * 100

    st.write(f"Mittleres korpuskuläres Volumen (MCV): {mcv:.2f} fL")
    st.write(f"Mittleres korpuskuläres Hämoglobin (MCH): {mch:.2f} pg")
    st.write(f"Mittlere korpuskuläre Hämoglobinkonzentration (MCHC): {mchc:.2f} g/dL")

    condition_type = classify_condition(mcv, mch, mchc)

    st.write(f"Typ: {condition_type}")
else:
    st.write("Bitte geben Sie gültige Werte für Hämoglobin, Erythrozytenzahl und Hämatokrit ein.")