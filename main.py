from stats import number_of_words, number_times_character, sorted_dictionary, sorted_dictionary
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        contents = f.read()
    return contents

def input_validation():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]


def main():
    book_path = input_validation()    
    book = get_book_text(book_path)
    number_words = number_of_words(book)
    dictionary = number_times_character(book)
    print (f"Found {number_words} total words")   
    sorted_dictionary(dictionary)

main()
