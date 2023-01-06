# exercise 1.1.2 from unit 1
'''
Write a function called double_letter defined as follows:

def double_letter(my_str):
The function accepts a string and returns a new string made up of two consecutive occurrences of each character in the original string.

Examples of running the double_letter function:

print(double_letter("python"))
print(double_letter("we are the champions!"))
'ppyytthhoonn'
'wwee aarree tthhee cchhaammppiioonnss!!'
Guidelines:

It is forbidden to use an external library, except the functools library.
Do not use loops.
The double_letter function block must contain only one line of code.
You can implement an additional auxiliary function as you wish.
Hint
You can use the join method.
'''

def double_letter(my_str):
    def letter_twice(my_char):
        return my_char * 2
    return ''.join(list(map(letter_twice, my_str)))

def main():
    print(double_letter("we are the champions"))

if __name__ == "__main__":
    main()
