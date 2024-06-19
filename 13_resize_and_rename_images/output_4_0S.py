import os

class list_files:
    def __init__(self, path):
        self.path = path
        self.check_and_list_files()

    def check_and_list_files(self):
        if not os.path.exists(self.path):
            print("Invalid directory path.")
        else:
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    print(file)
