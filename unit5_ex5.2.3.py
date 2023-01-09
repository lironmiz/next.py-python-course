# exercise 5.2.3 from unit 5
'''
In your wallet are 3 $20 bills, 5 $10 bills, 2 $5 bills, and 5 $1 bills.

In how many ways can you create a sum of 100 dollars from the bills?

For example, one way could be using 3 20 bills and 4 10 bills.

Write a program that prints to the screen all the options that can be used to create an amount of 100 dollars from the bills.

How many options did you get?

Guidelines:

Use the function from the itertools library to perform the calculation.
Avoid duplication in the calculation. For example, the option: 10 10 10 10 20 20 20 is exactly the same as the option 20 20 20 10 10 10 10. The internal order does not matter, so these options are counted only once.
First hint
Use the combination function from the itertools library that returns an iterator on which you can iterate.


Second hint
You can use the sum function and the set structure to shorten your solution.
'''

# Answer: 5
