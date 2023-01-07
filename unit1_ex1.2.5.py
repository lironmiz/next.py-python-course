# exercise 1.2.5 from unit 1
'''
Reverse engineering, or reverse engineering (in English: Reverse engineering),
is the study of something by breaking it down into its components and learning how it works.
Today, reverse engineering is widely used in the world of computers, when studying computer code.

Here is a piece of code that asks the user to enter a password as input. The code checks whether 
the entered password is correct (that is, meets certain conditions) or not and prints an
appropriate output to the screen.
'''

import functools
def function(num, item):
    return num + 1
password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")
    
#  After you understand how the code works, choose from the following inputs the input for which 
# the output will be printed: "!Correct password"
# Answer: 1234
