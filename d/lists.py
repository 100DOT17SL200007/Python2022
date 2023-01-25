#1 задача
# a = 0
# num = 20
# z = 0
# while True:
#   a = int(input("Введите число от 1 до 100 включительно, если хотите завершить нажмите 0: "))
#   if a < num:
#          print("Загаданное число больше")
#          z += 1
#   if a > num:
#          print("Загаданное число меньше ")
#          z += 1
#   if a == num:
#          print("Вы угадали число с ", z, "раза")
#          break
#   if a == 0:
#         print("Программа завершена")
#         break
#2 задача
# a = [int(input("->")) for i in range(int(input("Количество элементов в списке: ")))]
# for i in range(len(a)):
#     if i % 2 == 0:
#       print(a[i], end=" ")

#3 задача
# c = []
# a = [1,2,2,4,5,4,1,8,4,4,9,9,2,3,3,1,6,5]
# print(a)
# for i in range(len(a)):
#      if a[i] not in c:
#         c.append(a[i])
# print(c, end=" ")

#4 задача
# for i in range(10):
#     print('*' * (10 - i))