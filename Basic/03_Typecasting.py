# Type casting

from ast import Str


print(".........Type casting........")
a = "3534"
print("Original value of a = ",a, " and type is ",type(a))

a = int(a)+10
print("Int value of a = ",a, " and type is ",type(a+10))

b = Str(a) 
c = "1"+"amarendra"
print("String value of a = ",a, " and type is ",type(a))
