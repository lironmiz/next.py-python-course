# exercise 1.3.2 from unit 1
'''
Here is a function called is_funny that accepts a string and returns true only if the received string is made up entirely of the characters 'h' and 'a':

def is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True
Write the function is_funny so that it performs the same operation, in only one line of code.

An example of running the is_funny function:

print(is_funny("hahahahahaha"))
True
'''

import functools

# one line version
def is_funny(string):
    return all(char == 'h' or char == 'a' for char in string)

def main():
    print(is_funny("hbnhahahahaha"))


if __name__ == "__main__":
    main()
