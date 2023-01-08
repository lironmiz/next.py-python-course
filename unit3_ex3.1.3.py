# exercise 3.1.3 from unit 3
'''
In this unit we learned about the hierarchy tree of exceptions. Now we will
consciously try to write code that will throw exceptions of various types.

Write eight functions, each of which will throw a different exception,
from the following exceptions:

StopIteration
ZeroDivisionError
AssertionError
ImportError
KeyError
SyntaxError
IndentationError
TypeError
Call each of the functions you wrote and check that the expected exception was indeed thrown.
'''

def function_1():
    # StopIteration
    raise StopIteration

def function_2():
    # ZeroDivisionError
    1 / 0

def function_3():
    # AssertionError
    assert False, "AssertionError"

def function_4():
    # ImportError
    import invalid_module

def function_5():
    # KeyError
    d = {}
    d['invalid_key']

def function_6():
    # SyntaxError
    eval('invalid syntax')

def function_7():
    # IndentationError
    if True:
    print('IndentationError')

def function_8():
    # TypeError
    1 + 'string'

def test_exceptions():
    try:
        function_1()
    except StopIteration:
        print("StopIteration was thrown")

    try:
        function_2()
    except ZeroDivisionError:
        print("ZeroDivisionError was thrown")

    try:
        function_3()
    except AssertionError:
        print("AssertionError was thrown")

    try:
        function_4()
    except ImportError:
        print("ImportError was thrown")

    try:
        function_5()
    except KeyError:
        print("KeyError was thrown")

    try:
        function_6()
    except SyntaxError:
        print("SyntaxError was thrown")

    try:
        function_7()
    except IndentationError:
        print("IndentationError was thrown")

    try:
        function_8()
    except TypeError:
        print("TypeError was thrown")

test_exceptions()

