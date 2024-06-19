import os

class list_files:
    def __init__(self, path):
        self.path = path
        self.validate_and_list_files()

    def validate_and_list_files(self):
        if not os.path.exists(self.path) or not os.path.isdir(self.path):
            print("Invalid directory path.")
        else:
            self.list_files_recursive(self.path)
    
    def list_files_recursive(self, current_path):
        for root, dirs, files in os.walk(current_path):
            for file in files:
                print(file)
