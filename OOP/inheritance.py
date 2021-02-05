class parent:
    def phone(self):
        print("i have nokia 5310")




class child(parent):  #child inherits parent class
    pass

c=child()
c.phone()
print(c) #childile reference/object



#different types of inheritance
# 1.parent-->child
# 2.super-->sub
# 3.base-->derived