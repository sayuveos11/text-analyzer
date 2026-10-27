import unittest
from unittest.mock import patch, mock_open
import tempfile
from file_handler import FileHandler
from pathlib import Path


class TestSaveFile(unittest.TestCase):

    def test_save_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / 'result.txt'
            read_file = FileHandler(file_path)
            result = read_file.save_file("Hello Python!")

            self.assertTrue(result)
            self.assertEqual(file_path.read_text(encoding='utf-8'), "Hello Python!")

    def test_save_file_overwrite(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / 'result.txt'

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("Hello Python!")

            read_file = FileHandler(file_path)
            result = read_file.save_file("New content")

            self.assertTrue(result)
            self.assertEqual(file_path.read_text(encoding='utf-8'), "New content")

    @patch('builtins.open')
    def test_save_file_permission_error(self, mock_open):
        mock_open.side_effect = PermissionError("Permission denied")
        file_path = Path("permission_error.txt")
        file_handler = FileHandler(file_path)
        self.assertFalse(file_handler.save_file("Hello Python!"))
        mock_open.assert_called_once_with(file_path, 'w', encoding='utf-8')