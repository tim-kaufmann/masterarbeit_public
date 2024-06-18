import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Check if the target folder exists, create if it does not exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Traverse all files and subfolders in the source folder
    for dirpath, dirnames, filenames in os.walk(source_folder):
        # Build the corresponding target path
        relative_path = os.path.relpath(dirpath, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        
        # Create the subfolders in the target folder
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy each file preserving metadata
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(target_path, filename)
            shutil.copy2(src_file, dest_file)
    
    print("Backup completed successfully.")
