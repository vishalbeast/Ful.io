import re

def isValid(number):
    #pattern = re.compile('(0|212)?[-\s]?[4-9]\d{6}')
    pattern = re.compile(r"\+?[\d]{3}-[\d]{3}-[\d]{4}")

    return pattern.match(num)

num = ('212-456-7890')
if isValid(num):
    print('Valid phone number')
else:
    print('invalid mobile number')
    
