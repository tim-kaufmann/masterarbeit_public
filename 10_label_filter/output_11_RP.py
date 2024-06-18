import os

def label_filter(annotation_folder, Label_category):
    for filename in os.listdir(annotation_folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(annotation_folder, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()

            filtered_lines = []
            for line in lines:
                label = int(line.split()[0])
                if label in Label_category:
                    filtered_lines.append(line)
            
            with open(filepath, 'w') as file:
                file.writelines(filtered_lines)
