import os

class Testlist_files:
    def __init__(self, path):
        self.path = path
        self.list_files()

    def list_files(self):
        if not os.path.exists(self.path):
            print("Invalid directory path.")
        else:
            for root, _, files in os.walk(self.path):
                for file in files:
                    print(file)
