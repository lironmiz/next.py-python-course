# exercise 2.3.2 from unit 2
'''
What will be the output of the following code snippet?
'''

class test:
    def __init__(self, a="hello world"):
        self._a = a
    def display(self):
        print(self._a)
obj = test()
obj.display()

# Answer: hello world 
