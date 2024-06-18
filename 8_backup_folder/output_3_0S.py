import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Check if target folder exists, if not, create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Traverse the source folder
    for root, dirs, files in os.walk(source_folder):
        # Construct the relative path from the source folder
        relative_path = os.path.relpath(root, source_folder)
        target_root = os.path.join(target_folder, relative_path)
        
        # Create the corresponding directories in the target folder
        if not os.path.exists(target_root):
            os.makedirs(target_root)
        
        # Copy each file in the directory
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_root, file)
            shutil.copy2(source_file, target_file)
    
    print(f"Backup from '{source_folder}' to '{target_folder}' completed successfully.")

# Example usage:
# backup_folder('path/to/source_folder', 'path/to/target_folder')
