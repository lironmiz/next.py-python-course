# exercise 4.1.2 from unit 4
'''
Write a function called translate defined as follows:

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the' }
The function accepts as a parameter a string that represents a sentence in the Spanish language and returns a new string that is a translation of the sentence in the English language.

For the sake of simplicity, translate each word in the sentence using the words dictionary that appears inside the translate function. Check that your code works using it (you can also expand the dictionary if you want).

An example of running the translate function:

print(translate("el gato esta en la casa"))
the cat is in the house
Guidelines:

Realize the function to use a generator expression.
'''

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}

    return ' '.join(words[word] for word in sentence.split())


def main():
    choice = 'y'

    # Run the loop until the user chooses to exit
    while choice == 'y':
        sentence = input('Enter a sentence in Spanish: ')
        translation = translate(sentence)
        print(f'Translation: {translation}')

        choice = input('Translate another sentence? (y/n) ')

    print('Goodbye!')


if __name__ == '__main__':
    main()

    
