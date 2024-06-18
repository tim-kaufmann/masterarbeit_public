import os

def label_filter(annotation_folder: str, Label_category: list):
    # Loop through all files in the given annotation folder
    for filename in os.listdir(annotation_folder):
        file_path = os.path.join(annotation_folder, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Filter the lines based on the Label_category
            filtered_lines = [line for line in lines if int(line.split()[0]) not in Label_category]
            
            # Write the filtered lines back to the file
            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)
