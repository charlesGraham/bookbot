def get_word_count(text):
    words = text.split()
    print(f"{len(words)} words found in the document")


def get_char_count(text):
    lowercase_text = text.lower()
    char_count = {}
    for char in lowercase_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    print(char_count)
