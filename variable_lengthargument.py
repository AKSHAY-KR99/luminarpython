#in the case of more than two variables
def add(*args):
    return sum(args)

total=add(10,20,30)
print(total)

def print_data(*args):
    print(args)
print_data("ajay","kakkanad","thrissur")



def printing(**kwargs):
    print(kwargs)

printing(name="ajay",site="kakkand",home="thrissur")