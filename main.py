from text_analyzer import TextAnalyzer
from file_handler import FileHandler 

def main():
    analyzer_work = True

    while analyzer_work:

        print("\n=== TEXT ANALYZER ===\n")

        print("1. Enter text manually")
        print("2. Read text from file")
        print("3. Exit\n")

        try:
            user_choice = int(input("Choose option: "))
        except ValueError:
            print("Please enter a correct number")
            continue
            

        if user_choice == 1:
            text = input("Enter your text: ")

            analyzer = TextAnalyzer(text)
            print("\n=== TEXT ANALYZER ===\n")

            print("Characters:", analyzer.count_characters())
            print("Words:", analyzer.count_words())
            print("Sentences:", analyzer.count_sentences())
            print("Unique words:", analyzer.count_unique_words())
            print(f"Average word length: {analyzer.average_word_length()} \n")

            word_frequency_pair = analyzer.word_frequency()
            print("Word frequency: ")

            for k, v in word_frequency_pair.items():
                print(f"{k}: {v}")

            print()

        elif user_choice == 2:
            file_path = input("Enter a path to the file: ")
            handler  = FileHandler(file_path)
            text = handler.open_file()

            if text is not None:
                analyzer = TextAnalyzer(text)
                print("\n=== TEXT ANALYZER ===\n")
                
                print("Characters:", analyzer.count_characters())
                print("Words:", analyzer.count_words())
                print("Sentences:", analyzer.count_sentences())
                print("Unique words:", analyzer.count_unique_words())
                print(f"Average word length: {analyzer.average_word_length()} \n")
                    
                word_frequency_pair = analyzer.word_frequency()
                print("Word frequency: ")
                    
                for k, v in word_frequency_pair.items():
                    print(f"{k}: {v}")
                    
                print()
            else:
                print("File not found. Please check the file path.")

        elif user_choice == 3:
            analyzer_work = False

        else:
            print("Enter correct number")


if __name__ == "__main__":
    main()