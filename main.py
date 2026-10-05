from text_analyzer import TextAnalyzer

def main():
    text = input("Enter your text: ")

    analyzer = TextAnalyzer(text)
    print("\n=== TEXT ANALYZER ===\n")

    print("Characters:", analyzer.count_characters())
    print("Words:", analyzer.count_words())
    print("Sentences:", analyzer.count_sentences())
    print("Unique words:", analyzer.count_unique_words())
    print(f"Average word length: {analyzer.average_word_length()} \n")

    word_frequency_pear = analyzer.word_frequency()
    print("Word frequency: ")

    for k, v in word_frequency_pear.items():
        print(f"{k}: {v}")

    print()

if __name__ == "__main__":
    main()