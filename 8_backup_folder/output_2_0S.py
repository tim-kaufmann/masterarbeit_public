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
    for dirpath, dirnames, filenames in os.walk(source_folder):
        # Construct the target path
        relative_path = os.path.relpath(dirpath, source_folder)
        target_path = os.path.join(target_folder, relative_path)
        
        # Create the corresponding subfolders in the target folder
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # Copy files
        for filename in filenames:
            source_file = os.path.join(dirpath, filename)
            target_file = os.path.join(target_path, filename)
            shutil.copy2(source_file, target_file)
    
    print(f"Backup of '{source_folder}' to '{target_folder}' completed successfully.")

# Example usage
# backup_folder("/path/to/source_folder", "/path/to/target_folder")
