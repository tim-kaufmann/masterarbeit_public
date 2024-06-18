import os

def label_filter(annotation_folder_path, Label_category):
    # Ensure Label_category contains strings for comparison with YOLO format labels
    Label_category = [str(label) for label in Label_category]
    
    for filename in os.listdir(annotation_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder_path, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            with open(file_path, "w") as file:
                for line in lines:
                    if line.split()[0] in Label_category:
                        file.write(line)
