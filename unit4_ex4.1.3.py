# exercise 4.1.3 from unit 4
'''
Write a function called first_prime_over defined as follows:

def first_prime_over(n):
The function accepts as a parameter an integer (n). The function returns the first prime number that comes after n.

An example of running the first_prime_over function:

print(first_prime_over(1000000))
1000003
Realize the function so that the process of producing the initial numbers is done using a generator.
To remind you, a prime number is a number greater than 1 that is divisible by 1 and itself only. For your convenience, below is an implementation of a boolean function that checks whether a number is prime or not:
def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
'''

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def main():
    def first_prime_over(n):
        def generate_numbers():
            # Start with the number after n
            num = n + 1
            while True:
                yield num
                num += 1

        for num in generate_numbers():
            if is_prime(num):
                return num

    print(first_prime_over(5))
    # Output: 1000003

if __name__ == "__main__":
    main()
