# exercise 1.1.4 from unit 1
'''
Write a function called sum_of_digits defined as follows:

def sum_of_digits(number):
The function accepts a number and returns the sum of its digits.

An example of running the sum_of_digits function:

print(sum_of_digits(104))
5
Guidelines:

It is forbidden to use an external library, except the functools library.
Do not use loops.
The sum_of_digits function block must contain only one line of code.
You can implement an additional auxiliary function as you wish.'''

import functools

def sum_of_digits(number):
    def add(x, y):
        return x + y
    return functools.reduce(add, [int(digit) for digit in str(number)])


def main():
    print(sum_of_digits(11347))

if __name__ == "__main__":
    main()
