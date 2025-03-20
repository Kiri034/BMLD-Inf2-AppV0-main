code_dict = {
    "Start.py": {
        "description": "Startseite der App mit Login-Block und Hauptlogik.",
        "functions": [
            "LoginManager().go_to_login('Start.py')",
            "classify_condition(mcv, mch, mchc)",
            "fig_to_image(fig)"
        ],
        "features": [
            "Login-Block",
            "Eingabe von Hämoglobin, Erythrozytenzahl und Hämatokrit",
            "Berechnung von MCV, MCH und MCHC",
            "Speichern der Ergebnisse in st.session_state",
            "Scatterplot der Ergebnisse",
            "Download-Option für den Scatterplot"
        ]
    },
    "Erythrozyten Indices.py": {
        "description": "Berechnung und Visualisierung der Erythrozyten-Indizes.",
        "functions": [
            "classify_condition(mcv, mch, mchc)",
            "DataManager().append_record(session_state_key, record_dict)"
        ],
        "features": [
            "Eingabe von Hämoglobin, Erythrozytenzahl und Hämatokrit",
            "Berechnung von MCV, MCH und MCHC",
            "Klassifikation der Ergebnisse (Normochrom, Mikrozytär, etc.)",
            "Speichern der Ergebnisse in st.session_state",
            "Speichern der Ergebnisse in einer CSV-Datei",
            "Erfolgsmeldung bei erfolgreicher Speicherung"
        ]
    },
    "Werte.py": {
        "description": "Anzeige des Verlaufs der gespeicherten Resultate in einer Tabelle.",
        "functions": [],
        "features": [
            "Tabelle mit Datum, MCV, MCH, MCHC und Resultat",
            "Formatierung der Datumsspalte",
            "Anzeige einer Nachricht, wenn keine Daten vorhanden sind"
        ]
    },
    "Grafik.py": {
        "description": "Erstellung und Anzeige eines Scatterplots basierend auf gespeicherten Daten.",
        "functions": [
            "fig_to_image(fig)"
        ],
        "features": [
            "Erstellung eines Scatterplots für MCV, MCH und MCHC",
            "Drehung der X-Achsen-Beschriftungen für bessere Lesbarkeit",
            "Download-Option für die Grafik als PNG-Datei",
            "Überprüfung auf fehlende Daten und Spalten"
        ]
    },
    "utils/data_manager.py": {
        "description": "Hilfsfunktionen für das Datenmanagement.",
        "functions": [
            "append_record(session_state_key, record_dict)",
            "save_data(session_state_key)"
        ],
        "features": [
            "Speichern und Verwalten von Daten in st.session_state",
            "Unterstützung für DataFrame und Listen",
            "Speichern von Daten in einer CSV-Datei"
        ]
    },
    "utils/login_manager.py": {
        "description": "Verwaltung des Login-Systems.",
        "functions": [
            "go_to_login(file_name)"
        ],
        "features": [
            "Weiterleitung zur Login-Seite",
            "Sitzungsverwaltung"
        ]
    }
}