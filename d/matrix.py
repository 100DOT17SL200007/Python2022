# 21.12.22
#задание1.
# from math import sqrt, pi
# x = int(input("Наберите цифру от 1-3, 1 - треугольник; 2 - прямоугольник; 3 - круг: "))
# if x == 1:
#     a = int(input("Введите сторону a:" ))
#     b = int(input("Введите сторону b:" ))
#     c = int(input("Введите сторону c:" ))
#     h = (a+b+c)/2
#     s = sqrt((h*(h-a)*(h-b)*(h-c)))
# elif x == 2:
#     a = int(input("Введите сторону a:" ))
#     b = int(input("Введите сторону b:" ))
#     s = a * b
# elif x == 3:
#     num = int(input("Введите радиус окружности: "))
#     s = pi * (num ** 2)
# print(round(s,2))



# задание2.
# a = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# for row in a:
#   for x in row:
#     print(x, end="\t")
#   print()
# for vov in a:
#     for y in vov:
#         print(y)

#задание3.
# from random import randint
# a,b = 6,6
# num = [[randint(1,10) for x in range(a)] for y in range(b)]
# for row in num:
#     for x in row:
#         print(x,end="\t")
#     print()
# m = [randint(1,7) for x in range(1,7)]
# print(m)
# for y in range(b):
#     if y % 2 == 0:
#         num.append(m)
# for b in num:
#     for y in b:
#         print(y,end="\t")
#     print()

#задание4.
# from random import randint
# a,b = 6,6
# num = [[randint(1,10) for x in range(a)] for y in range(b)]
# for row in num:
#     for x in row:
#         print(x,end="\t")
#     print()
# matrix = []
# for y in range(b):
#    if y % 2 == 0:
#        if y % 2 !=0:
#         print(y)