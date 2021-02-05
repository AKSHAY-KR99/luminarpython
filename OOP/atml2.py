class bank:
    def withdraw(self):
        print("withdraw")
    def __deposit(self):
        print("deppo")
    def balance(self):
        print("balance")

class atm(bank):
    pass
Atm=atm()
Atm.withdraw()
Atm._bank__deposit()
Atm.balance()
