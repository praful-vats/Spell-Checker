Spell Checker

This is a simple spell checker program that can be used to check the spelling of words in a given text file. The program has the following features:

Reads words from a text file and returns a list of words
Creates a dictionary from the list of words
Searches the provided word in the dictionary and returns the relevant searched words
Finds the possible spelling mistakes in the word and return the suggested words
Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You will need to have Python 3 installed on your machine to run this program. You can download it from here.

Installation
Clone the repository
Copy code
git clone https://github.com/praful-vats/spell-checker.git
Navigate to the cloned repository
Copy code
cd spell-checker
Run the program
Copy code
python spell-checker.py
Usage
The program will prompt you to enter a word to search. Enter the word you want to search and press enter. If the word is found in the dictionary, it will be displayed on the screen. If the word is not found, the program will suggest similar words that might be the word you were looking for. To exit the program, type 'q' and press enter.

The program uses the file 'list.txt' as the source of words. You can replace this file with any other text file of your choice.

Time and Space Complexity
The time and space complexity of each function are as follows:

read_words(file_name): O(n) time complexity and O(n) space complexity
create_dictionary(words): O(nm) time complexity and O(nm) space complexity
search_word(dictionary, word): O(1) time complexity and O(1) space complexity
spell_check(dictionary, word): O(nm) time complexity and O(nm) space complexity
main(): O(nm) time complexity and O(nm) space complexity
Contributing
Feel free to submit pull requests and issues on the Github page.

Authors

Praful Vats
