class bank:
    def withdraw(self):
        print("withdraw")
    def __deposit(self): # __deposit is a local methode,beacuse '__' sign.it can only acces inside the bank
        print("deppo")
    def mcall(self):
        self.__deposit()
b=bank()
b.withdraw()
b.mcall()
# else another methode is
b._bank__deposit() # objectname._classname__localmethodename