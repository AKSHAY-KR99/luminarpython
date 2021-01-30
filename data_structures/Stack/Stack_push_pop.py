size=int(input("Enter a size : "))

top=0

stk=[]

n=1
def push():
    item=int(input("Enter the element : "))
    global top
    if top<size:
        stk.insert(top,item)
        top+=1
    else:
        print(top)
        print("stack Overflow")


def pop():
    global top
    if top<=0:
        print("stack is empty....!!!")
    else:
        top-=1
        print(stk[top]," popped out...!!")


def display():
    for i in range(0,top):
        print(stk[i])




while(n!=0):
    option=int(input("Enter The operation press 1)PUSH  2)POP  3)DISPLAY  "))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print("Invalid input")
    n=int(input("If u want to exit press '0', to continue press any number"))