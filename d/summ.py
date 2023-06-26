list = [-2, 3, 8, -11, -4, 6]

def s(i):
    if not i:
        return 0
    else:
        count = s(i[1:])
        if i[0] < 0:
         count += 1
        return count

print('Сумма отрицательных чисел:', s(list))
