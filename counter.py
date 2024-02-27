def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            return word_count
    except FileNotFoundError:
        return "File not found."


def main():
    file_path = input("Enter the path to the text file: ")
    word_count = count_words(file_path)
    if isinstance(word_count, int):
        print(f"The file contains {word_count} words.")
    else:
        print(word_count)


if __name__ == "__main__":
    main()
