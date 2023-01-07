# exercise 2.4.1 from unit 2
'''
What will be the output of the following code snippet?
'''

class A:
    def one(self):
        return self.two()
    def two(self):
        print('A')
class B(A):
    def two(self):
        print('B')
def main():
    my_object = B()
    my_object.two()
main()

# Answer: B
