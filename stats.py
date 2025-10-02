def number_of_words(book: str):
    word_count = 0
    for word in book.split():
        word_count +=1
    return word_count


def number_times_character(book: str):
    book = book.lower()

    dictionary = {}

    for word in book.split():
        for letter in word:
            if letter not in dictionary:
                dictionary[letter]= 0
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                raise Exception('Dictionary error!')
    return dictionary

def sort_on(items):
    return items['num']

def sorted_dictionary(characters: dict):
    new_list = []

    for i in characters:
        key = i
        value = characters[i]
        dict = {"char": key, "num": value}
        new_list.append(dict)
    
    new_list.sort(reverse=True,key=sort_on)
    for value in new_list:
        if value["char"].isalpha() == True:
            print(f"{value["char"]}: {value["num"]}")
