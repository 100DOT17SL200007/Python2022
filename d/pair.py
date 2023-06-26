from math import sqrt


class Pair:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def proiz(self):
        return self._a

    @proiz.setter
    def proiz(self, new_a):
        if isinstance(new_a, (int, float)):
            self._a = new_a

    @property
    def proiz1(self):
        return self._b

    @proiz1.setter
    def proiz1(self, new_b):
        if isinstance(new_b, (int, float)):
            self._b = new_b

    def get_summ(self):
        return self._a + self._b

    def get_product(self):
        return self._a * self._b

    def pair_info(self):
        print(f'Сумма чисел a и b: {self.get_summ()}')
        print(f'Произведение чисел a и b: {self.get_product()}')


class Right_Triangle(Pair):
    def get_gipot(self):
        return round(sqrt(self._a ** 2 + self._b ** 2), 2)

    def get_square(self):
        return self.get_product() / 2

    def get_info(self):
        print(f'Гипотенуза треугольника ABC: {self.get_gipot()}')
        print(f'Площадь треугольника ABC: {self.get_square()}')


p1 = Pair(5, 8)
p1.pair_info()
p1.proiz = 9
p1.pair_info()
p1.proiz1 = 10.5
p1.pair_info()

tr = Right_Triangle(5, 8)
tr.get_info()
