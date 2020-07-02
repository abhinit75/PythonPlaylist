'''
Classes:
- are like modules i.e mini-module
- Objects are similar to "import" statement
- Concept: Instantiate --> "create"
    - instantiating a class gets you a object


class MyStuff(object):

    def _init_(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")

'''
'''

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy Birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

'''
'''
class variable vs instace vraible
- the class variable is used for comonly throught class
- instance variable is specific to each instance of object

'''


class Employee(object):
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return f"{self.first}" + " " + f"{self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


emp_1 = Employee("Abhinit", "Patil", 120000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


# Learning to speak object-oriented

# Super function


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


square = Square.area(4)
square.area()