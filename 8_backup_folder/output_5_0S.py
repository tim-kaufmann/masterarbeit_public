import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Check if target folder exists, if not, create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Walk through all files and subfolders in the source folder
    for root, dirs, files in os.walk(source_folder):
        # Construct the relative path
        rel_path = os.path.relpath(root, source_folder)
        target_path = os.path.join(target_folder, rel_path)
        
        # Create corresponding subfolders in the target folder
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy files to the target folder, preserving metadata
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_path, file)
            shutil.copy2(source_file, target_file)
    
    print("Backup successful.")
