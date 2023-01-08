# exercise 4.3.2 from unit 4
'''
What will be the output of the code snippet?
'''
def f(x):
    yield x + 1
    print("test")
    yield x + 2
g = f(9)

# Answer: nothing
