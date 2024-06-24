import pandas as pd

# CSV-Datei laden
df = pd.read_csv('code_metrics.csv')

# Funktion zur Berechnung von pass@5
def calculate_pass_5(df):
    results = []
    grouped = df.groupby(['Programmieraufgabe', 'Prompting-Technik'])
    for (task, technique), group in grouped:
        # Überprüfen, ob mindestens ein Testlauf alle Testfälle bestanden hat
        success = 1 if (group['Nicht bestandene Testfälle'] == 0).any() else 0
        results.append({'Programmieraufgabe': task, 'Prompting-Technik': technique, 'pass@5': success})
    return pd.DataFrame(results)

# Berechnung der pass@5 Werte
pass_5_results = calculate_pass_5(df)

# Ergebnisse in eine .xlsx-Datei speichern
output_file = 'pass_5_results.xlsx'
pass_5_results.to_excel(output_file, index=False)

# Bestätigung der Speicherung
print(f"Die pass@5-Ergebnisse wurden erfolgreich in '{output_file}' gespeichert.")