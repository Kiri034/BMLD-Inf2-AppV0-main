import streamlit as st
import pandas as pd

st.title("Anämie-App")

st.info("""App-Beschreibung: Version 0.1 der Anämie-App für den Kurs Informatik 2. 
         Die App dient zur Diagnose von Anämie auf Basis von Laborwerten. 
         Die App ist anhand der Formel: MCV = Referenzbereich (80-100 fl), MCH = Hämoglobin/RbC (27-34 pg) und MCHC = Hämoglobin/Hkt (32-36 g/dl) programmiert.""")

st.write("Link zur App: https://workspace-elena-kirisha.streamlit.app/")

st.markdown("""#Authors:
            - Elena Müller (muellel3@students.zhaw.ch)
            - Kirisha Tharmaratnam (tharmkir@students.zhaw.ch)""")
