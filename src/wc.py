class wc:
    def __init__(self):
        pass

    def read_bytes(self, string):
        return len(string.encode('utf-8'))

    def read_bytes_from_file(self, filepath):
        try:
            with open(filepath, 'rb') as file:
                 file_contents = file.read()
            file_length = len(file_contents)
            return file_length
        except:
            raise FileNotFoundError