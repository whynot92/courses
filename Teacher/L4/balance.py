class Account():
    def __init__(self, balance=0):
        self.__balance = balance

    def add(self, money):
        self.__balance += money

    def minus(self, money):
        if self.__balance >= money:
            self.__balance -= money
        else:
            print("Ми не має достатньо коштів")

    def __str__(self):
        return str(self.__balance)

acc1 = Account(12)

acc1.add(5)
acc1.minus(12)
print(acc1)
acc1.__balance = 100
print(acc1)