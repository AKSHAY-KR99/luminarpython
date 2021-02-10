

from re import *

#patn="a+" #it check for single 'a' or concecutive a(excluding zero number of a)
#patn='a*' #any no. of 'a' including Zero number
patn='a?' #occurance of single a including zero nuber of a
#patn='a{2}' #print group of 2a's

#patn='a{2,4}' #maximum 4a's and minimun 2a's eg:- phone number degit

matcher=finditer(patn,"aaaaaaabababaaba")

for match in matcher:
    print(match.start(),"==>",match.group())

#comon elements in array
#[1,2,3,4,5,6][6,5,4,3,2,1]