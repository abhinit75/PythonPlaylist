import os
from pathlib import Path

# covert a string into a path
# os.path.join('usr', 'bin', 'spam'))
# abs
'''
Useful commands:
1. os.getcwd
2. os.chdir(enter path)
3. os.mkdir() or os.makedir()

Handling Absolute and Relative Paths
- os.path.abspath(path) --> returns  a string of absolute path (covert relative to absolute)
- os.path.isabs(path) --> returns True is path is absolute
- os.path.relpath(path, start) --> path from start to file 
- os.p;ath.dirname(path)
- os.path.basename(path)
- os.path.split()
- os.path.getsize
# Checking Path validity
- os.path.exists(path)
- os.path.isfile(path)
- os.path.isdir(path)

'''
'''
print(os.path.abspath('.'))
print(os.path.abspath('./Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.getcwd())
'''
'''
sonnetFile = open('sonnet29.txt')
print(sonnetFile.read())
'''
'''
path = Path('/Users/abhi/Desktop/Projectfiles/Sonnet29.txt')
with open(path, mode='a') as f:
    f.write("this is a line.\nThis is a second line.\nThis is the third line.")

path2 = Path('/Users/abhi/Desktop/Projectfiles/Sonnet29.txt')
r = path2.open()
print(r.read())
'''
'''
creating a new file"
path = Path('mytextfile.txt)
path.touch()

path.write_text('This is myfile.txt')
'''
'''
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month

name = input('Enter article name:')

path1 = Path('articles') / str(year) / str(month)
path1.mkdir(parents=True)

path2 = path1 /  f'{name}.txt'

path2.touch()

print(f'Article created at: {path2}')
'''

'''
Saving Variables with the Shelve Module:\
- have key value pairs like dictionaries

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])
'''
'''
from sys import argv


script, filename = argv, argv


print(f"We are going to erase {filename}.")
print("If you don't want that, hit CRTL-C (^C)).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we will close it")
target.close()
'''

''' copy from file to file

from sys import argv
from os.path import exists

script, from_file, to_file = argv, argv, argv

from_file = 'sonnet29.txt'
to_file = 'new_file.txt'

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print("Ready, hit RETURN to continue, CRTL-C to abort")
input()

out_file = open(to_file, 'w') # giving write access
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
'''
# we could do these two on one line, how?
# Code can be one line using ;
