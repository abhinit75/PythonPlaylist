def phone_numbers(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 647-741-0309 tomorrow. 647-217-0768'
for i in range(len(message)):
    chunk = message[i:i+12]
    if phone_numbers(chunk):
        print(f"The phone numbers are: {chunk}")
