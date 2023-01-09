# exercise 6.2.5 from unit 6
'''
Create a class called "GreetingCard" that includes a method that initializes attributes with default values. Below is the breakdown:

attribute default value
_recipient Dana Ev
_sender Eyal Ch
Added a method named greeting_msg to the class that prints to the screen a message indicating the name of the sender and the name of the recipient.
When finished, save the Python file you wrote as file1.py.

Create a new Python file named file2.py. Import the "GreetingCard" class into it.
Inside the file, create a class called BirthdayCard that inherits from the GreetingCard class. Add the following attribute to the class:

attribute default value
_sender_age 0
We have updated the greeting_msg method so that in addition to the name of the recipient and the name of the sender, the greeting "Happy birthday" and the age of the sender will be printed.

Create another Python file called main.py. Create in it one instance of the BirthdayCard class and one instance of the GreetingCard class. Call the greeting_msg method on each instance.
'''

# first file 
class GreetingCard:
   """A class representing a greeting card.

    Attributes:
        _recipient (str): The recipient of the greeting card.
        _sender (str): The sender of the greeting card.
    """
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch'):
       """Initializes a GreetingCard object.

        Args:
            recipient (str): The recipient of the greeting card.
            sender (str): The sender of the greeting card.
        """
        
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
       """Prints the greeting message."""
        print(f'Recipient: {self._recipient} , Sender: {self._sender}')
        
# second file 
import file1 as f

class BirthdayCard(f.GreetingCard):
   """A class representing a birthday card, which is a type of greeting card.

    Attributes:
        _sender_age (int): The age of the sender of the birthday card.
    """
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch', sender_age=0):
        """Initializes a BirthdayCard object.

        Args:
            recipient (str): The recipient of the birthday card.
            sender (str): The sender of the birthday card.
            sender_age (int): The age of the sender of the birthday card.
        """
        
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
       """Prints the greeting message for a birthday card."""
        
        super().greeting_msg()
        print('Happy birthday!')
        print(f'Sender age: {self._sender_age}')
        
# main file 
import file1 as f1
import file2 as f2


def main():
    b = f2.BirthdayCard(sender_age=10)
    b.greeting_msg()

    g = f1.GreetingCard()
    g.greeting_msg()


if __name__ == "__main__":
    main()
