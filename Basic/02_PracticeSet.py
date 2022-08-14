#Password checker

username = input('Enter your username = \n')
password = input('Enter your password = \n')

password_length = len(password)
hidden_password = '*' * password_length

print(
    f'your username is {username} and password is {hidden_password}, which is {password_length} characters long'
)
'''
#Age calculator

a = int(input('Enter your birth year = '))

age = 2022 - a
print('your age is: = ',age)

'''

#print(f'your age is: = {age}')
'''
#Conditional statment
#1. Find greatest of four numbers
print(bool("True"))

a = int(input('Enter first number = '))
b = int(input('Enter second number = '))
c = int(input('Enter third number = '))
d = int(input('Enter fourth number = '))
if a>b:
    greater = a
else:
     greater = b

if c>d:
    greater2 = c
else:
     greater2 = d

if greater>greater2:
    greater = greater
else:
     greater = greater2


print('Greatest number is : ',greater)


list = [a,b,c,d]
#print('Greatest number is : ',greater)
print('list number is : ',list)
list.sort()
list.reverse()
print('Greatest number is : ',list[0])#,list[len(list)-1])
'''
'''
print(".........user input........")

a = input('Enter first number = ')
b = input('Enter second number = ')
c = input('Enter operator to perform opration = ')

a = int(a)
b = int(b)

#result = a + b
10
print(a+b)

'''