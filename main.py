from stats import get_word_count, get_char_count


def main():
    book_text = get_book_text("books/frankenstein.txt")
    get_word_count(book_text)
    get_char_count(book_text)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


main()
