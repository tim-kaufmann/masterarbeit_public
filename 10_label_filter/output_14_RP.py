import os

def label_filter(folder_path, Label_category):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    if int(line.split()[0]) not in Label_category:
                        file.write(line)
