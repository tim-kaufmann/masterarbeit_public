import pandas as pd
import scipy.stats as stats

# CSV-Datei laden mit expliziter Angabe des Trennzeichens und Fehlerbehandlung
df = pd.read_csv('code_metrics2.csv', encoding='utf-8', sep=';')

# Erfolgsrate pro Prompting-Technik berechnen
success_rate = df.groupby('Prompting-Technik').apply(lambda x: (x['Nicht bestandene Testfälle'] == 0).mean()).reset_index()
success_rate.columns = ['Prompting-Technik', 'Erfolgsrate']

# Chi-Quadrat-Test vorbereiten
contingency_table = pd.crosstab(df['Prompting-Technik'], df['Nicht bestandene Testfälle'] == 0)

# Chi-Quadrat-Test durchführen
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

# Ergebnisse anzeigen
print("Erfolgsrate pro Prompting-Technik:")
print(success_rate)

print("\nChi-Quadrat-Test Ergebnisse:")
print(f"Chi2: {chi2}, p-Wert: {p}, Freiheitsgrade: {dof}")
print("Erwartete Häufigkeiten:")
print(expected)

# Erfolgsraten in einer .xlsx-Datei speichern
output_file = 'success_rate.xlsx'
success_rate.to_excel(output_file, index=False)

# Bestätigung der Speicherung
print(f"Die Erfolgsraten wurden erfolgreich in '{output_file}' gespeichert.")
