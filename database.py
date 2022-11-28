class data:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read()
        self.write()

    def read(self):
        with open(self.file_name, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)