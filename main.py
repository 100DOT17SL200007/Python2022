# 05.12.22
# name_Name2 = "Ksenia"
# print("Hello,", name_Name2)
# age = 20
# print(type(age))
# print(id(age))
# age = "hello"
# print(type(age))
# a = b = c = 1
# print(a,b,c)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
# a ="5"
# b =2
# print(int(a)+b)
# a = 1
# b = 2
# print("a =", a)
# print("b =", b)
#  c = a
#  a = b
#  b = c
# b = b - a
# a = a + a
# a, b = b, a
# print("a =", a)
# print("b =", b)
# print("строка"
# "символов")
# print('строка \n   символов')
# print("\tДокумент    \"file.txt\" D:\\folder\\file.py")
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 5)
import sqlite3

#
# print(56576575675656346565465)
# print(5.68767868968685465747575)


# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(6 // 2)
# print(6 ** 2)
# print(6 ** 2)
# print(7 % 2)

# number = 6 + 4 * 5 **2 + 7
# print(number)
# number = (6 + 4) * 5 ** (2 + 7)
# print(number)
# a = 5
# b = 7
# c = 3
# sum = a + b + c
# um = a * b * c
# sqr = sum / 3
# print('Сумма:', sum)
# print('Произведение:', um)
# print('Среднее арифметическое:', sqr)
# num = 10
# num += 5  #num = num + 5
# print(num)
# num -= 3 #num = num - 3
# print(num)
# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 +c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num//= 10 #432
# res += num % 10 * 100
# num//= 10 #43
# res += num % 10 * 10
# num//= 10
# res += num % 10
# print(res)

#  07.12.22
# Функции явного преобразования типов
# str()
# int()
# float
# bool

# num1 = '2.5'
# num2 = 3
# res = int(float(num1)) + num2
# print(res)
#
# print(int(3.8))
# a = round(3.8)
# print(a)
# print(type(a))
# b = round(3.83465, 2)
# print(b)
# print(type(b))
# name = "Виктор"
# age = 28
# print("Меня зовут", name, ".Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне " + str(age) + "лет.")
# print("Меня зовут", name, ".Мне", age, "лет.", sep="--", end="")
# print("Я учу Python.")
# name = input("Ваше имя:")
# print(name)
# a = int(input("Число: "))
# b = int(input("Степень: "))
# a = int(a)
# b = int(b)
# st = a ** b
# print('Число', a, 'в степени', b, 'равно', st)
# b1 = True #1
# b2 = False #0
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))
# print(bool(" "))
# print(bool("4"))
# print(bool(0))
# print(bool(None))
#
# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(7 + 5 != 7)
# print( 8 < 7)
# print( 8 > 7)
# print( 8 <= 7)
# print( 8 >= 7)

# print(2 < 10 < 9) # True && False
# print(3 * 3 <= 7  >= 2) # False && True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 and 1 + 3 < 4)
# print(5 - 3 == 2 or 1 + 3 == 4)
# print(5 - 3 < 2 or 1 + 3 == 4)
#
# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

#
# day = int(input("Введите день недели (цифрой): "))
# if day >= 1 and day <= 5:
#     print("Рабочий день", end=" ")
# if day == 1:
#     print("понедельник")
# if day == 2:
#     print("вторник")
# if day == 3:
#     print("среда")
# if day == 4:
#     print("четверг")
# if day == 5:
#     print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день", end=" ")
# if day == 6:
#     print("суббота")
# if day == 7:
#     print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца:"))
# if month == 12 or month == 1 or month == 2:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:  # 5 <= n <= 9 or n == 0
#         print("ворон")
# else:
#     print("Ошибка ввода")
# password = "qwerty"
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print("Пароль не верен")

# a = int(input('Делимое: '))
# b = int(input('Делитель: '))
# print(a / b if b != 0 else "На ноль делить нельзя!")
# day = '11'
# time = 10
# match day:
#     case 'понедельник' | 'вторник' | 'среда'| 'четверг'| 'пятница' if 9 <= time <= 16:
#           print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#           print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# 12.12.22
# Исключения
#
# a = 5
# b = 0
# print(a / b)
# try:
#    n = int(input("Введите целое число: "))
#    print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

##try:
#    n = int(input("Введите делимое: "))
#    m = int(input("Введите делитель: "))
#    print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try: #попытаться
#    n = int(input("Введите делимое: "))
#    m = int(input("Введите делитель: "))
#    print(n / m)
#  except (ValueError, ZeroDivisionError) :     #исключения
#     print("Нельзя вводить строки и делить на ноль ")
# # else:  #когда в блоке try не возникло исключения
# #     print("Все нормально. Вы ввели числа", n, "и", m)
# # finally: #выполняется в любом случае
# #     print("Конец программы")
 #try:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#     print(int(a) + int(b))
# except(ValueError):
#      print(a + b)
#Циклы
# i = 0
# while i < 5:
#     print("i =", i)
# #     i += 1  #i = i + i
# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#         i += 1

# try:
#     x = int(input('Количество: '))
#     while x > 0:
#          print('*', end='')
#          x -= 1
# except ValueError:
#     print('Введите число!')

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конц диапазона: "))
# sum1 = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2 !=0:
#         sum1 += a
#     a += 1
# print(sum1)

 #n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
#
# i = 0
# while i < 10:
#     if i == 3:
#         i +=1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

#  i = 0
#  while True:
#      print(i)
#      if i == 5:
#          break
#      i += 1
#
# while True:
#    n = int(input("Введите положительное число: "))
#     if n < 0:
#             break
#             m = 1
# while True:
#      n = int(input('Число: '))
#         if n == 0:
#             break
#             m *= n
# print('Произведение равно:', m)

# i = 0
# while i < 10:
#     print(i)
#     i +=1
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, '\t', end = '')
#         j += 1
#     print('')
#     i += 1

 #n = int(input("Введите число от 1 до 99: "))
# kop = n
# if 11 <= kop <= 14:
#     print(n, "копеек")
# elif 0 <= n <= 10 or 15 <= n <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(n, "копейка")
#     elif 2 <= kop <= 4:
#         print(n, "копейки")
#     else:
#         print("копеек")
# else:
#     print("Ошибка ввода")
 #a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# print(a / b if b > 0 else "На ноль делить нельзя")



# 14.12.2022
# for  element in collection:
#  тело цикла

# for i in "Hello", "red", "blue", "yellow" , 20, 0.3:
#     print(i)

# print(range(5))
# # range(start, stop, step)
# for i in range(-8, 1):
#     print(i, end=" ")
# print()
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i % 10 == i // 10:
#        print (i, end=" ")
#
# for i in range(3):
#        print (i, end=" ")
#        if i == 1:
#            break
# else:
#     print('\done')

# for i in range(1, 4):
#     print("+++", i)
#     for j in range(1, 3):
#         print("----", j)

# a = int(input("Введите ширину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         print("*", end="")
#     print()

# a = int(input("Введите ширину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         if i == 0 or j == 0 or i == b - 1 or j == a - 1:
#             print('*', end=" ")
#         else:
#            print(" ", end=" ")
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# for i in "Hello":
#     print(i)
#
# num = [i for i in range(30)  if i % 2 == 0]
# print(num)

# Списки(list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums))
# print(id(nums[1]))
# print(nums[0])
# print(nums[-4])
#
# nums[5] = 2
# nums[1] += 100
# print(nums)
# print(id(nums[1]))
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
# c = list("Hello")
# print(c)
# s = [5] * 6
# print(s)
# a = [1,2,3]
# b = [4,5]
# c = a + b
# print(c)

# n = list(range(10))
# print(n)
# [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
# n = 5
# a = [i * 3 for i in "Hello"]
# print(a)
#a = [0] * int(input("Количество элементов в списке: "))
#print(a)
#for i in range(len(a)):
#   a[i] = int(input("->"))
#   print(a)

# a= [int(input("->")) for i in range(int(input("Количество элементов в списке: ")))]
# print(a)


# nums = [8, 9, 3, 5, 6]
# print(nums * 2)
# for i in range(len(nums)):
#     print(nums[i] * 2, end=" ")
# print()
# for i in nums:
#      print(i * 2, end=" ")

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# summa=0
# for i in a:
#     if i<0:
#         summa+=i
# print(summa)

# a = list(range(21,41))
# print(a)
# z = 0
# s = 0
# for i in a:
#     if i % 2==0:
#         s += 1
#     else:
#         z += i
# print('Четных: ',s,'Нечетных: ',z)


# a = [int(input('-->')) for i in range(int(input('n: ')))]
# n = sum1 = 0
# for i in a:
#     if i != 0:
#         n += 1
#         sum1 += i
# print("Среднее значение: ", sum1 / n)

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# print(a)
# for i in range(len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# список[start:stop:step](срез)
# a = [9,4,3,1,5,17]
# print(id(a))
# print(a[-1:0:-1])
# print(a[1:3:-1])
# print(id(a[10:20]))


#a= list(range(1,8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])


# 19.12.22
# a = list(range(1, 8))
# print(a)
# a[1:3] = [0,0,0,0]
# print(a)

# Методы списков
# print(dir(list))
# a = list(range(1, 8))
# print(a)
# a.append(99) #добавляет элемент в конец списка
# print(a)
# a.extend([22,11,9]) #добавляет множество элементов  вконец списка
# print(a)
# a.insert(20,100) #добавляет элемент в список. Первый параметр - индекс, второй - добавляемое значение
# print(a)
# a.extend('add')
# print(a)
# s = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = input("->")
#     s.append(x)
# print(s)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

#
# a = [5,9,2,1,4,3]
# b = [4,2,1,3,7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1,2,3, 2,4]
# b = [11,22,33]
# c=[]
# if len(b) > len(a):
#     a, b = b, a
#     for i in range(len(a)):
#          c.append(a[i])
#          c.append(b[i])
#     for i in range(len(a), len(b)):
#          c.append(a[i])
# print(c)

 #b = [11, 12, 13, 2, 4, 13]
# b.remove(13)  #удаляет элемент из списка по значению, если элементов с заданным значением несколько, то удаляется только первый
# print(b)
# a = 12
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(-1)  #с пустыми скобками - удаляет последний элемент из списка, с заданным индексом в скобках - удаление по индексу.
# print(b)

# b.clear()
# print(b) #очищает список
# s = []
#  n = int(input('Количество элементов списка: '))
#   for i in range(n):
#    k = int(input('Введите индекс:  '))
#     i = s.pop(k)
#          s.append(x)
#  print(s)
# #
# a = [int(input('-> ')) for num in ' ' * int(input('Count: '))]
# b = int(input('Index: '))
# a.pop(b)
# print(a)

#a = [9,2,7,2,4,2,3,2]
# num = a.count(2) #количество заданных значений в списке
# print(num)
# ind = a.index(2,2) #возвращает первый индекс искомого значения. Также можно указать значения start и end.
# print(ind)

# a = [9,2,7,2,4,2,3,2]
# b = a.copy()
# print("a", a)
# print("b", b)
# a = [9,2,7,2,4,2,3,2]
# print(a)
# a.reverse() #перестраивает элементы списка в обратном порядке.
# print(a)
# a.sort() #сортирует список, по умолчанию - по возрастанию, reverse=True - по убыванию.
# print(a)
# a.sort(reverse=True)
# print(a)
#
# b=["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)
# c = sorted(a)
# print(c)
# print(a)
#Генерация случайных данных
# import random
# print(random.random())
# print(random.randint(2,9)) #от 2 по 9 (включительно)
# print(random.randrange(2,9,2))
# from random import randrange, randint as ran
# from random import *
# import random as r
# # print(r.uniform(10.5, 25.5))
# # print(round(r.uniform(10.5, 25.5),3))
# city = ["Москва", "Геленджик", "Анапа", "Сочи", "Санкт-Петербург"]
# print(r.choice(city))
# print(r.choices(city, k=5))
# r.shuffle(city)
# print(city)

 # 21.12.22
# import random as r
#
# mas = [r.randint(-30,30) for i in range(10)]
# print(mas)

# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))
# print(max(sum))

# x = list('1253512467')
# print(x)
# print('a' in x)
# print('a' not in x)

# lst = []
# #if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# print(bool(lst()))

# from random import randint
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0,10) for i in range(n1)]
# b = [randint(0,10) for i in range(n2)]
# print("Первый список: ", a)
# print("Первый список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#          c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списокв: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)
# import random
# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)

# m = [
#     [1,2,3,4,9,5],
#     [5,6,7,8],
#     [9,10,11,12,5]
# ]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#         print()

# for row in m:
#     for x in row:
#           print((x, end="\t")
#      print()

# w,h=5,3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     for x in row:
#          print(x, end="\t")
#     print()
# print([[x for x in row] for row in matrix])

# for x, y in [[1,2], [3,4], [5,6], [7,8]]:
#     print(x, "+", y, "=", x + y)
# from random import  randint
# w,h = 3,4
# n = 1
# matrix = [[randint(-20,10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         if x != 0:
#            n *= x
#            print(x, end="\t")
#     print()
# print("Количество отрицательных чисел: ", n)

# w = h = 6
# n = 1
# matrix = [[randint(1,100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#       print(x, end="\t")
#     print()
# s = []
# # m = 101
# for i in range(w):
#     # s.append(matrix[i][i])
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(m)
# print(min(s))
# import  math as m
# from math import sqrt, ceil, floor, pi
#
# num1 = sqrt(2)
# num2 = sqrt(3.2)
# num3 = sqrt(3.8)
# print(num1)
# print(num2)
# print(num3)
# print(pi)
# from math import pi
# a = int(input("Введите радиус окружности: "))
# c = 2 * pi * a
# print("Длина окружности: ", round(c,2))

# 26.12.22

# import time
# import locale
#
#
# locale.setlocale(locale.LC_ALL, "ru")
# locale.setlocale(locale.LC_ALL, "de")
#
#
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mon)
#
# print(time.strftime("Today is %B"))
# print(time.strftime("Today is %B %d, %Y"))
# print("Сегодня:", time.strftime(":  %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()))

#pause = 5
# print("Progamm started...")
# time.sleep(pause)
# print(pause, "seconds")

#task = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(task)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")

#Функции
# a = 2
#
#
# def hello(name, word):
#      print("Hello,", name, ".Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#      # x = 1
#      print(w)
#      print(a + b)
#
# w = 8
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(2.5, 4.7)

# def symbol(count, a, b):
#      # print((a + b) * (count // 2) + a * (count % 2))
#      for i in range(count):
#           if i % 2 == 0:
#                print(a, end="")
#           else:
#                print(b, end="")
#      print()
#
# symbol(9, "+", "-")
# symbol(9, "X", "0")


#def get_sum(a, b):
#      return a + b
#      print("Сережа")
#
#
# x = 2
# y = 5
# w = get_sum(x,y)
# print(w * 2)

#def maximum(one, two):
#      if one > two:
#           return True
#      else:
#           return False
#
# if maximum(5, 13):
#      print("Первое число больше")
# else:
#      print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Этот пароль надежный")
# else:
#     print("Это ненадежный пароль")


# def cube(a):
#      return  a*a*a
#
#
# for i in range(1,11):
#      print(i, "в кубе =", cube(i))

# def change(lst):
#       # lst[0], lst[-1] = lst[-1], lst[0]
#       end = lst.pop()
#       start = lst.pop(0)
#       lst.insert(0, end)
#       lst.append(start)
#       return lst
#
#
# print(change([1,2,3]))
# print(change([9,12,33,54,105]))
# print(change(['с', 'л', 'о', 'н']))

# def get_sum(a,b,c=1,d=1):
#     return a + b + c + d
#
#
# print(get_sum(1,2,5,7))
# print(get_sum(1,2,5))
# print(get_sum(1,2))
# print(get_sum(1,2,d=5))

# def digits_sum(n, even= True):   #38271
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма четных цифр: ")
# print(digits_sum(987402, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# # display_info('Igor', age=23, name="Ira")


#28.12.22
# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# print(id(a))
# a = 6
# # print(a == b)
# # print(a is b)
#
# print(id(a))


# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))


# s = True
# print(id(s))
# s = True
# print(s)
# print(id(s))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# b = tuple([1, 2, 3, 4, 5])
# print(type(b))
# print(b)

# t = (2,)
# print(type(t))
# print(t)

# t = tuple("Hello")
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple(input('-> ') for i in range(3))
# print(s)

# s = input("-> ")
# print(tuple(s))
# from random import randint
#
#
# s = tuple(randint(1, 30) for i in range(20))
# print(s)


# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
#
# print(t3.count('l'))
# print(t3.count('a'))
#
# print(t3.index('l', 4))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if num not in tup:
#         return tuple()
#     first = tup.index(num)
#     if num not in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# # def tpl_sum(t1, t2):
# #     print(t1)
# #     print(t2)
# #     print(t1 + t2, (t1 + t2).count(0))
# #
# #
# # tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))
#
# def tpl_sum(a, b):
#     return tuple(randint(a, b) for _ in range(12))
#
#
# t1 = tpl_sum(0, 5)
# # t1 = tuple(randint(0, 5) for i in range(12))
# # tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))
# print(t1)
# t2 = tpl_sum(-5, 0)
# # t2 = tuple(randint(-5, 0) for j in range(12))
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3.count(0))


# point = (10, 20)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси Х и в координате 0 по оси Y")
#     case (0, y):
#         print("!!!Точка находится в координате 0 по оси Х и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси Х и в координате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")


# t = [2, 3]
# print("t =", id(t))
# print(id(t[0]))
# t[0] = 5
# print(t)
# print(id(t[0]))
# print("t =", id(t))
# a = 5
# print(id(a))


# t = (10, 11, [1, 2, 3], [4, 5, 6, 4, 7, 8, 9, 6, 6, 12], ['hello', 'world'])
# print("t =", t.__sizeof__())
# print(t, id(t))
# print(len(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))
# print(len(t))
# print("t =", t.__sizeof__())

# a = tuple(range(2))
# print(a)
# print(a.__sizeof__())
# b = tuple(range(1))
# print(b)
# print(b.__sizeof__())

# Распаковка кортежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# name1, age1, married1 = get_user()
# user = get_user()
# name1, age1, married1 = user
# print(name1, age1, married1)
# print(user[0])
# print(user[1])
# print(user[2])

# a = (1, 2)
# del a
# print(a)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)




# 09.01.2023
# list()
# tuple()
# set() - множество, неупорядоченный список уникальных данных.
# frozenset()
# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# c = ['red', 'green', 'green', 'blue']
# a = set(c)
# print(type(a))
# print(a)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(par):
#     return (set(par), len(set(par)))
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# c = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print('B' + i[1:])
#
#
# for i in r:
#     if i[0] == 'a':
#         if i[1] == 'c':
#             print("A" + i[1:])
#     else:
#         if i[1] == 'c':
#             print('B' + i[1:])


# s = {'banana', 'apple', 'orange'}
# print(s)
# # s.add(4)  # добавляет элемент во множество
# # if 44 in s:
# #     s.remove(44)  # удаляет элемент по значению
# # s.discard(44)  # удаляет элемент по значению без генерации исключения
# a = s.pop()  # удаление первого элемента
# s.clear()  # полная очистка множества
# print(s)
# print(a)

# Операции над множествами
# a = {0, 1, 2, 3, 4}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # a |= b
# # a &= b
# # c = b - a
# # a -= b
# # c = a ^ b
# # a ^= b
# c = a < b
# print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = 'Hello'
# s2 = "How are you"
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=" ")


# s1 = "Python"
# s2 = "Programming language"
# print(set(s1).difference(s2))
#
# s1 = 'Python'
# s2 = 'Programing language'
# print(set(s1) - set(s2))
#
# a = "Python"
# b = "Programming language"
# c = set(a) - set(b)
# for i in c:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
# drawing = drawing - both_hobby
# print(drawing)

#Словарь (dict)
# frozenset()

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({"hello", "world"})
# print(s1)


# Словарь (dict)

# a = [1, 2, 3]
# d = {1: 'one', 'two': 2, 'three': 3, 'four': 3}
# print(a[0])
# print(d[1])

# d = {'one': 1, 'two': 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))

# a = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna'),
# )
#
# b = dict(a)
# print(b)

# d = {i: 100 for i in range(2, 7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)


# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print("one1" in d)
# key = 'one1'
# if key in d:
#     del d[key]
# print(d["one1"])
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key, "-> ", d[key])

# a = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# s = 1
# for i in a:
#     s *= a[i]
# print(s)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {input("-> "): input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)


# a = [1,2,3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(a)
# print((d))

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# s = 1
# for key in d:
#     s *= d[key]
#     print(s)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# d = {i: input("->") for i in range(1,5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i35-4670K', 3, 8500],
#     '3': ['AMD FX-6300',6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1],"шт.по", goods[i][2], "руб.", sep="")
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input("Количество: "))
#         goods[n][1] = qty
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1],"шт.по", goods[i][2], "руб.", sep="")


# 11.01.23

# studs = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[sname] = point
#     s += point
#
# print(studs)
# avrg = s / n
# print(avrg)
# for i in studs:
#     if studs[i] > avrg:
#         print(i)

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['c'])
# value = d.get('f', False)  # получить значение по заданному ключи
# print(value)
# n = d.keys()  # список ключей
# print(n)
# n = d.values()  # список значений
# print(n)
# n = d.items()  # список кортежей ключ + значение
# print(n)
#
# for i, j in d.items():
#     print(i, "->", j)


# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()  # создание копии словаря
#
# print("D =", d)
# print("D2 =", d2)
#
# d['b'] = 5
# d2['e'] = 7
#
# print("D =", d)
# print("D2 =", d2)


# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')  # удаляет элемент из словаря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem()  # удаляет произвольную пару ключ + значение и возвращает их
# print(item)
# print(d)
# item = d.setdefault("f", 5)  # добавляет ключ со значением по умолчанию, если ключа не существует
# print(item)
# print(d)

# d.update({"a": 20, 'w': 10})  # обновление словаря
# print(d)
# d.update([('q', 7), ('t', 9)])
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'd': 4}
# # z = x.copy()
# # z.update(y)
# # z = y | x
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(d)
# print(new_d)
#
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4738, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3908, "S": 3645, "E": 8821, "W": 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
# w = {k: v for k, v in d.items()}
# print(w)
# for i, j in d.items():
#     if len(d) <= 2:
#         print(i, ":", j)

# d = {'a': 1, 'b': 2, 'c': 3}
# count = 0
# for i in d:
#     print(i, ':', d[i])
#     count += 1
#     if count == 2:
#         break

# value = int(input("-> "))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value = list(d.keys())
# print(value)
# value = list(d.values())
# print(value)
# value = list(d.items())
# print(value)


# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = [#         ]  # d['two'] = []
#         s = i  # s = 'two'
#     else:
#         d[s].append(i)  # d['two'] = [10, 20]
#
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = dict(zip(b, a))
# print(d)


# b = [12, 1, 2]
# d = list(zip(b))
# print(d)

#
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [2.0, 4.6, 7.5]
#
# d = list(zip(a, b, c))
# print(d)

#
# one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
#
# obj = {
#     'one': {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'},
#     'two': {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# }
# print(obj)
#
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.6}
# two = {'pepper': 0.8, 'onion': 0.55}
# print({**one, **two})


# {{'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55}}
# {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
#
# data = ['a', 'b', 'c', 'd']
#
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(len(data)):
#     print(i, end=" ")
# print()
#
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1
#
# for j, i in enumerate(data, 100):
#     print(j, ":", i)
#
# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ":", i, "->", v)
#
#
# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6, 9, 5))
# print(func())

#16.01.23
# def to_dict(*lst):
# print(*lst)
# print(lst)
# return {i: i for i in lst}
#  print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))

#  def ch(*args):
# pass
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
# def fun(*a):
#     return [i for i in a if i < sum(a) / len(a)]
#     print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))

# print(fun(3, 6, 1, 9, 5))# def func(*lst):
#     sum = 0
#     count = 0
#     new_lst = []
#     for i in lst:
#         sum += i
#         count += 1
#     avarange = sum / count
#     print('Ср. ариф: ', avarange)
#     for j in lst:
#         if j < avarange:
#             new_lst.append(j)
#     print(new_lst)

#     func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# def func(a, b,  *args):
#     return a, b, args
#    print(func(2, 3))
# print(func(2, 3, 4, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name:", student, end=", scores: ")
#     a, b = None, ""
#     for score in scores:
#         a = str(score) + ", "
#         b += a
#     print(b[:-2])
#     print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)
#
# def print_scores(student, *scores):
#     print("Student Name:", student, end=", scores: ")
#     count = 0
#     for score in scores:
#         count += 1
#         if count != len(scores):
#             print(score, end=", ")
#         else:
#         print(score)

#         print_scores("Kate", 100, 95, 88, 92, 99)
#         print_scores('Rick', 96, 20, 33, 56)

# def reverse_num(n):
# 12 => 21
# s = str(n)
#     return int(s[::-1])
#      def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or only_add and i % 2:
#             res.append(reverse_num(i))
#     return res
#     print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))

# def func(**kwargs):
#     return kwargs
#      print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))
# def func(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()

#      func(name="Irina", surname="Sharma", age=22, phone=1234567890)
# func(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=9876543210)
# def func(**data):
#      for key, value in data.items():
#          my_dict[key] = value
#      return my_dict
#     my_dict.update(data)
#     my_dict = {'one': 'first'}
# func(k1=22, k2=31, k3=11, k4=91)
# print(my_dict)

# func(name='Bob', age=31, weight=61, eyes_color='grey')# print(my_dict)
# def func(a, *args, b=2, **kwargs):
#     print(a, kwargs, args, b)
#      func(4, 5, 6, 7, b=3, k1=22, k2=31, k3=11, k4=91)

# Области видимости (scope)
# name = "Tom"
# глобальная переменна# surname = "sum"
# def hi():
#     global name, surname
#     name = "Sam"
# локальные переменные
#     surname = "Johnson"
#     print("Hello", name, surname)### def bye():
#     print("Good bye", name, surname)
#      hi()
# print(surname)
# bye()
# i = 5
#  def func(arg=i):
#     print(arg)

#      i = 6
# func()
# 5
# x = 5
# def add_two(a):
#      x = 2
#        def add_some():
#          x = 3
#         return a + x
#              return add_some()
#          print(add_two(3))

# import builtins
#  name = dir(builtins)
#  for t in name:
#     print(t)

# type1 = [8, 1, 2, 4, 5, 6, 9]
# print(min(type1))
#  a = [7, 8, 9, 5]
# print(type(a))
# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)

#             inner_func()
#          outer_func("world!")

# def fun1():
#     a = 6
#         def fun2(b):
#         a = 4
#         print(a + b)
#             print("a =", a)
#     fun2(4)
#     fun1()
#
# x = 25
# t = 0
#  def fn():
#     global t
#     a = 30
#         def inner():
#         nonlocal a
#         a = 35
#              inner()
#     t = a
#      fn()
# z = x + t
# 25 + 30 = 55
# print(z)
# 25 + 35 = 60
# x = 5
#  def fn1():
#     x = 25
#         def fn2():
#          x = 33
#                 def fn3():
#             nonlocal x
#             x = 55
#                    fn3()
#         print('fn2.x =', x)
#              fn2()
#     print('fn1.x =', x)

#      fn1()
# print(x)
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#        def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#              inner()
#              return [a, b]
#          res = outer(2, 3, -1, 4)
# # print(res)

# Замыкание
# def outer(n):
#     def inner(x):
#         return n + x
#              return inner
#          add = outer(5)
# print(add(10))
# print(add(20))
#  add1 = outer(6)
# print(add1(10))
# print(outer(5)(10))
# def func1():
# a = 1
# b = 'line'
# c = [1, 2, 3]
# def func2():
# nonlocal a, b
# c.append(4)
# a = a + 1
# b = b + "_new"
# return a, b, c
# return func2func = func1()print(func())


# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#  print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))
# s = 0
#  def rect_paral_square(a, b, c):
#  def rect_square(i, j):
#         return i * j
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#  rect_paral_square(2, 4, 6)
# print(s)
# rect_paral_square(5, 8, 2)
# print(s)
# rect_paral_square(1, 6, 8)
# print(s)
# def rect_paral_square(a, b, c):
#     s = 0
#   def rect_square(i, j):
#         nonlocal s
#         s += i * j
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))
# def func(city):
#     s = 0
# def wrap():
#   nonlocal s
#         s += 1
#   print(city, s)
#   return wrap
#   res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#    return student
#   A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))
# def func(a, b):
#     def add():
#     return a + b
#     def sub():
#         return a - b
#      def mul():
#         return a * b
#      def replace():
#         print("qqq")
#
#      replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#   obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# obj1()
# lambda (Анонимные функции)
# print((lambda x, y: x + y)(1, 2))
# c = (lambda x, y: x + y)('a', 'b')
# print(c)
# a = 5
# func = lambda x, y: x + y + a
# b = func(1, 2)
# print(b)
# print(func('a', 'b'))
# (lambda: print("Hello"))()
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# summ = lambda a=1, b=2, c=3: a + b + c
#print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())
# func = lambda *args: args
# print(func(1, 2, 3, 4, 5, 6, 7))
#  print(func())
#   c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#     for t in c:
#     print(t('abc_'))def inc(n):
#     return lambda x: n + x
#     f = inc(42)
#     print(f(3))
#  inc1 = (lambda n: lambda x: n + x)
#     f3 = inc1(42)
#     print(f3(3))
#     print("!!!", (lambda n: lambda x: n + x)(42)(3))
#     def inc2(n):
#     def wrap(x):
#     return n + x
#     return wrapf1 = inc2(42)
#     print(f1(3))

#print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))

#print((lambda a,b,c: a if c > a < b else c if b > c < a else b)(18,15,9))

# dim = [1,2,3]
# dim1 = [4,5,6]
# res = list(map(lambda x,y: x+y, dim,dim1))
# print(res)

# print((lambda i: lambda j: lambda k: i + j + k)(2)(4)(6))
# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федоров', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#  res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)
# def func(i):
#     return i[1]
#    d = {'b': 15, 'a': 3, 'c': 7}
# {'a': 3, 'c': 7, 'b': 15}
# lst = list(d.items())
# print(lst)
#  lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# print(dict(lst))
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# ]print(a[3](12, 3))
# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#  for i in b:
#     if i < 0:
#   print(a['two'](i))
#     elif i > 0:
#    print(a['one'](i))
#     else:
#    print(a['three'](i))
# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#  d[3]()
# print((lambda a, b: a if a > b else b)(12, 5))
# m = lambda a, b, c: a if a < b else b if b < c else c
# print(m(19, 28, 5))
#  print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 18, 15))
# map(func, iterable), filter(func, iterable)
# def mul(t):
#     return t * 2# lst = [2, 8, 12, -5, -10]
#  lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)
# t = (2.88, -1.75, 100.03)
#  t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
#  print(t2)
# area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
# res = list(map(round, area, range(1, 7)))
# print(res)
# print(round(3.45612131, 3))
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#  res = list(map(lambda x, y: (x, y), st, num))
# print(res)l1 = [1, 2, 3]l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# z = [15,37,36,26,27,35,27,20,24,3]
# res = list(filter(lambda a: 10 < a <= 20, z ))
# print(res)

#23.01.23
# filter(func, iterable)
# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))#
# print(res)
# z = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# res = list(filter(lambda a: 10 < a <= 20, z))
# print(res)
# from random import randint
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)
# nums = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, nums))
# print(res)
# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# (1, 3, 5, 7, 9)# print(m)
#  m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)
# Декораторы# def hello():
#     return 'Hello, I am func "hello"'
#  def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#  super_func(hello)# def hello():
#     return 'Hello, I am func "hello"'
#  test = hello# print(test())
# def my_decorator(func):
#     def func_wrapper():
# print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#   def func_test():
#     print('Hello, I am func "func_test"')
#   test = my_decorator(func_test)
# test()
# def my_decorator(func):
# декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
# @my_decorator
# декоратор# def func_test():
# декорируемая функция
#     print('Hello, I am func "func_test"')
# func_test()
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#   return wrap
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#    return wrap
#  @bold
# @italic
# def hello():
#     return "text"
# print(hello())
# def cnt(fn):
#     count = 0
#  def wrap():
#   nonlocal count
#         count += 1
#         fn()
#  print("Вызов функции:", count)
# return wrap
#  @cnt
# def hello():
#     print("Hello")
#  hello()
# hello()
# hello()
# hello()
# hello()
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
# return wrap
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#  print_full_name("Ирина", "Назарова")
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print(*args)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#   return wrap
#   @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#  @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#  print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", last="Назаров", second="Федорович")
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#  return wrap
#     return args_dec
#  @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#  @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
# summa(5, 2)
# sub(5, 2)
#  def decor(*args):
#     def args_dec(fn):
#         def wrap(x, y):
#   print(args[0], x, args[1], y, "=", end=" ")
#             print(*args, end=" ")
#             fn(x, y)
#  return wrap
#     return args_dec
#  @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#  @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#  summa(5, 2)
# sub(5, 2)
# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
# return wrap
# return decor
#  @multiply(3)
# def return_num(ch):
#     return ch
#    print(return_num(5))
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#  for i in range(len(args)):
#    if type(f_args[i]) != args[i]:
#    raise TypeError("Некорректный тип данных", f_args[i])
# print("Некорректный тип данных!")
#    for k in kwargs:
#    if type(f_kwargs[k]) != kwargs[k]:
#      raise TypeError("Некорректный тип данных", f_kwargs[k])
# return fn(*f_args, **f_kwargs)
# return wrap
#     return wrapper### @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#   @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#   @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello"):
#     return (x + y) * z
#  print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))
# def args_decorator(tx=None, decorator_text=""):
# def my_decorator(func):
# def wrap(*args):
# print(decorator_text, end="")
# func(*args)
# return wrap
# if tx is None:
# return my_decorator
# else:
# return my_decorator(tx)
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
# print(text)
# @args_decoratordef
# hello_world2(text):
# print(text)
# hello_world("world!")
# hello_world2("Hi!")
#
# a = 5
# print(a)

# print("Вносим изменения в новый репозиторий")

#01.02.2023

#ФАЙЛЫ

# f = open('text.txt') #mode = 'r'
# print(*f)
#
# i = 0
# f = open('text.txt')
# for a in f:
#     i += 1
# f.close()
# print(i)

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]
# print(list(map(str,lst)))
#
# with open(file_name, 'w+') as my_file:


#13.03.23

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
# class OS:
#     def system(self):
#         return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
# comp = Computer()
# print(comp.name)
# me_os = comp.os
# my_cpu = comp.cpu
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#         class Inner:
#             def display1(self):
#                 print("Inner Of Base Class")
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#      class Inner(Base.Inner):
#         def display2(self):
#           print("Inner Of SubClass")
#
# a = SubClass()
# a.display()
# b = a.db
# b.display1()
# b.display2()

#Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, + "is sleeping")
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + "is playing")
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + "is barking")
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()


# class AA:
#     def __init__(self):
#         print("Инициализатор AA")
# class A:
#     def __init__(self):
#         print("Инициализатор A")
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор B")
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор C")
#
# class D(B,C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор D")
#
# d =D()
# print(D.mro())
# print(D.__mro__)

# class Point:
#     def __init__(self, x,y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp:Point, ep:Point):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         super().__init__(color,width)
#
# class Line(Pos,Style):
#     def __init__(self, sp:Point, ep:Point, color, width):
#         Pos.__init__(self, sp,ep)
#         Style.__init__(self,color,width)

# Миксины (примеси)

#class Displayer:
#   @staticmethod
#    def display(message):
 #      print(message)


#class LoggerMixin:
 #   def log(self, message, filename="logfile.txt"):
  #      with open(filename, 'a') as fh:
 #           fh.write(message)

 #   def display(self,message):
#       Displayer.display(message)
 #       self.log(message)

#class MySubClass(LoggerMixin, Displayer):
 #   def log(self,message,filename=""):
 #       supper().log(message, filename="log.txt")

#sub = MySubClass()
#sub.display("Это строка будет напечатана и сохранена в файл")


# class Goods:
#     def __init__(self,name,weight,price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name},{self.weight},{self.price}")
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         Mixin.ID += 1
#         self.id = Mixinlog.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
# class NoteBook(Goods, MixinLog):
#     pass
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.save_log()

# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     DAY = 86400
#
#     def __init__(self,sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec / 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return x if x > 9 else "0" + str(x)
#
#     def __add_(self,other):
#         if not isinstance(other,Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данным Clock")
#         return Clock(self.sec + other.sec)
#
#        def __eq__(self,other):
#           if self.sec == other.sec:
#               return  True
#           return False
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec / 3600) % 24
#
#        if key == "hour":
#            set.sec = s + 60 * m + value * 3600
#        elif key == "min":
#            self.sec = s + 60 * value + h * 3600
#        elif key == "sec":
#            self.sec = value + 60 * m + h * 3600
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# print(c1["hour"],c1["min"],c1["sec"])
# c1["hour"] = 9
# c1["min"] = 20
# c1["sec"] = 30
# print(c1["hour"],c1["min"],c1["sec"])
# print(c1.get_format_time())

#c1 = Clock(100)
#c2 = Clock(200)
#c4 = Clock(300)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
# c3 = c1 + c2 + c4  #c3 = Clock(100+200)  #c3 = Clock(300) + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
# print(c4.get_format_time())
# # c2 += c1
# print(c2.get_format_time())


#class Student:
 #  def __init__(self, name, marks):
 #      self.name = name
 #      self.marks = list(marks)

 #  def __getitem__(self, item):
  #     if 0 <= item < len(self.marks):
  #         return self.marks[item]
   #    else:
   #        raise IndexError("Неверный индекс")
            # print("Неверный индекс")

  #  def __setitem__(self, key, value):
  #      if not isinstance(key, int) or key < 0:
  #          raise TypeError("Индекс должен быть положительным числом")

   #  if key >= len(self.marks):
   #      off = key + 1 - len(self.marks)
    #     self.marks.extend([None] * off)

  #   self.marks[key] = value

  #  def __delitem__(self,key):
  #      if not isinstance(key, int):
   #         raise TypeError("Индекс должен быть целым числом")
   #     del self.marks[key]


#s1 = Student("Сергей", [5,5,3,4,5])
#print(s1[2])
#s1[2] = 4
#print(s1.marks)
# print(s1.marks[2])
# print([None] *6)


# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
# cat = Cat("Пушок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.coord = args
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(5,7,3)
# print(len(p))

#
# from random import choice, randint
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         if self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age='{self.age}', pol'={self.pol}'"
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M","F"])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Types are not supported!")
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)

# Полиморфизм
# class Rectangle:
#     def __init__(self,w,h):
#         self.w = w
#         self.h = h
#
#     def get_per_rect(self):
#         return 2* (self.w + self.h)
#
# class Square:
#     def __init__(self,a):
#         self.a = a
#
#     def get_per_sq(self):
#         return 4 * self.a
#
# class Triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
# r1 = Rectangle(1,2)
# r1 = Rectangle(3,4)
# s1 = Square(10)
# s2 = Square(20)
#
# shape = [r1,r2,s1,s2]
#
# for g in shape:
#     print(g.get_perimetr())
#
#     if isinstance(g, Rectangle):
#         print(g.het_per_rect())
#     else:
#         print(g.get_per_sq())
# print(r1.get_per_rect(), r2.get_per_rect())
# print(s1.get_per_sq(), s2.get_per_sq())

# class Number:
#     def __init__(self, value):
#         self.value = value
#     def total(self,a):
#         return self.value + a
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self,a):
#         return len(self.value + str(a))
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#      def info(self):
#              return f"Я кот. Меня зовут {self.name}, Мой возраст {self.age}."
#       def make_sound(self):
#             return f"{self.name} мяукает."
# class Dog:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#      def info(self):
#            return f"Я собака. Меня зовут {self.name}, Мой возраст {self.age}."
#      def make_sound(self):
#           return f"{self.name} гавкает."
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
# for i in [cat, dog]:
# print(i.info())
# print(i.make_sound())


# class Human:
#     def __init__(self,last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'{self.last_name}{self.first_name}{self.age}', end=" ")
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#        super().__init__(last_name, first_name, age)
#        self.speciality = speciality
#        self.group = group
#        self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality}{self.group}{self.rating}", end=" ")
#
# class Teacher(Human):
#     def __init__(self,last_name, first_name, age, speciality, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality}{self.experience}", end=" ")
#
# class Graduate(Student):
#     def __init__(self,last_name, first_name, age, speciality, group, rating,topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)]
# for i in group:
#     i.info()
#     print(i.first_name)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#     def get_perimetr(self):
#             return 2 * (self.w + self.h)
# class Square:
#     def __init__(self, a):
#         self.a = a
#     def get_perimetr(self):
#         return 4 * self.a
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#         r1 = Rectangle(1, 2)
#         r2 = Rectangle(3, 4)
#         s1 = Square(10)
#         s2 = Square(20)
#         t1 = Triangle(1, 2, 3)
#         t2 = Triangle(4, 5, 6)
#         shape = [r1, r2, s1, s2, t1, t2]
#         for g in shape:
# print(g.get_perimetr())


#pip install requests

# import requests



# from bs4 import BeautifulSoup


# f = open ('index.html').read()
# soup = BeautifulSoup(f,"html.parser")
# row = soup.find("div", class_="name")
#row = soup.find_all("div", class_="row")[1].find(class_="name").text
# row = soup.find_all("div", {"data-set":"salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", id="whois").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
# f = open ('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f,"html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)


# import re
# def get_salary(s):
#     pattern = r""
#     res = re.findall(patterns)
#     print(res)
#
# f = open ('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f,"html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)

# import requests
#
# res = requests.get("https://ru.wordpress.org/")
# print(res.headers)

#
# import requests
# from bs4 import BeautifulSoup
# import re
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("article")
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find('span', class_="rating-count")
#     print(rating)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
# if __name__=="__main__":
#     main()




#12.04.23

# import sqlite3
#
# # con = sqlite3.connect("profile.db")
# # cur = con.cursor()
# #
# # con.close()
#
# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE  IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )""")
#
#     cur.execute("DROP TABLE users")


# 24.04.23

# import sqlite3
#
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 34000),
#     ('Honda', 29000),
# ]
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE  IF NOT EXISTS cars(
#        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#        model TEXT,
#        price INTEGER
#    )
#    """)
    # cur.executescript("""
    # DELETE FROM cars WHERE model LIKE 'B%';
    # UPDATE cars SET price = price + 100;
    # """)
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?,?)", cars)
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?,?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(1, 'Volvo', 55000)")
    # cur.execute("INSERT INTO cars VALUES(1, 'Mercedes', 65000)")
    # cur.execute("INSERT INTO cars VALUES(1, 'Bentley', 35000)")
    # cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52000)")

# con.commit()
# con.close()

# con = None
# try:
#     con = sqlite3.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE  IF NOT EXISTS cars(
#            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#            model TEXT,
#            price INTEGER
#        );
#        BEGIN;
#        INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#         UPDATE cars2 SET price = price + 100;
#         """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса",e)
# finally:
#     if con:
#         con.close
#26.04.23
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE  IF NOT EXISTS cars(
#        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#        model TEXT,
#        price INTEGER
#    );
#    CREATE TABLE IF NOT EXISTS cost(
#    name TEXT, tr_in INTEGER, buy INTEGER
#    );
#    """)

    # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    # last_row_id = cur.lastrowid
    # buy_car_id = 2
    # cur.execute("INSERT INTO cost VALUES('Илья',?,?)", (last_row_id, buy_car_id))
    # cur.execute("SELECT model, price FROM cars")
    #
    # # for res in cur:
    # #     print(res)
    #
    # # rows = cur.fetchall()
    # # print(rows)
    #
    # rows = cur.fetchone()
    # print(rows)
    #
    # rows2 = cur.fetchmany(5)
    # print(rows2)

# def read_ava(n):
#     try:
#        with open(f"avatars/{n}.png", 'rb') as f:
#         return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# def wirte_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return  False
#     return True
#
# with sqlite3.connect('cars.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#     name TEXT,
#     ava BLOB,
#     score INTEGER
#     );
#     """)

    # img = read_ava(1)
    # if img:
    #       binary = sqlite3.Binary(img)
    #       cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))

    # cur.execute("SELECT ava FROM users")
    # img = cur.fetchone()['ava']
    #
    # write_ava('out.png', img)

# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#     with open('sql_dump.sql', "w") as f:
#         for sql in con.iterdump():
#             print(sql)

# with sqlite3.connect('automobile.db') as con:
#      cur = con.cursor()
#
#      with open('sql_dump.sql', "r") as f:
#             sql = f.read()
#             cur.executescript(sql)

#
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# DATABASE_NAME = 'students.db'
#
# engine = create_engine(f"sqlite:///{DATABASE_NAME}")
# Session = sessionmaker(bind=engine)
# Base = declarative_base()
#
#
# def create_db():
#      Base.metadata.create_all(engine)


# import os
# from sqlalchemy import and_, or_, not_,desc
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator


# if __name__ =='__main__':
#      db_is_created = os.path.exists(DATABASE_NAME)
#      if not db_is_created:
#           db_created.create.db()
#
#      session = Session()
#

#10.05.23
#      print(session.query(Lesson).all())
#      print("*" * 60)
#
#      for it in session.query(Lesson):
#           print(it.lesson_title)
#
#           print(session.query(Lesson).count())
#           print("*" * 60)
#
#      for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('M%'))):
#           print(it)
#      print("*" * 60)
#
#      for it, gr in session.query(Lesson.lesson_title, Group.group_name).\
#              filter(and_(association_table.c.lesson_id == Lesson_id,
#                          association_table.c.group_id == Group_id,
#                          Group.group_name == 'MDA-7')):
#           print(it, gr)
#      print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
#       print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
#       print(session.query(Student).filter(Student.age.between(16,17)).all())
#       print(session.query(Student).filter(not_(Student.age.between(16,17))).all())
#        print(session.query(Student).filter(not_(Student.age.like("1%"))).limit(4))

       # for it in session.query(Student).filter(not_(Student.age.like("1%"))).limit(4).offers(3):
       #       print((it)
    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print((it)

    # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
    #     print(it)

    # for it in session.query(distinct(Student.age)):
    #     print(it)
    # for it in session.query(Student.age).filter(Student.age < 20).distinct():
    #      print(it)
# for it in session.query(Lesson):
#     print(it.lesson_title)
# print("*" * 60)
#
# i = session.query(Lesson).first()
# i.lessin_title = "Информатика"
# session.add(i)
# session.commit()

    # for it in session.query(Lesson):
    #    print(it.lesson_titile)
    # print("*" * 60)
    #
    # session.query(Lesson).filter(Lesson.lesson_title.like("%M%")
    #                              ).update({'lesson_title': 'M'}, synchronize_session='fetch')
    # session.commit()
#    for it in session.query(Lesson):
#     print(it.lesson_titile)
#   print("*" * 60)

#    session.add(Lesson(lesson_title="Математика"))
#     session.commit()

    # for it in session.query(Lesson):
    #    print(it.lesson_titile)
    # print("*" * 60)
    #
    # i = session.query(Lesson).filter(Lesson(lesson_title == "Физика").one()
    # session.delete(i)
    # session.commit()
    #
    # for it in session.query(Lesson):
    #    print(it.lesson_titile)
    # print("*" * 60)

#Шаблонизатор  Jinja
#pip install jinja2

from jinja2 import Template

#per = Perso("Игорь", 28)
# name = "Игорь"
# age = 28
# per = {'name': "Игорь", 'age':28}
# tm = Template("Меня зовут {{ p.name }}. Мне {{p.age}} лет.")
# #tm = Template("Меня зовут {{ p.get_name() }}. Мне {{ p.get_age()}} лет.")
# msg = tm.render(p=per)
#
# print(msg)
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#
# per = Perso("Игорь", 28)
# # name = "Игорь"
# # age = 28
#
# #tm = Template("Меня зовут {{ p.name }}. Мне {{ p.name}} лет.")
# tm = Template("Меня зовут {{ p.get_name() }}. Мне {{ p.get_age()}} лет.")
# msg = tm.render(p=per)
#
# print(msg)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Сочи'},
#     {'id': 4, 'city': 'Минск'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
# link = """<select>
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{c['id']}}>{{c['city']}}</option>
#     {% elif c.city == "Москва" -%}
#     {% else %}
#          {{c['city']}}
#     {% endif -%}
# {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# cars = [
#     {"model": 'Audi', 'price': 23000},
#     {"model": 'Skoda', 'price': 54000},
#     {"model": 'Renault', 'price': 34000},
#     {"model": 'Wolksvagen', 'price': 45000},
# ]

# tpl = "{{ cs | sum(attribute='price')).price }}"
# tpl = "{{ ((cs | random).model }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# person = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 23, 'weight': 34.5},
#     {'name': 'Виталий', 'year': 34, 'weight': 98.5}
# ]

# tpl = """
# {% for u in user -%}
#     {% filter upper %}
#       {{ u.name }}
#     {% endfilter %}
# (% endfor -%}
# """

# tpl = """
# {% for u in user -%}
#     {% filter string %}
#       {{ u.year }} -  {{ u.weight }}
#     {% endfilter %}
# (% endfor -%}
# """
#
# tm = Template(tpl)
# msg = tm.render(user=person)
#
# print(msg)

# html = """
# {% macro text_input(name,value='', type='text', size='40') %}
#      <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size={{ size}}>
# {% endmacro %}
#
# <p>{{ text_input('username') }}</p>
# <p>{{ text_input('email', type='password') }}</p>
# <p>{{ text_input('password') }}</p>
# """

# tm = Template(html)
# msg = tm.render(user=person)
#
# print(msg)



# 15.05.23

# person = [
#      {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#      {'name': 'Никита', 'year': 23, 'weight': 34.5},
#      {'name': 'Виталий', 'year': 34, 'weight': 98.5}
# ]

# html = """
# {% macro list_users(list_of_user) -%}
#      <ul>
#          {% for u in list_of_user -%}
#          <li>{{ u.name }}{{caller(u)}}</li>
#          {%- endfor %}
#      </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users)%}
# <ul>
# <li>age:{{user.year}}</li>
# <li>weight:{{user.weight}}</li>
# </ul>
# {%endcall%}
#  """
# html = """
# {% macro list_users(list_of_user) -%}
# <ul>
#      {% for u in list_of_user -%}
#      <li>{{ u.name }}
#        <ul>
#           <li>age:{{u.year}}</li>
#           <li>weight:{{u.weight}}</li>
#        </ul>
#      </li>
#     {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {{ list_users(users) }}
# """
# tm = Template(html)
# msg = tm.render(user=person)
#
# print(msg)
#
# tm = Template(html)
# msg = tm.render(user=person)
#
# print(msg)


# from jinja2 import Environment, FileSystemLoader
#
# # person = [
# #      {'name': 'Алексей', 'year': 18, 'weight': 78.5},
# #      {'name': 'Никита', 'year': 23, 'weight': 34.5},
# #      {'name': 'Виталий', 'year': 34, 'weight': 98.5}
# # ]
#
# subs = ['Культура', 'Наука', 'Политика', 'Спорт']
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('company.html')
# msg = tm.render(list_table=subs)
#
# print(msg)

#24.05.23
#Django


print("Загружено на GitHub")