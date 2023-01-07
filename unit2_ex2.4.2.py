# exercise 2.4.2 from unit 2
'''
Exercise 2.4.2
Define a class called BigThing which receives as a parameter during creation a variable of a certain type (can be anything: string, list, number, etc.).

Add a method called size to the class that works as follows:

If the variable is a number - the method returns the number
If the variable is a list/dictionary/string - the method returns the length of the variable (len).
Below is a sample run:

my_thing = BigThing("balloon")
print(my_thing.size())
7

Define another class called BigCat which inherits from the BigThing class and also receives a weight during creation:

If the weight is greater than 15, the size method will return "Fat"
If the weight is greater than 20, the size method will return "Very Fat"
Otherwise, the method returns OK.
Below is a sample run:

cutie = BigCat("mitzy", 22)
print(cutie.size())
Very Fat

'''

# 1:
class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if isinstance(self._thing, (int, float)):
            return self._thing
        elif isinstance(self._thing, (list, dict, str)):
            return len(self._thing)

# 2:
class BigCat(BigThing):
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
        super().__init__(self._name)

    def size(self):
        if self._weight > 15 and self._weight <= 20:
            return "Fat"
        elif self._weight > 20:
            return "Very Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloofgggn")
    print(my_thing.size())
    my_thing = BigThing([1, 2, 3, 4, 5])
    print(my_thing.size())

    my_thing = BigThing(42)
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
