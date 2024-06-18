import os
import shutil

def backup_folder(source_folder, target_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        raise Exception(f"The source folder '{source_folder}' does not exist.")

    # Check if the target folder exists, if not, create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Walk through the source folder
    for root, dirs, files in os.walk(source_folder):
        # Create corresponding directories in the target folder
        for dir in dirs:
            source_dir_path = os.path.join(root, dir)
            relative_path = os.path.relpath(source_dir_path, source_folder)
            target_dir_path = os.path.join(target_folder, relative_path)
            if not os.path.exists(target_dir_path):
                os.makedirs(target_dir_path)

        # Copy each file to the target folder
        for file in files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_file_path, source_folder)
            target_file_path = os.path.join(target_folder, relative_path)
            shutil.copy2(source_file_path, target_file_path)

    print("Backup completed successfully.")
