# exercise 6.2.1 from unit 6
'''
Here are two files named file1.py and file2.py.

file1.py
def change(a):
    b = [x * 2 for x in a]
    print(b)
file2.py
def change(a):
    b = [x * x for x in a]
    print(b)
What will be printed to the screen following the execution of the following code snippet?

from file1 import change
from file2 import change
def main():
    my_lst = [1, 2, 3]
    change(my_lst)
main()
'''

# Answer: [9 ,4 ,1]
