import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"Source folder '{source_folder}' does not exist.")
    
    # Check if target folder exists, if not, create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Traverse all files and subfolders in the source folder
    for root, dirs, files in os.walk(source_folder):
        # Build the relative path from the source folder
        relative_path = os.path.relpath(root, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        
        # Create corresponding subfolders in the target folder
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy each file to the target path
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_path, file)
            shutil.copy2(source_file, target_file)
    
    print("Backup completed successfully.")

# Example usage:
# backup_folder('/path/to/source_folder', '/path/to/target_folder')
