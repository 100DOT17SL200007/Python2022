class Student:
    def __init__(self, name):
        self.name = name
        self.text = self.Text()

    def show(self):
        print(self.name, '=>', end=' ')

    class Text:
        def __init__(self):
            self.model = 'HP'
            self.processor = "i7"
            self.memory = '16'

        def show(self):
            print(f'{self.model}, {self.processor}, {self.memory}')


s = Student('Vladimir')
s.show()
i = s.text
i.show()

s2 = Student('Roman')
s2.show()
i2 = s2.text
i2.show()
