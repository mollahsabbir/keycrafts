class Person():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fun(self):
        print('Hello World')


p = Person(1, 2)

p.fun()