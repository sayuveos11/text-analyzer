class TextAnalyzer:

    def __init__(self, text: str):
        self.text = text

    def normalize_text(self):
        words_text = []

        for char in self.text:
            if char not in '.?!:;,':
                words_text.append(char)

        lower_text = "".join(words_text)
        return lower_text.lower()

    def count_characters(self):
        return len(self.text)

    def count_words(self):
        words_list = self.normalize_text().split()
        return len(words_list)

    def count_sentences(self):
        sentences_count = 0

        for character in self.text:
            if character in '.?!':
                sentences_count += 1

        return sentences_count

    def count_unique_words(self):
        unique_count = 0
        lower_text = self.normalize_text()
        unique_list = []

        for word in lower_text.split():
            if word not in unique_list:
                unique_list.append(word)
                unique_count += 1

        return unique_count

    def word_frequency(self):
        frequency_dict = {}
        lower_text = self.normalize_text()

        for word in lower_text.split():
            if word not in frequency_dict:
                frequency_dict[word] = 1
            else:
                frequency_dict[word] += 1

        return frequency_dict
            
    def average_word_length(self):
        average_count = 0
        words_list = self.normalize_text().split()

        for word in words_list:
            average_count += len(word)

        if words_list:
            average_length = average_count / len(words_list)
        else:
            average_length = 0

        return round(average_length, 2)

        
