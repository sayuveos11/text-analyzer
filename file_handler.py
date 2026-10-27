class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def open_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = f.read()
                return data
        except (FileNotFoundError, PermissionError, UnicodeDecodeError):
            return None

    def save_file(self, content):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except OSError:
            return False

        return True