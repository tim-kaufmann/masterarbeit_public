import os

def label_filter(annotation_folder_path, label_category):
    for filename in os.listdir(annotation_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            filtered_lines = []
            for line in lines:
                label = int(line.split()[0])
                if label in label_category:
                    filtered_lines.append(line)
            
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
