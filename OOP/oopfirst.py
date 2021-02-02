#class
# object
# reference
# class is blue print,prototype,class is a plan,template,design pattern
#class use cheythu undaakunna vasthu ;;;; object
#REFERENCE ::: object ne operate cheyyan upayogikkunnu

class person:
    #methodes are below
    def setperson(self,age,name):
        self.age=age
        self.name=name
    def printperson(self):
        print("name : ",self.name)
        print("age : ",self.age)

#so we created a class named PERSON with attributes name and age

#two methos are created  1.setperson()   2.printperson()

#we have to create REFERENCE (here 'obj' is a reference)

obj=person()
obj.setperson(25,"Xavier")
obj.printperson()


obj2=person()
obj2.setperson(24,"Daniel")
obj2.printperson()