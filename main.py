from docx import Document
import codecs

## this is the funciton for counting words ## 
def count_words(file_path):
    try:
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                word_count = len(text.split())
                return word_count
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            # Make sure to decode the text properly for Arabic
            word_count = sum(len(paragraph.text.split()) for paragraph in doc.paragraphs)
            return word_count
        else:
            return "Unsupported file format. Please provide a .txt or .docx file."
    except FileNotFoundError:
        return "File not found."


def main():
    file_path = input("Enter the path to the text file or docx file: ")
    word_count = count_words(file_path)
    if isinstance(word_count, int):
        print(f"The file contains {word_count} words.")
    else:
        print(word_count)


if __name__ == "__main__":
    main()
