import re


def number(n):
    return re.findall(r'\+*7[\s(]*\d{3}\)*\s*\d{3}(?:[\s-]*\d\d){2}', n)


print(number('+7 499 456-45-78'))
print(number('+74994564578'))
print(number('7 (499) 456 45 78'))
print(number('7 (499) 456-45-78'))