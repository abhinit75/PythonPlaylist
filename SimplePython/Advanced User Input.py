"""
Breaking up a sentence:

stuff = input('>')
words = stuff.split()

Lexicon Tuples:
- Break sentence into words
- make (Type, Word) Pairs

"""
num = int(input(">"))

a = 0
b = 1
c = 0
for i in range(num):
    print(c)
    c = a + b
    b = a
    a = c

