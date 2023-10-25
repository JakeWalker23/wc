class wc:
    def __init__(self):
        pass

    def read_bytes_from_file(self, filepath):
        try:
            with open(filepath, 'rb') as file:
                file_contents = file.read()
                return f"{len(file_contents)} {filepath}"
        except:
            raise FileNotFoundError

    def read_lines_from_file(self, filepath):
        try:
            with open(filepath, 'rb') as file:
                file_line_count = file.readlines()
                return f"{len(file_line_count)} {filepath}"
        except:
            raise FileNotFoundError

    def read_words_from_file(self, filepath):
        try:
            with open(filepath, 'r') as file:
                file_contents = file.read()
                word_count = file_contents.split()
                return f"{len(word_count)} {filepath}"
        except:
            raise FileNotFoundError