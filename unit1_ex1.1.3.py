# exercise 1.1.3 from unit 1
'''
Write a function called four_dividers defined as follows:

def four_dividers(number):
The function accepts a number and returns a list of
all numbers from 1 to that number (inclusive) that are
divisible by four without a remainder.


Examples of running the four_dividers function:

print(four_dividers(9))
print(four_dividers(3))
[4, 8]
[]
Guidelines:

It is forbidden to use an external library, except
 the functools library.
Do not use loops.
The four_dividers function block must contain only one
 line of code.
You can implement an additional auxiliary function as you wish.
'''

def four_dividers(number):
    def is_divisible_by_four(x):
        return x % 4 == 0
    return list(filter(is_divisible_by_four, range(1, number + 1)))

def main():
    print(four_dividers(20))

if __name__ == "__main__":
    main()
