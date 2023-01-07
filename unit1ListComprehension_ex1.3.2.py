# exercise 1.3.2 from unit 1
'''
Write a function called is_prime defined as follows:

def is_prime(number):
The function accepts a number and returns a boolean value representing whether it is prime (True-prime, False-not prime). A prime number is a number that is divisible by itself and 1 without a remainder.

An example of running the is_prime function:

print(is_prime(42))
print(is_prime(43))
False
True
Guidelines:

It is forbidden to use an external library, except the functools library.
It is allowed to use the for loop only within a list assembly structure.
The is_prime function block must contain only one line of code.
Do not implement additional helper functions in the code.
'''

import functools

def is_prime(number):
    return  False if number < 2  else all(number % i for i in range(2, int(number ** 0.5) + 1))


def main():
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(5))
    print(is_prime(6))
    print(is_prime(7))
    print(is_prime(59))

if __name__ == "__main__":
    main()
