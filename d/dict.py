# 1.задание
# col = ['red', 'green', 'blue']
# colors = ['#FF0000', '#008000','#0000FF']
# d = dict(zip(col, colors))
# print(d)

# col = {}
# col.update([('red', '#FF0000'), ('green', '#008000'),('blue', '#0000FF')])
# print(col)

# 2.задание
# d = {i : i**3 for i in range(1,10)}
# print(d)

#3.задание
# a = ['color','fruit', 'pet']
# b = ['blue','apple','dog']
# c = {}
# c.update([('color', 'blue'),('fruit', 'apple'),('pet','dog')])
# print({v: k for k, v in c.items()})

#4. задание
# def f(*a):
#     print(min(a))
# f(10,9)
# f(2,3,4)
# f(3, 5, 10, 6)
#5. задание
# def f(*a):
#     i = 0
#     for i in range(len(a)):
#        print([a[i] + a[(i+1) % len(a)]] , end=" ")
# f(3,9,1)
# f(2,5,4,2)
# f(3,5,10,6,3)
