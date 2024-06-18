import os

def label_filter(annotation_folder_path, Label_category):
    # Convert Label_category to set for faster lookup
    label_set = set(Label_category)
    
    # Iterate through all files in the annotation folder
    for filename in os.listdir(annotation_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(annotation_folder_path, filename)
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
            # Filter the lines that match the label categories
            filtered_lines = [line for line in lines if int(line.split()[0]) in label_set]
            
            # Write the filtered lines back to the file
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
