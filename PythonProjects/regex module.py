import re
import re
'''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # r' = passing raw strings to re.compile

mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
'''
'''
Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a
raw string.)
3. Pass the string you want to search into the Regex object’s search() method.
This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual
matched text.
'''

phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex1.search('My number is 647-741-0309')
# print('area code found: ' + mo2.group(1))

areaCode, number = mo2.groups()
print(areaCode, number)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

# matching multiple groups with Pipe ( | )


#  Pipe ( | ) can be used to match one of many experessions

heroRegex = re.compile(r'Batman | Spiderman')
mo1 = heroRegex.search("Is Spiderman better or Batman")
print(mo1)

# Matching multiple groups with Pipe
batRegex = re.compile(r'Bat(Man|mobile|Copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1), mo.group(1))

# Matching optional Words

aRegex = re.compile(r'Bat(wo)?man')
x = aRegex.search("Batman is sickk")
print(x.group())

y = aRegex.search("Batwoman is a great fighter")
print(y.group())

# Matching Zero or More with the Star

bRegex = re.compile(r'Bat(wo)*man')
z = bRegex.search("The Batwowowowoman")
print(z.group())

# Matching one or More with the plus
''' The regex Bat(wo)+man will not match the string 'The Adventures of Batman' 
because at least one wo is required by the plus sign.
'''
cRegex = re.compile(r'Bat(wo)+man')
mo3 = cRegex.search('The Adventures of Batman')
print(mo3 is None)

# Matching Specific Repetions with Curly Braces
haRegex = re.compile(r'(Ha){3}')  # it only matches the number specified
match = haRegex.search("HaHaHa")
print(match.group())

# Greedy and Non-greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
ghd = greedyHaRegex.search("HaHaHaHaHa")
print(ghd.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
nghd = nongreedyHaRegex.search("HaHaHaHaHa")
print(nghd.group())

# The findall() method
# returns a list of strung but not a match object
''' 
1. When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() 
returns a list of string matches, such as ['415-555- 9999', '212-555-0000'].
2. When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\ d\d\d), the method findall() 
returns a list of tuples of strings (one string for each group), such as [('415', '555', '1122'), ('212', '555', '0000')].

'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
print(phoneNumRegex.findall('Cell: 647-741-0309 Work: 647-217-0768'))

gphoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(gphoneNumRegex.findall('Cell: 647-741-0309 Work: 647-217-0768'))

'''
Table 7-1: Shorthand Codes for Common Character Classes
    Shorthand character class
\d \D \w
\W \s \S
Represents
\d --> Any numeric digit from 0 to 9.
\D --> Any character that is not a numeric digit from 0 to 9.
\w --> Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W --> Any character that is not a letter, numeric digit, or the underscore character.
\s --> Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S --> Any character that is not a space, tab, or newline.
'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#  In this example, \d+ is one or more numeric digits, \s is followed by a whitespace character, \w+

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

x = 'RoboCop eats baby food. BABY FOOD.'

# can be used to remove characters or letters from a string
for vowel in vowelRegex.findall(x):
    x = x.replace(vowel, '')
print(x)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# Caret and Dollar Sign Characters
beginswITHhELLO = re.compile(r'^Hello')
print(beginswITHhELLO.search('Hello world!'))
print(beginswITHhELLO.search('He said Hello'))

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 75'))
print(endsWithNumber.search('Your number is Seventy Five'))

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890'))  # The last example shows that if ^ & $ are used then entire strinf
# must match regex
# Carrots cost dollars

# The wildcard character (. or dot)
atRegex = re.compile(r'.at')  # --> can be used to find rhyming words
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Matching everything with Dot-Star
# default uses greedy method --> matches as much text as possible
userInputF = input("First Name:")
userInputL = input("Last Name: ")
line = f'First Name: {userInputF} Last Name: {userInputL}'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
bo = nameRegex.search(line)

print(bo.group(1), bo.group(2))

nonGreedyRegex = re.compile(r'<.*?>')
go = nonGreedyRegex.search('<to serve man> for dinner.>')
print(go.group())

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newLineRegex = re.compile('.*', re.DOTALL)
print(newLineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

# Case-insensitive matching

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine and all cop'))

# Substituting Strings with the sub Method()

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double  agent'))

# Managing Complex Regexes

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
)''', re.VERBOSE)

# Combining re.DOTALL, re.Verbose, re.I

someRegexValue = re.compile(r'fod', re.IGNORECASE | re.DOTALL | re.VERBOSE)
