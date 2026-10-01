class TextAnalyzer:

    def __init__(self, text: str):
        self.text = text

    def count_character(self):
        return len(self.text)

    def count_words(self):
        words_list = self.text.split()
        return len(words_list)

    def count_sentences(self):
        sentences_count = 0

        for character in self.text:
            if character in '.?!':
                sentences_count += 1

        return sentences_count

    def count_unique_words(self):
        unique_count = 0
        lower_text = self.text.lower()
        unique_list = []

        for word in lower_text.split():
            if word not in unique_list:
                unique_list.append(word)
                unique_count += 1

        return unique_count

    def word_frequency(self):
        frequency_dict = {}
        lower_text = self.text.lower()

        for word in lower_text.split():
            if word not in frequency_dict:
                frequency_dict[word] = 1
            else:
                frequency_dict[word] += 1

        return frequency_dict
