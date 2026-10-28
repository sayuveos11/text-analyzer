from text_analyzer import TextAnalyzer
from file_handler import FileHandler 
from pathlib import Path

def display_analysis(text):
    analyzer = TextAnalyzer(text)

    result = (
        f"Characters: {analyzer.count_characters()}\n"
        f"Words: {analyzer.count_words()}\n"
        f"Sentences: {analyzer.count_sentences()}\n"
        f"Unique words: {analyzer.count_unique_words()}\n"
        f"Average word length: {analyzer.average_word_length()}\n"
    )

    word_frequency_pair = analyzer.word_frequency()

    result += "\nWord frequency:\n"

    for k, v in word_frequency_pair.items():
        result += f"{k}: {v}\n"

    print(result)
    return result

def save_analyzis_result(result, source_path=None):
    user_choice = input("Save results to file? (y/n): ")
                
    if user_choice.lower() == 'y':

        while True:
            file_path = Path(input("Enter a path to the file: "))

            if source_path is not None and Path(file_path).resolve() == Path(source_path).resolve():
                print("Cannot overwrite the source file!")
                continue

            if file_path.exists():
                overwrite = input("File already exists. Overwrite? (y/n): ")

                if overwrite.lower() != 'y':
                    continue

            save_handler = FileHandler(file_path)
            save_results = save_handler.save_file(result)
                    
            if save_results:
                print("Results saved successfully!")
            else:
                print("Failed to save results.")

            break

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
            result = display_analysis(text)
            save_analyzis_result(result) 

        elif user_choice == 2:
            file_path = input("Enter a path to the file: ")
            handler  = FileHandler(file_path)
            text = handler.open_file()

            if text is not None:
                result = display_analysis(text)
                save_analyzis_result(result, source_path=file_path)
            else:
                print("Failed to read the file.")

        elif user_choice == 3:
            analyzer_work = False

        else:
            print("Enter correct number")


if __name__ == "__main__":
    main()