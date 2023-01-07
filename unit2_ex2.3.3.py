# exercise 2.2.3 from unit 2
'''
Hide the animal's name and age attributes (reminder: _).
Allow the animal name to be determined during instance creation.
If no name was set for the animal during the creation of the instance,
 make sure to initialize its name with the default value "Octavio".
Write a method called set_name that allows you to change the name of the
 animal.
It actually has a method called get_name that returns the name of the animal.
Create a variable called count_animals designed to count how many animals
 were created from the class. Think: what type of variable is this, and where
  in the code should the counting operation be placed?
Write a main program in which you create two animal shows
(one with a name of your choice, the other without).
Print the name of each of the instances - check that for one of them the name
you gave was printed and for the other the default value Octavio was printed.
Change the name of one of the instances and print its new name after the
 change using the get_name method.
Print the variable count_animals and check that the value 2 is indeed
obtained (because only two animals were created from the class).
'''


class Cat:
    count_cat = 0
    def __init__(self, name=None):
        if name is None:
            self._name = "Octavio"
        else:
            self._name = name
        self._age = None
        Cat.count_cat += 1


    def get_age(self):
        return self.age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

def main():

    cat1 = Cat('cat1')
    cat2 = Cat()

    print(cat1.get_name())
    print(cat2.get_name())
    cat1.set_name('liron')
    print(cat1.get_name())
    print(cat1.count_cat)

if __name__ == '__main__':
    main()
