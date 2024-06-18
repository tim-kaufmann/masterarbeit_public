import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Check if target folder exists, create if it does not
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Traverse all files and subfolders in the source folder
    for root, dirs, files in os.walk(source_folder):
        # Create corresponding subfolders in the target folder
        relative_path = os.path.relpath(root, source_folder)
        target_subfolder = os.path.join(target_folder, relative_path)
        if not os.path.exists(target_subfolder):
            os.makedirs(target_subfolder)
        
        # Copy files to the target subfolders
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_subfolder, file)
            shutil.copy2(source_file, target_file)
    
    print("Backup completed successfully.")
