class Avto:
    print('Данные автомобиля ')

    def __init__(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price
    def get_avto(self):
        print(f'Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n'
              f'Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}')



v = Avto('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
v.get_avto()