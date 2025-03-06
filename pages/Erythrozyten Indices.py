import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime

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
    
    if mch < 27 or mchc > 33:
        color_condition = "Hypochrom"
    elif mch < 32 or mchc > 36:
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
        st.session_state.data.append({'Datum': datetime.now(), 'MCV': mcv, 'MCH': mch, 'MCHC': mchc, 'Resultat': result})
    else:
        st.write("Bitte geben Sie gültige Werte für Hämoglobin, Erythrozytenzahl und Hämatokrit ein.")

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
    df['Wochentag'] = df['Datum'].dt.day_name()
    fig, ax = plt.subplots()
    ax.scatter(df['Wochentag'], df['MCV'], c='blue', label='MCV')
    ax.scatter(df['Wochentag'], df['MCH'], c='green', label='MCH')
    ax.scatter(df['Wochentag'], df['MCHC'], c='red', label='MCHC')
    ax.set_xlabel('Wochentag')
    ax.set_ylabel('Werte')
    ax.legend()
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
