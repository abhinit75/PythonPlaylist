import re

capReg = re.compile(r'.*[A-Z].*')
lowerReg = re.compile(r'.*[a-z].*')
digitReg = re.compile(r'.*\d.*')


def checkPassword(text):
    if capReg.search(text) and lowerReg.search(text) and digitReg.search(text):
        return True
    else:
        return False


pw = 'kenIsgreat99'
print(checkPassword(pw))
