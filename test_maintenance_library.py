import unittest
from unittest.mock import patch
from maintenance_library import ConsoleApp
from library import Library

class TestConsoleApp(unittest.TestCase):
    def setUp(self):
        self.app = ConsoleApp()

    @patch('builtins.input', side_effect=['Название книги', 'Автор книги', '2023'])
    @patch('library.Library.add_book')
    def test_add_book(self, mock_add_book, mock_input):
        self.app.add_book()
        mock_add_book.assert_called_with('Название книги', 'Автор книги', '2023')

if __name__ == '__main__':
    unittest.main()