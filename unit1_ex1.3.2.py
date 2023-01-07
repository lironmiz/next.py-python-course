# exercise 1.3.1 from unit 1
'''
Write a function called intersection defined as follows:

def intersection(list_1, list_2):
The function accepts two lists and returns a list of the members that are in the intersection between them. That is, members that are in both the first list and the second list. No member will appear twice in the cut list.

An example of running the intersection function:

print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
[3]
[5,6]
Guidelines:

It is forbidden to use an external library, except the functools library.
It is allowed to use the for loop only within a list assembly structure.
The intersection function block must contain only one line of code.
Do not implement additional helper functions in the code.
'''

import functools

def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))


def main():
    print(intersection([1, 2, 3, 4], [1, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 7, 7, 6]))

if __name__ == "__main__":
    main()
