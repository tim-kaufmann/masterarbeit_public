import os

def label_filter(annotation_folder: str, Label_category: list):
    for filename in os.listdir(annotation_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            with open(file_path, 'w') as file:
                for line in lines:
                    label = int(line.split()[0])
                    if label in Label_category:
                        file.write(line)
