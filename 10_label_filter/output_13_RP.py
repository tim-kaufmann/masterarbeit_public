import os

def label_filter(annotation_folder_path, label_category):
    # Get a list of all files in the annotation folder
    annotation_files = [f for f in os.listdir(annotation_folder_path) if os.path.isfile(os.path.join(annotation_folder_path, f))]
    
    for annotation_file in annotation_files:
        file_path = os.path.join(annotation_folder_path, annotation_file)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        filtered_lines = []
        for line in lines:
            parts = line.strip().split()
            if int(parts[0]) in label_category:
                filtered_lines.append(line)
        
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)
