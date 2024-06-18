import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Check if target folder exists, if not, create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Walk through the source folder
    for root, dirs, files in os.walk(source_folder):
        # Compute the relative path
        relative_path = os.path.relpath(root, source_folder)
        # Compute the corresponding target path
        target_path = os.path.join(target_folder, relative_path)
        
        # Create any necessary directories in the target path
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy files to the target path
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_path, file)
            shutil.copy2(source_file, target_file)
    
    print("Backup completed successfully.")
