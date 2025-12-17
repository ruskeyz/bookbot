import sys
from stats import get_book_text, count_words, count_chars, chars_to_list

# path = "books/frankenstein.txt"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("------------ Word Count ------------")
    count_words(content)
    print("---------- Character Count ----------")
    dict = count_chars(content)
    chars_to_list(dict)
    print("============ END ============")


main()
