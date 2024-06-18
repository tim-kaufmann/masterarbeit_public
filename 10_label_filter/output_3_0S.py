import os

def label_filter(annotation_folder_path, Label_category):
    for filename in os.listdir(annotation_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            with open(file_path, 'w') as file:
                for line in lines:
                    category = int(line.split()[0])
                    if category in Label_category:
                        file.write(line)
