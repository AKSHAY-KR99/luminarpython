#polyforms means more than one form
# eg:- consider me, i have differnt charecter in different situation,this is called polymorephism
# 1.mothode overloading
# 2.over riding
# 3.operator overloading

#1.methode overloading
#------------------------
# same methode name, but different number of arguments
#recently take

class math:
    def add(self):
        print("NO ARGUMENT")
    def add(self,num1):
        print("ONE ARGUMENT")
    def add(self,num1,num2):
        print("TWO ARGUMENTS")

m=math()
m.add(10,79)