import os

def label_filter(annotation_folder, Label_category):
    # Convert Label_category to a set for faster lookup
    Label_category_set = set(Label_category)
    
    # Iterate over all files in the annotation folder
    for filename in os.listdir(annotation_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            # Filter lines that do not match the categories in Label_category_set
            filtered_lines = [line for line in lines if int(line.split()[0]) not in Label_category_set]
            
            # Write the filtered lines back to the file
            with open(file_path, "w") as file:
                file.writelines(filtered_lines)
