# exercise 5.2.2 from unit 5
'''
Given the following code:

numbers = iter(list(range(1, 101)))
for i in numbers:
    print(i)
Change the code so that it prints every third number only, without using the if command.
'''

import itertools

numbers = list(range(1, 101))
filtered_numbers = itertools.islice(numbers, 2, None, 3)
for i in filtered_numbers:
    print(i)
