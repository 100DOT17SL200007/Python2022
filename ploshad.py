#глобальная
# w = 0
# def ploshad(a,b,c):
#      global w
#      w = 2 * (a * b + a * c + b * c)
#
#      def ploshad1():
#          h = a * b
#      ploshad1()
#      return w
#
# print(ploshad(2, 4, 6))
# print(ploshad(5, 8, 2))
# print(ploshad(1, 6, 8))

#локальная
# def ploshad(a, b, c):
#     def ploshad1():
#         h = a * b
#         c = 2 * (h + h + h)
#         return c
#
#     print(ploshad1())
#
#
# ploshad(2, 4, 6)
# ploshad(5, 8, 2)
# ploshad(1, 6, 8)

#нелокальная
#
# def ploshad(a, b, c):
#     h = 2 * (a * b + a * c + c * b)
#     def ploshad1():
#         nonlocal h
#         h1 = a * b
#         h2 = a * c
#         h3 = c * b
#         w = 2 * (h1 + h2 + h3)
#
#     ploshad1()
#     return h
#
#
# print(ploshad(2, 4, 6))
# print(ploshad(5, 8, 2))
# print(ploshad(1, 6, 8))
