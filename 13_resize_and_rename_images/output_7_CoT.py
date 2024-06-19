import os

class ListFiles:
    def __init__(self, path):
        self.path = path
        self.list_files()

    def list_files(self):
        if not os.path.exists(self.path):
            print("Invalid directory path.")
            return

        for root, _, files in os.walk(self.path):
            for file in files:
                print(file)

def list_files(path):
    ListFiles(path)
