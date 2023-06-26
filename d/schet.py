class Account:
    rub1 = 0.025
    rub2 = 0.023
    valuta = 'RUB'
    valuta_usd = 'USD'
    valuta_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.num} принадлежащий {self.surname} был закрыт')

    @classmethod
    def usd(cls, z):
        cls.rub1 = z

    @classmethod
    def eur(cls, z):
        cls.rub2 = z


    @staticmethod
    def convert(value, z):
        return value * z

    @staticmethod
    def commission(val):
        per = val*0.05
        return per+val

    def convert_usd(self):
        usd_val = Account.convert(self.value, Account.rub1)
        print(f'Состояние счета: {usd_val} {Account.valuta_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rub2)
        print(f'Состояние счета: {eur_val} {Account.valuta_eur}.')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.valuta}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'Сумма для снятия с коммиссией 5% составила :{val} {Account.valuta}.\nНа вашем балансе недостаточно средств')
        else:
            self.value -= val
            print(f'Сумма для снятия с коммиссией 5% составила:{val} {Account.valuta}.\n{val} {Account.valuta} были успешно сняты!')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.valuta} было успешно добавлено!')
        self.print_balance()

    def print_info(self):
        print('Информация о счёте')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)




acc = Account('12345', 'Вернан', 0.05, 2000)
acc.print_info()
acc.convert_usd()
acc.convert_to_eur()
print()
acc.usd(2)
acc.convert_usd()
acc.eur(3)
acc.convert_to_eur()
print()
acc.edit_owner('Арсас')
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(acc.commission(100))
print()
acc.withdraw_money(acc.commission(5000))
print()
acc.add_money(5000)
print()