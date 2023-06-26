a = [5, 9, 6, 7]
b = [3, 11, 8]
c = [2, 4]
d = [10, 1, 12]
s = int(input('1 - сортировка по убыванию. 2 - сортировка по возрастанию\n-> '))


def lis(h1, h2):
    if len(h1) > 1:
        x = h1[(len(h1) - 1) // 2]

        num = [i for i in h1 if i < x]
        num1 = [i for i in h1 if i == x]
        num2 = [i for i in h1 if i > x]
        if h2 == 1:
            h1 = lis(num2, 1) + num1 + lis(num, 1)
        elif h2 == 2:
            h1 = lis(num, 2) + num1 + lis(num2, 2)
    return h1


def mex(a, b, c, d, e):
    lst = a + b + c + d
    if e == 1:
        print(lis(lst, 1))
        return lis(lst, 1)
    elif e == 2:
        print(lis(lst, 2))
        return lis(lst, 2)
    return e


def meaning(lst, lst1):
    f = False
    s = 0
    while s < len(lst) and not f:
        if lst[s] == lst1:
            f = True
        else:
            s += 1
    if f == True:
        return f'Значение  {lst1} найдено'
    else:
        return f'Значение {lst1} не найдено'
num = int(input('Введите значение: '))
print((meaning((mex(a, b, c, d, s)), num)))
