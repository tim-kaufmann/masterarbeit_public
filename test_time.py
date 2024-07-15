import os
import time
import subprocess
import pandas as pd
from datetime import datetime

# Liste der zu ignorierenden Dateien
ignored_files = [
    'calculate_chi_test.py', 'calculate_pass_at_k.py', 'test_sleep.py',
    'test.py', 'measure_data.py', 'test_time.py', '__init__.py'
]

def measure_performance(file_path):
    start_time = time.time()
    process = subprocess.Popen(['python', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def determine_prompting_technique(file_name):
    if '0S' in file_name:
        return 'Zero Shot'
    elif 'CoT' in file_name:
        return 'Chain-of-Thoughts'
    elif 'RP' in file_name:
        return 'Role-Play'
    else:
        return 'Unknown'

def main(directory):
    data = []
    current_script = os.path.basename(__file__)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and file != current_script and file not in ignored_files and 'test' not in file.lower():
                file_path = os.path.join(root, file)
                print(f'Processing file: {file_path}')
                try:
                    prompt_technique = determine_prompting_technique(file)
                    task_name = os.path.basename(root)
                    execution_time = measure_performance(file_path)
                    data.append({
                        'Testlauf-ID': file,
                        'Programmieraufgabe': task_name,
                        'Prompting-Technik': prompt_technique,
                        'Ausführungszeit': execution_time
                    })
                except Exception as e:
                    print(f'Error processing file {file_path}: {e}')

    if data:
        df = pd.DataFrame(data)
        df.to_csv('code_metrics.csv', index=False)
        print('Data extraction complete. Results saved to code_metrics.csv')
    else:
        print('No data to save.')

if __name__ == '__main__':
    current_directory = os.getcwd()
    main(current_directory)