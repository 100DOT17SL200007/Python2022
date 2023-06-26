c = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
h1 = []
h2 = []
h3 = []

def m():
    for i in c:
        if i % 2 == 0 or i % 3 == 0 and i != 2 and i != 3:
            h1.append(i)
        elif i == 0 or i == 1:
            h3.append(i)
        else:
            h2.append(i)
    print('min: ', min(h2))
    print('max: ', max(h1))

m()