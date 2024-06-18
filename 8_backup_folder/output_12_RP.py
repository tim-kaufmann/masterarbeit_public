import os
import shutil

def backup_folder(source_folder, target_folder):
    # Source folder check
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder {source_folder} does not exist.")
    
    # Target folder check
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Traverse all files and subfolders in the source folder
    for dirpath, dirnames, filenames in os.walk(source_folder):
        # Build target path
        relative_path = os.path.relpath(dirpath, source_folder)
        target_dir = os.path.join(target_folder, relative_path)
        
        # Create corresponding subfolders in the target folder
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Copy files
        for file in filenames:
            source_file = os.path.join(dirpath, file)
            target_file = os.path.join(target_dir, file)
            shutil.copy2(source_file, target_file)
    
    # Output success message
    print("Backup completed successfully.")
