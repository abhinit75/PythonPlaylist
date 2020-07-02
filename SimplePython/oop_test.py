import random
from urllib.request import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
'''
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip()), encoding="utf-8")


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            input("> ")
            print(f"ANSWER:  {answer}\n\n")

except EOFError:
    print("\nBye")
'''

'''
OOPS:
- structuring programs so that properties and behaviours are bundled into individual objects
- an object could represent a person with the name property, age, address etc.

Another common programming pardigm is procedural programming:
- which structures a program according to a "recipe" in that it provides steps, in the form of functions and code blocks
- sequencial programming

Classes in python:
- an object is an instance of some class
- blueprint for how something should work oir be defined, but does not provide real content itself
- "like an idea for something"

Python Objects (Instances)
- class = blueprint, instance = copy of the class with actual values
- literally an object belonging to a specific 

1. All classes create objects and all objects contain characteristics called attributes
2. reffered to asd properties in the opening paragraph
3. _init_() method to intialize

Class Attributes:
- While instance attributes are specific to object, class attributes are the same for all instances
- Instantiating Objects - fancy term for creating a new, unique instance of a class
'''


class Dog:
    # Class Attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        is_hungry = False

    def walk(self):
        return "{} is walking".format(self.dogs)


# Child class (inherits from Dog Class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

'''
# Child classes inherit attributes and
# behaviours as well
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviours as well
print(jim.run("slowly"))

# is Jim an instance of DOg
print(isinstance(jim, Dog))

# Is Julie an instance of Dog()
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is Johnny Walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# Is Julie and instance of jim
print(isinstance(julie, jim))

# instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))

# Instantiate the Dog Object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

# Is philo a mammal?
if philo.species == 'mammal':
    print("{} is a {}!".format(philo.name, mikey.age))

dog1 = Dog("Bob", 19)
dog2 = Dog("Alice", 22)
dog3 = Dog("Jack", 23)

'''
'''
def get_biggest_number():
    a = [dog1.age, dog2.age, dog3.age]
    age = 0
    for i in a:
        if i > age:
            age = i

    return age


print(get_biggest_number())
'''

'''
def get_big_number(*args):
    return max(args)


print("The oldest dog is {} years old".format(get_big_number(dog1.age, dog2.age, dog3.age)))


# Modifying Attributes
class Email:
    def __init__(self):
        self.is_sent = False

    def send_email(self):
        self.is_sent = True

my_email = Email()
print(my_email.is_sent)

my_email.send_email()
print(my_email.is_sent)
'''
'''
Inheritance
- process by which one class takes on the attributes and methods of another
- child classes derive properties from parent classes
'''


