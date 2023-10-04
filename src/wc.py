class wc:
    def __init__(self):
        pass

    def read_bytes_from_file(self, filepath):
        try:
            with open(filepath, 'rb') as file:
                file_contents = file.read()
                return len(file_contents)
        except:
            raise FileNotFoundError