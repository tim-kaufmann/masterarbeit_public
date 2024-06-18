import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder {source_folder} does not exist.")
    
    # Check if the target folder exists, if not, create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Walk through the source folder
    for dirpath, dirnames, filenames in os.walk(source_folder):
        # Construct the target path
        relative_path = os.path.relpath(dirpath, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        
        # Create directories in the target path
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy each file in the current directory to the target path
        for file in filenames:
            source_file = os.path.join(dirpath, file)
            target_file = os.path.join(target_path, file)
            shutil.copy2(source_file, target_file)
    
    print("Backup completed successfully.")
