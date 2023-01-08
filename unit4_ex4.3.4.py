# exercise 4.3.4 from unit 4
'''
Write a generator function called get_fibo defined as follows:

def get_fibo():
The function returns a generator that produces members of the Fibonacci series.

In mathematics, the Fibonacci series is a series whose first two terms are 0 and 1 and each term after that is equal to the sum of the two numbers preceding it. Accordingly, the first members of the series are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

An example of running the get_fibo generator function:

To view an accessible code snippet
fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
Guidelines:

A generator function that returns a generator for generating numbers in the Fibonacci series.
'''
def get_fibo():
    yield 0
    yield 1
    fibo_numbers = [0, 1]
    while True:
        length = len(fibo_numbers)
        fibo_numbers.append(
            fibo_numbers[length - 1] + fibo_numbers[length - 2])
        yield fibo_numbers[len(fibo_numbers) - 1]


def get_fibo_better():
    yield 0
    yield 1
    x = 0
    y = 1
    while True:
        num = x + y
        x = y
        y = num
        yield num


def main():
    fibo_gen = get_fibo_better()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == "__main__":
    main()
    
