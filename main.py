from text_analyzer import TextAnalyzer

def main():
    text = input("Enter your text: ")

    analyzer = TextAnalyzer(text)

    print("Characters:", analyzer.count_characters())
    print("Words:", analyzer.count_words())
    print("Sentences:", analyzer.count_sentences())


if __name__ == "__main__":
    main()