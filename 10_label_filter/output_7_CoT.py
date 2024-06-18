import os

def label_filter(annotation_folder_path, Label_category):
    for filename in os.listdir(annotation_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            filtered_lines = [line for line in lines if int(line.split()[0]) not in Label_category]
            
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
