import unittest
from text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):

    # count_words

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

    # normalize_text

    def test_normalize_text(self):
        text = "Hello,world"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.normalize_text(), "hello world")

    # word_frequency

    def test_word_frequency(self):
        text = "Hello,hello HELLO!"
        analyzer = TextAnalyzer(text)

        expected_result = {
            "hello": 3
        }

        self.assertEqual(analyzer.word_frequency(), expected_result)

    # count_unique_words

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

    # count_unique_words() = len(word_frequency())

    def test_unique_equal_frequency(self):
        text = "Python Python Java JavaScript python"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.count_unique_words(), len(analyzer.word_frequency()))

    # average_word_length

    def test_average_word_length(self):
        text = "cat dog"
        analyzer = TextAnalyzer(text)

        self.assertEqual(analyzer.average_word_length(), 3)

    def test_almost_average_word_length(self):
        text = "a bb ccc dddd"
        analyzer = TextAnalyzer(text)

        self.assertAlmostEqual(analyzer.average_word_length(), 2.5, places=2)

    def test_empty_average_word_length(self):
        text = ""
        analyzer = TextAnalyzer(text)
        
        self.assertAlmostEqual(analyzer.average_word_length(), 0)