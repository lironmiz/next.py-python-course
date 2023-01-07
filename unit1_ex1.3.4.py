# exercise 1.3.2 from unit 1
'''
A programmer named Gad turned on the computer in his office and
discovered that he had fallen victim to an attack. A hacker has locked
his computer with a password and is now unable to perform operations on it.

Gad clicked on the "Help" button that appeared on the screen, and a window opened in front of him with the following hint.

After reading the hint, Gad realized that the situation was not lost and that the hacker left him a chance to unlock his computer. The bold inscription represents
 the password for the computer, and the three lines below it are a clue that may help to decipher it.


Here is a Python program that includes a variable named password that points to the password string (as it appears in the hint).

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
# <Add one line of code here>
Use the hint in the body of the message and think: how can you decipher the password to open the computer?
Add lines of code to the program that will cause the decrypted password to be printed to the screen.
Solve the task again, this time using only one line of code that will print the decrypted password to the screen.
Guidelines:

Make use of built-in functions in the language if necessary. Use the internet search to find what you are looking for.
There are several ways to solve the problem in one line of code

'''

import functools

# one line version
def caesar_cipher(string):
    print("".join(chr((ord(c) + 2 - 97) % 26 + 97) if c.isalpha() else c for c in string))

def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print(caesar_cipher(password))



if __name__ == "__main__":
    main()
