#withdrawal,deposit,balance,CreateAccount

from datetime import datetime
class Bank:
    def create_account(self,acno,person_name,min_balance,bank_name):
        self.acno=acno
        self.p_name=person_name
        self.min_bal=min_balance
        self.bank_name=bank_name
    def deposit(self,amount):
        self.min_bal+=amount
        print("Your A\c ",self.acno,"has been credited with amt",amount,"on",datetime.now(),"avl balance ",self.min_bal)
    def withdrawal(self,amount):
        if(amount<self.min_bal):
            self.min_bal-=amount
            print("Your A\c ", self.acno, "has been debited with amt", amount, "on", datetime.now(), "avl balance ",
                  self.min_bal)
        else:
            print("Transaction error due to insufficient balance")

    def balance(self):
        print("A\c balance is ",self.min_bal)


obj1=Bank()
obj1.create_account(5262635,"Ajay",3954,"federal")
obj1.withdrawal(200)

