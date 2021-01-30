num=10
def change():
    global num      #if do not use GLOBAL key word result will be 20 & 10,else print correct
    num=5
    num*=4
    print(num)
change()
print(num)