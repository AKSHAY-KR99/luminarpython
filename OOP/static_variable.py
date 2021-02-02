#STATIC VARIABLE

from datetime import datetime
class Bank:

    bank_name="SBI"  #Static variable (Bank.bank_name)
    def __init__(self,acno,person_name,min_balance):
        self.acno=acno
        self.p_name=person_name
        self.min_bal=min_balance

    def deposit(self,amount):
        self.min_bal+=amount
        print(Bank.bank_name,"Your A\c ",self.acno,"has been credited with amt",amount,"on",datetime.now(),"avl balance ",self.min_bal)
    def withdrawal(self,amount):
        if(amount<self.min_bal):
            self.min_bal-=amount
            print("Your A\c ", self.acno, "has been debited with amt", amount, "on", datetime.now(), "avl balance ",
                  self.min_bal)
        else:
            print("Transaction error due to insufficient balance")

    def balance(self):
        print("A\c balance is ",self.min_bal)


obj1=Bank(5262635,"Ajay",3954)
obj1.withdrawal(200)

