# functional program to use reduce program length
# LAMBDA code

#cube of a function
cube=lambda num:num**3
print(cube(3))

add=lambda num1,num2:num1+num2
print(add(3,5))

sub=lambda num1,num2:num1-num2
print(sub(5,6))

even=lambda num:num%2==0
print(even(11))

adding=lambda n1,n2,n3,n4:n3+n1+n2+n4
print(adding(10,20,30,40))


#map() no. of input = no.of output
#filter() output lesser than input
#reduce() #one output, eg:- lagest no,highest numbr