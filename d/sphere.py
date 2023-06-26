from math import pi


class Sphere:
    def __init__(self, radius, volume, square, x, y, z):
        self.__radius = radius
        self.__volume = volume
        self.__square = square
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if isinstance(new_radius, (int, float)):
            self.__radius = new_radius
        else:
            print('Радиус имеет числовое значение')

    @property
    def volume(self):
        return 4 / 3 * pi * self.__radius ** 3

    @property
    def square(self):
        return 4 * pi * self.__radius ** 2

    @property
    def center(self):
        return (self.__x, self.__y, self.__z)

    def set_center(self, new_x, new_y, new_z):
        if isinstance(new_x, (int, float)) and isinstance(new_y, (int, float)) and isinstance(new_z, (int, float)):
            self.__x = new_x
            self.__y = new_y
            self.__z = new_z
        else:
            print('Радиус имеет числовое значение')

    def is_point_inside(self, x, y, z):
        return (self.__x - x) ** 2 + (self.__y - y) ** 2 + (self.__z - z) ** 2 < self.__radius ** 2


v = Sphere(0.6, 0, 0, 0, 0, 0)
print('Радиус сферы: ', v.radius)
print('Объём сферы: ', v.volume)
print('Площадь внешней поверхности сферы: ', v.square)
print('Координаты центра сферы: ', v.center)
print('Находится ли точка внутри сферы:', v.is_point_inside(0, -1.5, 0))
