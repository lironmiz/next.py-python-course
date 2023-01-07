# exercise 2.3.1 from unit 2
'''
What will be the output of the following code snippet?
'''

class Sales:
    def __init__(self, money):
        self.money = money
        money = 100
val = Sales(123)
print(val.money)

# Answer: 123 
