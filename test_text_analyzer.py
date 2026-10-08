import unittest
from text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):

    def test_count_words_normal_text(self):
        text = "Hello world Python"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.count_words(), 3)

    def test_count_words_empty_text(self):
        text = ""
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.count_words(), 0)

    def test_count_words_multiple_spaces(self):
        text = "Hello    World"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.count_words(), 2)

    def test_normalize_text(self):
        text = "Hello,world"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.normalize_text(), "hello world")

    def test_word_frequency(self):
        text = "Hello,hello HELLO!"
        analyzer = TextAnalyzer(text)

        expected_result = {
            "hello": 3
        }

        self.assertEqual(analyzer.word_frequency(), expected_result)

    def test_count_unique_words(self):
        text = "Python is great Python"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.count_unique_words(), 3)

    def test_count_unique_words_empty(self):
        text = ""
        analyzer = TextAnalyzer(text)
    
        self.assertEqual(analyzer.count_unique_words(), 0)

    def test_count_unique_words_repeated(self):
            text = "Hello hello HELLO"
            analyzer = TextAnalyzer(text)
    
            self.assertEqual(analyzer.count_unique_words(), 1)
