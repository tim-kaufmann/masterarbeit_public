import os

def label_filter(folder_path, Label_category):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.endswith(".txt"):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            filtered_lines = [line for line in lines if int(line.split()[0]) not in Label_category]
            
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
