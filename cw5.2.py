class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Brak wystraczajacych srodkow na koncie")
        else:
            self.balance -= amount

    def transfer(self, amount, to_account):
        if amount > self.balance:
            print("Brak wystraczajacych srodkow na koncie")
        else:
            self.withdraw(amount)
            to_account.deposit(amount)


class PrivateAccount(Account):
    def __init__(self, account_number, balance=0, salary=0):
        super().__init__(account_number, balance)
        self.salary = salary

    def salary_transfer(self):
        self.deposit(self.salary)


class FirmAccount(Account):
    def __init__(self, account_number, balance=0, zus_number=None):
        super().__init__(account_number, balance)
        self.zus = zus_number

    def pay_zus(self, amount):
        self.withdraw(amount)
        print("Platnosc podatku w wysokosci {} przekazana dla ZUS: {}".format(amount, self.zus))


mojeKonto = PrivateAccount(111111, 1000, 1000)
kontoKamila = PrivateAccount(222222, 500, 1500)
mojaFirma = FirmAccount(222222, 2000, 101010)
print(mojaFirma.balance)
mojaFirma.pay_zus(500)
print(mojaFirma.balance)

print("\n")
print("Przed przelewem z mojego konta do Kamila 500 zl\n")

print("Stan mojego konta: {}".format(mojeKonto.balance))
print("Stan konta Kamila: {}".format(kontoKamila.balance))
mojeKonto.transfer(500, kontoKamila)
print("\n")
print("Po przelewem z mojego konta do Marka 500 zl\n")

print("Stan mojego konta: {}".format(mojeKonto.balance))
print("Stan konta Kamila: {}".format(kontoKamila.balance))
print("\n")

print("Przed wyplata\n")
print("Stan mojego konta: {}".format(mojeKonto.balance))
mojeKonto.salary_transfer()
print("Po wyplacie\n")
print("Stan mojego konta: {}".format(mojeKonto.balance))