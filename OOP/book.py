class Book:
    def __init__(self,page):
        self.page=page
    def __add__(self, other):
        return Book(self.page+other.page)
    def __sub__(self, other):
        return Book(self.page-other.page)
    def __mul__(self, other):
        return Book(self.page*other.page)
    def __str__(self):
        return str(self.page)

obj1=Book(100)
obj2=Book(200)
obj3=Book(300)
print(obj1)
print(obj1+obj2+obj3)
print(obj1-obj2+obj3)
print("multi : ",obj1*obj2*obj3)