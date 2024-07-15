import time
import subprocess

def measure_performance(file_path):
    start_time = time.time()
    print(f"Startzeit: {start_time:.6f}")  # Debugging-Ausgabe
    process = subprocess.Popen(['python', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = time.time()
    print(f"Endzeit: {end_time:.6f}")  # Debugging-Ausgabe
    execution_time = end_time - start_time
    print(f"Ausführungszeit: {execution_time:.6f} Sekunden")  # Debugging-Ausgabe
    return execution_time

# Test-Skript zur Messung
test_script_path = 'test_sleep.py'

# Erstellen eines Test-Skripts, das 2 Sekunden wartet
with open(test_script_path, 'w') as f:
    f.write("import time\n")
    f.write("time.sleep(2)\n")

# Ausführung des Test-Skripts
execution_time = measure_performance(test_script_path)
print(f"Gemessene Ausführungszeit: {execution_time:.6f} Sekunden")

# Überprüfung der Einheit
# Annahme: Zeit in Sekunden
print(f"Ausführungszeit in Sekunden: {execution_time:.6f} s")
# Annahme: Zeit in Millisekunden
print(f"Ausführungszeit in Millisekunden: {execution_time * 1e3:.6f} ms")
# Annahme: Zeit in Mikrosekunden
print(f"Ausführungszeit in Mikrosekunden: {execution_time * 1e6:.6f} µs")
# Annahme: Zeit in Nanosekunden
print(f"Ausführungszeit in Nanosekunden: {execution_time * 1e9:.6f} ns")
