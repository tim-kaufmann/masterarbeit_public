import os

def label_filter(annotation_folder, Label_category):
    for filename in os.listdir(annotation_folder):
        file_path = os.path.join(annotation_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            filtered_lines = []
            for line in lines:
                label = int(line.split()[0])
                if label in Label_category:
                    filtered_lines.append(line)

            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
