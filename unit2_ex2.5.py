# exercise 2.5 from unit 2
'''
Welcome to the "Hayton" Zoo! It is a virtual zoo where there are animals of different kinds - and it is realized entirely in the Python language.

Let's start by creating a basic class to represent an animal:
Write a class called Animal with the attributes: animal name (name_) and degree of hunger (hunger_).
Added an initialization method to the Animal class that will be used to set initial values ​​for the animal's attributes. The default value for the attribute degree of hunger (hunger_) is 0. The attribute animal name (name_) has no default value.
There are different types of animals in the zoo:
type
Dog
Cat
Skunk
Unicorn
Dragon
Write subclasses representing the types of animals in the type column (one for each type). On the subclasses to the network from the Animal superclass that you implemented in the previous section.
Instructions: If you have written a class that does not yet have code, you can add the pass command to its block.

Implement the following instance methods:

A get_name method that returns the name of the animal (name_).
is_hungry method that returns a Boolean value describing whether the animal is hungry or not (a hungry animal is an animal whose hunger degree value is greater than zero).
A feed method that subtracts one "point" from the degree of hunger (hunger_) of the animal.
Instructions: Think about where you should implement these methods - in the subclasses, or in the superclass.

We've created classes that represent animals, and now it's time to use them to create animal instances!
Here is a table describing the animals you have to create, with certain values ​​for the name (name_) and degree of hunger (hunger_) attributes.

hunger_ name_ Type
10 Brownie Dog
3 Zelda Cat
0 Stinky Skunk
7 Keith Unicorn
1450 Lizzy Dragon
For example: you need to create a dragon type animal called "Lizzy" and its hunger level is 1450.

Write a main function called main that performs the following tasks:

Creates one animal of each type (Unicorn, Skunk, Cat, Dog and Dragon) and initializes it with the values ​​shown in the table. She saves the instances of the animals in a list called zoo_lst.
Go through the animals in the zoo_lst list using a for loop. For each hungry animal, print its type (type, the name of the subclass) and its name (name_) and then feed it until it is no longer hungry (that is, until its degree of hunger is 0).
Instructions: You can use the following code skeleton.

for animals in zoo_lst:
     while animal.is_hungry():
        animal.feed()
Below is an example of a possible output:

Dog Brownie
Cat Zelda
Unicorn Keith
Dragon Lizzy
Every animal can talk. Here is a table describing a type of animal, and what it knows how to say.

talk Type
woof woof Dog
Meow Cat
tsssss Skunk
Good day, darling Unicorn
Raaaawr Dragon
Added a method named talk to the Animal class.
Implement the talk method in each of the subclasses that represent types of animals. The method must print to the screen the words that the animal knows how to say.
In the main program, after the feeding phase, add a call to the talk method for all the animals.
Instructions: Use the polymorphism mechanism to perform the task.

Below is an example of a possible output:

Dog Brownie
woof woof
Cat Zelda
meow
tssssss
Unicorn Keith
Good morning, darling
Dragon Lizzy
Raaaawr

Each of the animals has a method that is unique only to it and it prints a certain caption to the screen. Here is a table describing for each type of animal the name of its unique method, and what it prints to the screen.
For example: an animal of type "skunk" has a unique method called "stink" that prints "Dear lord!"

print special method Type
There you go, sir! fetch_stick Dog
Meeeeow chase_laser Cat
Dear Lord! stink Skunk
I'm not your toy... sing Unicorn
$@#$#@$ breath_fire Dragon
Add to each subclass its unique method.
In the main program, after calling the talk method for each animal, call the unique method for the animal, depending on its type.
Below is an example of a possible output:

Dog Brownie
woof woof
There you go, sir!
Cat Zelda
meow
Meeeow
tssssss
Dear Lord!
Unicorn Keith
Good morning, darling
I'm not your toy...
Dragon Lizzy
Raaaawr
$@#$#@$

There are two types of animals that have an additional feature (in addition to the name and degree of hunger). Each attribute has a default value:

default value attribute Type
6 _stink_count Skunk
"Green" _color Dragon
For example, an animal of type Dragon has an attribute named color_ which is initialized to the default value "Green".

Add the specific attributes to the subclasses and initialize them with the default values in the table.

New animals joined the zoo, one of each type. Below is a table describing the values of their attributes: name (name_) and degree of hunger (hunger_).

_hunger _name Type
80 Doggo Dog
80 Kitty Cat
80 Stinky Jr. Skunk
80 Clair Unicorn
80 McFly Dragon
In the main program, create a new animal of each type (according to the table). Updated the zoo_lst list definition to also include these animal instances as members (in addition to the ones it already has).
Run the program as usual, so that the operations in the loop will also be performed on the new animals.
Add to the Animal class an attribute describing the name of the zoo (zoo_name) and initialize it with the value "Hayaton". This property has a single and fixed value and must be shared by all animals created from the Animal class. Print this attribute once at the end of the program.
Directions: Think about what type of feature you need to set.
'''


class Animal:
    """
    A class representing an animal.

    Attributes:
        name (str): The name of the animal.
        hunger (int): The degree of hunger of the animal, with 0 being not hungry and higher values indicating greater hunger.
    """

    def __init__(self, name, hunger=0):
        """
        Initializes the animal with a name and a degree of hunger.

        Args:
            name (str): The name of the animal.
            hunger (int): The degree of hunger of the animal, with 0 being not hungry and higher values indicating greater hunger.
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        Returns the name of the animal.

        Returns:
            str: The name of the animal.
        """
        return self._name

    def is_hungry(self):
        """
        Returns whether the animal is hungry or not.

        Returns:
            bool: True if the animal is hungry, False otherwise.
        """
        return self._hunger > 0

    def feed(self):
        """
        Decreases the degree of hunger of the animal by 1.
        """
        self._hunger -= 1

    def talk(self):
        pass

class Dog(Animal):
    """
       A class representing an Dog.
    """
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    """
         A class representing an Cat.
    """
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    """
        A class representing an Skunk.
    """
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._stink_count = 6
    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    """
        A class representing an Unicorn.
    """
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    """
        A class representing an Dragon.
    """
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._color = "Green"
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)

    # Add the zoo list
    zoo_lst = [brownie, zelda, stinky, keith, lizzy]

    # Feed animal
    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
            print(f"Feeding {animal.get_name()} ({type(animal).__name__})")

    # Create new animals
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_jr = Skunk("Stinky Jr.", 80)
    Clair = Unicorn("Clair", 80)
    mcFly = Dragon("McFly", 80)

    zoo_lst.append(doggo)
    zoo_lst.append(kitty)
    zoo_lst.append(stinky_jr)
    zoo_lst.append(Clair)
    zoo_lst.append(mcFly)

if __name__ == '__main__':
    main()
