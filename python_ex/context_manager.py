class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        self.file.close()

with FileManager('C:\\Python3\\python_ex\\test1.txt', 'w') as f:
    f.write('Hello, world!')
