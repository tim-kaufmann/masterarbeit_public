import os
import shutil

def backup_folder(source_folder, target_folder):
    # Source folder check
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Target folder check
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Traverse all files and subfolders in the source folder
    for root, dirs, files in os.walk(source_folder):
        # Build target path
        relative_path = os.path.relpath(root, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        
        # Create subfolders in the target folder
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy files
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_path, file)
            shutil.copy2(src_file, dst_file)
    
    print("Backup completed successfully.")
