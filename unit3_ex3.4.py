# exercise 3.4 from unit 3
'''
Ido maintains a baking blog online for food lovers. Every surfer who wants to connect to the blog is obliged to choose a username and password as follows.

Username:

Must consist of the following legal characters: English letters, numbers and an underscore.
It must be between 3 and 16 characters long.
The password:

Must consist of at least 8 characters, and up to a maximum of 40 characters in length.
Must contain at least one of the following mandatory characters: one uppercase English letter, one lowercase English letter,
 one number and one special sign such as an exclamation mark (to perform the task you can use string.punctuation).
You must help Ido write a code that checks whether the username and password entered by surfers meet the conditions.

Write a function called check_input defined as follows:

def check_input(username, password):

The function accepts two parameters of type string: username and password. The function prints "OK" to the screen if the username and
 password are correct (that is, meet the conditions presented earlier).

If the username or password (or both) do not meet the defined conditions we would like to throw a detailed exception describing what
 went wrong. For this purpose, fulfill the following exceptions:

Exception named UsernameContainsIllegalCharacter - describes a username that contains illegal characters.
Exception named UsernameTooShort - describes a username consisting of less than 3 characters.
Exception named UsernameTooLong - describes a username consisting of more than 16 characters.
An exception named PasswordMissingCharacter - describes a password that does not contain at least one of the mandatory characters.
Exception named PasswordTooShort - describes a password consisting of less than 8 characters.
Exception named PasswordTooLong - describes a password consisting of more than 40 characters.
Please note: each exception is implemented in a separate class that inherits from the Exception superclass.

We have updated the code of the check_input function so that in a situation where it receives as input an invalid username or password,
 an appropriate exception will be thrown.

If everything is correct, the function will print OK as usual.

For your convenience, we have compiled for you inputs with which you can test the code you wrote.

check_input("1", "2")
check_input("0123456789ABCDEFG", "2")
check_input("A_a1.", "12345678")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")
All inputs except the last one are incorrect. Make sure that for each of the inputs one exception is thrown that describes
 the problem with it. The order of priority of the thrown exception is determined according to the order of the clauses in the question.

Write a main main function that receives the user's username and password for the blog. Incorporate in the main function block a call
 to the check_input function to check whether the input meets the conditions.

If the input is not correct, ensure that a detailed message describing the problem with the input is printed to the user. Then ask
 for more input until you get proper input.

Below is a sample run:

To view an accessible code snippet
check_input("1", "2")
check_input("0123456789ABCDEFG", "2")
check_input("A_a1.", "12345678")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")

Improved the UsernameContainsIllegalCharacter and PasswordMissingCharacter exceptions to contain a more accurate description of the problem.

So far the UsernameContainsIllegalCharacter exception class has printed a generic message:

The username contains an illegal character

Now, add a description of the illegal character and its position in the string to the UsernameContainsIllegalCharacter class.

Below is a sample run:

To view an accessible code snippet
check_input("A_a1.", "12345678")
So far the PasswordMissingCharacter exception class has printed a generic message:

The password is missing a character

Now, create 4 subclasses that inherit from the PasswordMissingCharacter class, where each class will describe a missing character in the password.

Note, the classes must extend the use of the __str__ method of the superclass, so that when printing it will only add in parentheses additional
 detail about the missing character. That is, it must use the method of the superclass and add to it.

Here are additions for certain characters:

check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
The password is missing a character (Uppercase)
The password is missing a character (Lowercase)
The password is missing a character (Digit)
The password is missing a character (Special)
'''

import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, illegal_char, index):
        self.username = username
        self.illegal_char = illegal_char
        self.index = index

    def __str__(self):
        return f"The username '{self.username}' contains the illegal character '{self.illegal_char}' at index {self.index}."
class UsernameTooShort(Exception):
    def __str__(self):
        return "Username is too short. It must be at least 3 characters long."

class UsernameTooLong(Exception):
    def __str__(self):
        return "Username is too long. It must be at most 16 characters long."


class PasswordMissingCharacter(Exception):
    def __init__(self, password, missing_char):
        self.password = password
        self.missing_char = missing_char

    def __str__(self):
        return f"The password '{self.password}' is missing the required character '{self.missing_char}'."
class PasswordTooShort(Exception):
    def __str__(self):
        return "Password is too short. It must be at least 8 characters long."

class PasswordTooLong(Exception):
    def __str__(self):
        return "Password is too long. It must be at most 40 characters long."

def check_input(username, password):
    if any(c.isalpha() for c in username):
        raise UsernameContainsIllegalCharacter(username, c, username.index(c))

    if not any(c.isdigit() for c in password):
        raise PasswordMissingCharacter(password, 'a digit')
    elif len(username) < 3:
        raise UsernameTooShort
    elif len(username) > 16:
        raise UsernameTooLong
    elif not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password) or not any(c in string.punctuation for c in password):
        raise PasswordMissingCharacter
    elif len(password) < 8:
        raise PasswordTooShort
    elif len(password) > 40:
        raise PasswordTooLong
    else:
        print("OK")

def main():
    while True:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)

main()
