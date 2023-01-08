# exercise 3.3.2 from unit 3
'''
Ido's birthday is coming up, and in honor of the occasion he wants to invite his friends to the birthday. Ido is interested in inviting only the people who are 18 years old or older. For this purpose, implement the following function.

def send_invitation(name, age):
    if int(age) < 18:
        print("under age")
    otherwise:
        print("You should send an invite to " + name)
The function send_invitations accepts two parameters: name and age. If the age is less than 18, it prints an appropriate message on the screen.

Actually a custom exception called UnderAge.
Right in the exception class the __str__ method. The method will return a string that tells the user that their age is less than 18. Add the present age of the invitee to the string, and in a few years he will be able to reach Ido's birthday.
Throw away the exception you created in the code - for this purpose, replace code line number 3.
Catch the exception in the code when it is thrown.
To test, run the function with arguments 17 and 20.
'''

class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Your age is less than 18. You are currently {str( self.age)} years old. In a {str(18 - self.age)} you will be able to join Ido's birthday celebration."


def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)


try:
    send_invitation("John", 17)
    send_invitation("Anna", 20)
except UnderAge as e:
    print(e)
