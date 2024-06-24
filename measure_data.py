import os
import re
import time
import subprocess
from datetime import datetime
import pandas as pd
import ast

def extract_code_metrics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    # Code length
    code_length = len(code.splitlines())
    
    # Comment count
    comment_count = sum(1 for line in code.splitlines() if line.strip().startswith('#'))
    
    # Imported libraries
    tree = ast.parse(code)
    import_count = sum(isinstance(node, (ast.Import, ast.ImportFrom)) for node in tree.body)
    
    # Check for unwanted test cases
    unwanted_test_cases = bool(re.search(r'\bdef\s+test_', code))
    test_case_count = len(re.findall(r'\bdef\s+test_', code))
    
    return code_length, comment_count, import_count, unwanted_test_cases, test_case_count

def run_pytest(test_file_path):
    result = subprocess.run(['pytest', test_file_path], capture_output=True, text=True)
    output = result.stdout
    
    # Extract passed and failed tests
    passed_tests = sum(int(match) for match in re.findall(r'(\d+) passed', output))
    failed_tests = sum(int(match) for match in re.findall(r'(\d+) failed', output))
    
    # Extract error messages
    error_messages = re.findall(r'=== FAILURES ===\n(.*?)\n====', output, re.DOTALL)
    error_messages += re.findall(r'ERROR at setup of test.*?\n(.*?)\n', output, re.DOTALL)
    
    return passed_tests, failed_tests, error_messages


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
            if file.endswith('.py') and file != current_script and 'test' not in file.lower():
                file_path = os.path.join(root, file)
                print(f'Processing file: {file_path}')
                try:
                    prompt_technique = determine_prompting_technique(file)
                    task_name = os.path.basename(root)
                    execution_time = measure_performance(file_path)
                    
                    code_length, comment_count, import_count, unwanted_test_cases, test_case_count = extract_code_metrics(file_path)
                # Find corresponding test file
                    test_file_path = os.path.join(root, f'test_{file}')
                    if os.path.exists(test_file_path):
                        passed_tests, failed_tests, error_messages = run_pytest(test_file_path)
                    else:
                        passed_tests, failed_tests, error_messages = 0, 0, []
                    
                    data.append({
                        'Testlauf-ID': file,
                        'Datum/Zeit': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'Prompting-Technik': prompt_technique,
                        'Programmieraufgabe': task_name,
                        #'Antworttext': '',  # Not applicable here
                        #'Codeauszug': '',  # Not applicable here
                        'Länge des Codes': code_length,
                        'Kommentare im Code': comment_count,
                        'Anzahl der importierten Bibliotheken': import_count,
                        'Bestandene Testfälle': passed_tests,
                        'Nicht bestandene Testfälle': failed_tests,
                        #'Fehlermeldungen': error_messages,
                        'Ausführungszeit': execution_time,
                        'Unerwünschte Testfälle vorhanden': '',
                        'Unerwünschte Beispiele vorhanden': '',
                        'Besondere Beobachtungen': '',  # Placeholder for any notes
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