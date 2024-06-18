import os

class ListFiles:
    def __init__(self, path):
        self.path = path

    def list_files(self):
        if not os.path.exists(self.path) or not os.path.isdir(self.path):
            print("Invalid directory path.")
        else:
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    print(file)

def list_files(path):
    lf = ListFiles(path)
    lf.list_files()
