import os

class list_files:
    def __init__(self, path):
        self.path = path
        self.print_files()

    def print_files(self):
        if not os.path.exists(self.path) or not os.path.isdir(self.path):
            print("Invalid directory path.")
        else:
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    print(file)
