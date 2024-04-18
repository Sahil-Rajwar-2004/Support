import os

version = "0.0.1"

class SearchFile:
    def __init__(self,filename,directory = os.getcwd()):
        self.filename = filename
        self.directory = directory

    def search(self):
        for root,_,files in os.walk(self.directory):
            if self.filename in files:
                return os.path.join(root,self.filename)
        return f"file: '{self.filename}' not found at '{self.directory}'"

class FileFilter:
    def __init__(self,file_extension,directory = os.getcwd()):
        self.file_extension = file_extension
        self.directory = directory

    def search(self):
        contents = os.listdir(self.directory)
        matching_files = []
        for file in contents:
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path) and (self.file_extension is None or file.lower().endswith(self.file_extension.lower())):
                matching_files.append(file_path)
        return matching_files

