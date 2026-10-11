import unittest
from unittest.mock import patch, mock_open
import tempfile
from file_handler import FileHandler
from pathlib import Path
    
class TestFileHandler(unittest.TestCase):

    def test_read_file(self):
        with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8') as tf:
            tf.write("Hello Python!\nThis is a test")
            tf.flush()
            file_path = Path(tf.name)
            read_file = FileHandler(file_path)
            self.assertEqual(read_file.open_file(), "Hello Python!\nThis is a test")

    def test_read_file_not_found(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "None.txt"
            read_file = FileHandler(file_path)
            self.assertIsNone(read_file.open_file())

    def test_read_empty_file(self):
        with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8') as tf:
            file_path = Path(tf.name)
            read_file = FileHandler(file_path)                
            self.assertEqual(read_file.open_file(), "")

    # permission testing 

    @patch('builtins.open')
    def test_read_permission_error(self, mock_open):
        mock_open.side_effect = PermissionError("Permission denied")
        file_path = Path('permission_error.txt')
        read_file = FileHandler(file_path)
        self.assertIsNone(read_file.open_file())
        mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')

    # unicode error

    @patch('builtins.open')
    def test_read_encoding_error(self, mock_open):

        mock_open.return_value.__enter__.return_value.read.side_effect = UnicodeDecodeError(
            "utf-8",
            b"\xff",
            0,
            1,
            "invalid start byte"
        )

        file_path = Path('encoding_error.txt')
        read_file = FileHandler(file_path)
        self.assertIsNone(read_file.open_file())

        mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')
        mock_open.return_value.__enter__.return_value.read.assert_called_once()


        
