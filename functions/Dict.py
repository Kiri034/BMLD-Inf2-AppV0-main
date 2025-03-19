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
            "fig_to_image(fig)"
        ],
        "features": [
            "Eingabe von Hämoglobin, Erythrozytenzahl und Hämatokrit",
            "Berechnung von MCV, MCH und MCHC",
            "Speichern der Ergebnisse in st.session_state",
            "Scatterplot der Ergebnisse",
            "Download-Option für den Scatterplot"
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
    "utils/data_manager.py": {
        "description": "Hilfsfunktionen für das Datenmanagement.",
        "functions": [
            "append_record(session_state_key, record_dict)",
            "save_data(session_state_key)"
        ],
        "features": [
            "Speichern und Verwalten von Daten in st.session_state",
            "Unterstützung für DataFrame und Listen"
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