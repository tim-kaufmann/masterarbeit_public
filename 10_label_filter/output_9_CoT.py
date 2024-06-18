import os

def label_filter(annotation_folder, Label_category):
    # Convert Label_category to a set for faster lookup
    label_set = set(Label_category)
    
    # Iterate through all files in the annotation folder
    for filename in os.listdir(annotation_folder):
        file_path = os.path.join(annotation_folder, filename)
        
        # Read the file and filter lines based on Label_category
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        filtered_lines = [line for line in lines if int(line.split()[0]) not in label_set]
        
        # Write the filtered lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(filtered_lines)
