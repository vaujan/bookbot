def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    words = get_words(lowered_text)
    chararcters_number = get_num_characters(words)
    sorted_charachters_number = dict(sorted(chararcters_number.items()))
    return print(f'List of the characters number are: {sorted_charachters_number}')


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return words

def get_num_characters(list):
    charachters_count = {}

    for word in list:
        for char in word:
            if char not in charachters_count:
                charachters_count[char] = 1
            else:
                charachters_count[char] += 1

    return charachters_count

main()