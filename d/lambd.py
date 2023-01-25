#1. задание
#print((lambda r, p: p * (r * 2))(3.14,2))
#print((lambda a,b: a * b)(10,13))
#print((lambda z,v,h: ((z + v) * h) / 2)(7,5,3))

#2. задание
# print((lambda a,b,c: a * b * c)(2,5,5))

#3. задание
# num = [3,5,7,3,9,5,7,2]
# print(list(map(lambda num1: num1 ** 2, num)))
# print(list(map(lambda num1: num1 ** 3, num)))

#4.задание
# student = [
#           {'name': 'Jennifer', 'final': 95},
#           {'name': 'David', 'final': 92},
#           {'name': 'Nikolas', 'final': 98},
#            ]
# res = sorted(student, key = lambda item: item['name'])
# print(res)
# res = sorted(student, key = lambda item: item['final'], reverse=True)
# print(res)

#5. задание
# a = [3,6,8,9,1,2]
# print(list(map(lambda b: b * a.index(b) ** 3, a)))

#6. задание
student = [
          {'name': 'Jennifer', 'final': 95},
          {'name': 'David', 'final': 92},
          {'name': 'Nikolas', 'final': 98},
          ]
res = sorted(map(student, key = lambda item: item(['final']))
print(res)