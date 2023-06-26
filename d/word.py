# 1. задача

# s = 'I am learning Python. hello, WORLD!'
# first = s.find('h')
# last = s.rfind('h')
# print(s[:first] + s[last + 1:])
#2. задача

# s = 'I am learning Python. hello, WORLD!'
# first = s.find('h')
# last = s.rfind('h')
# w = s[first + 1: last]
# print(s[:first + 1] + w[::-1] + s[last:])

#3.задача

# h1 = input('Введите строку: ')
# h2 = input('Её заменяемая подстрока: ')
# h3 = input('Новая подстрока: ')
# print(h1.replace(h2, h3))

#4.задача

# s = '''Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели. '''
# a = ''
# lst = []
# for i in range(len(s)):
#      if s[i] == ' ' or s[i] == '\n':
#          lst.append(a)
#          a = ''
#          continue
#      else:
#          a += s[i]
# print(lst)
# count = 0
# for i in lst:
#      if i.find('е') == 0 or i.find('Е') == 0:
#          count += 1
# print('Количество слов: ', count)