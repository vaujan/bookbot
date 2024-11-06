def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    words = get_words(lowered_text)
    chararcters_number = get_num_characters(words)
    sorted_charachters_number = sorted(chararcters_number, reverse=True, key=lambda k: k['count'])

    print(f'"--- Begin report of {book_path} ---"')
    print(f'{len(words)} was found in the document')
    print ()
    for charachter in sorted_charachters_number: 
        print(f"The '{charachter["letter"]}' was found {charachter["count"]} times")
    print ()
    print ()

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return words
def get_num_characters(list):
    characters_count_list = []

    for word in list:
        for letter in word:
            if letter.isalpha():
                found = False
                for char_dict in characters_count_list: 
                    if char_dict["letter"] == letter:
                        char_dict["count"] += 1
                        found = True
                        break
                if not found:
                    characters_count_list.append({"letter": letter, "count": 1})
    return characters_count_list

def sort_on(dict):
    return dict["count"]

main()
