class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def open_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = f.read()
                return data
        except FileNotFoundError:
            return None