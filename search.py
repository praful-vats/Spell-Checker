import collections
import re

def read_words(file_name):
    with open(file_name, "r") as file:
        return re.findall(r"[a-z]+", file.read().lower())

"""To read the words from the file and return a list of words
Time complexity = O(n)
Space complexity = O(n)
n=number of characters in file"""


def create_dictionary(words):
    dictionary = collections.defaultdict(list)
    for word in words:
        index = "".join([str(word.count(c)) for c in "abcdefghijklmnopqrstuvwxyz"])
        dictionary[index].append(word)
    return dictionary

"""To create a dictionary from the list of words and return it
Time complexity = O(n*m)
Space complexity = O(n*m)
n=number of words
m=maximum length of words"""


def search_word(dictionary, word):
    index = "".join([str(word.count(c)) for c in "abcdefghijklmnopqrstuvwxyz"])
    words_at_index = dictionary.get(index, [])
    if word in words_at_index:
        return [word]
    else:
        return None

"""To searche the provided word in the dictionary and returns the relevant searched words
Time complexity = O(1)
Space complexity = O(1)"""


def spell_check(dictionary, word):
    suggestions = set()
    for i in range(len(word)):
        temp_word = word[:i] + word[i+1:]
        result = search_word(dictionary, temp_word)
        if result is not None:
            suggestions |= set(result)
    return suggestions

"""To find the possible spelling mistakes in the word and return the suggested words
Time complexity = O(n*m)
Space complexity = O(n*m)
n=number of words
m=maximum length of words"""


def main():
    words = read_words("list.txt")
    dictionary = create_dictionary(words)
    while True:
        word_to_search = input("Enter word to search (or 'q' to quit): ").lower()
        if word_to_search == "q":
            break
        searched_words = search_word(dictionary, word_to_search)
        if searched_words:
            print(f"Searched Words : {searched_words}")
        else:
            print(f"No word found for {word_to_search}")
            suggestions = spell_check(dictionary, word_to_search)
            if suggestions:
                print(f"Did you mean : {suggestions}")

"""Time complexity = O(n*m)
Space complexity = O(n*m)
n=number of words
m=maximum length of words"""

if __name__ == "__main__":
    main()
