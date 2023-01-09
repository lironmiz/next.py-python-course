class LengthError(Exception):
    """
    A class used to represents an LengthError exception.
    """

    def __init__(self, arg):
        self._arg = arg
        super().__init__(arg)

    def __str__(self):
        return f'id number need to be equal to 9. your id length is: {len(self._arg)}'


class IDIterator:
    """
     A class used to represents an iterator named IDIterator.
    Args:
        id: The starting ID number defaults to 100000000.
    """

    def __init__(self, id=100000000):
        """Initialize the class with the given attribute."""
        check_id_valid(id)
        self._id = int(id)

    def __iter__(self):
        """
        Return the iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next valid ID number

        Raises:
            StopIteration: If the end of the range has been reached.
        """
        # raise stop iteration when id is max id valid number
        if self._id >= 999999999:
            raise StopIteration()
        is_valid = False
        # if id is valid, return the id else try the next id
        while not is_valid:
            self._id += 1
            is_valid = check_id_valid(self._id)

        return self._id


def help_is_valid(id_number):
    """
     Perform id validation operations on the elements of the provided id number and return the resulting list of integers.

    :param id_number
    :type id_number: str
    :return: return list of integer
    :rtype: list
    """
    digits = []
    for i, digit in enumerate(id_number):
        # even index position multiply by 1
        if i % 2 == 0:
            result = int(digit) * 1
        # odd index position multiply by 2
        else:
            result = int(digit) * 2

        # if value is greater that 9 add the sum of their digits
        if result >= 10:
            result = int(str(result)[0]) + int(str(result)[1])
        # add result to the digits list
        digits.append(result)
    # return digits list
    return digits


def check_id_valid(id_number):
    """
    The function checks if the ID received as a parameter is valid or invalid
    :param id_number
    :type id_number: str or int
    :return: return true if the id is valid else false
    :rtype: bool
    :raise: TypeError: raises an Exception
    """
    # Check if the input type is correct
    if not isinstance(id_number, (str, int)):
        raise TypeError("you must enter a string or int")
    elif not str(id_number).isdigit():
        raise TypeError("you Inserting a string that does not all contain numbera")

    # Convert the parameter to a string
    id_number = str(id_number)
    # Check if the length of the string is correct, i.e. exactly 9 digits
    if len(id_number) != 9:
        raise LengthError(id_number)

    numbers = help_is_valid(id_number)

    # Return True if the sum of the numbers in the list is divisible by 10, False otherwise."
    return sum(numbers) % 10 == 0


def id_generator(id_number):
    """
    generator function which returns valid ids numbers

    :param id_number
    :type id_number: str or int
    :return: return true if the id is valid else false
    :rtype: bool
    """
    # make sure the id is valid
    check_id_valid(id_number)

    # make sure the type is an integer
    id = int(id_number)
    # stop iteration when id is greater then 999999999
    while id <= 999999999:
        # increment id
        id += 1
        # validate id
        valid = check_id_valid(id)
        # if valid, yield id
        # if not valid continue to another while loop
        if valid:
            yield id


def main():
    # take user input
    id = input("Enter ID: ")
    if input("Generator or Iterator? (gen/it)? ") == "it":
        # create an iter from IDIterator class
        valid_id_iter = iter(IDIterator(id))
        # print 10 valid id numbers
        for _ in range(0, 10):
            print(next(valid_id_iter))
    else:
        # create an id generator instance
        id_gen = id_generator(id)
        for _ in range(0, 10):
            print(next(id_gen))


if __name__ == "__main__":
    main()
