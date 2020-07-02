# What is Inheritance?
'''
Inheritance us used to indicate that one class will get the most or all of its features from a parent class.
i.e. Foo(Bar) --> "which says Make a class Foo that inherits from Bar"

Three ways on interaction:
1. Actions on the child imply an action on parent
2. Actions on the child override the action on the parent
3. Actions on the child alter the action on the parent
'''
'''

# Implicit inheritance

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# Override Explicitly

class Parent1(object):

    def override(self):
        print("PARENT override()")


class Child1(Parent1):

    def override(self):
        print("CHILD override()")

dad = Parent1()
son = Child1()

dad.override()
son.override()

# Alter Before or After

class Parent2():

    def altered(self):
        print("PARENT altered()")


class Child2(Parent2):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child2, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent2()
son = Child2()

dad.altered()
son.altered()
'''
# All Three Combined
'''

class Parent:

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

'''
'''
PYTHON FOR MULTIPLE INHERITANCE USING SUPER()
'''

# Python with single Inheritance


class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()

# Python Super() with Multiple Inheritance


class Animal:
    def __init__(self, animalName):
        print(animalName, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super().__init__(NonWingedMammalName)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')

