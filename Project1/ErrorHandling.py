
#Type of error
#TypeError
#syntax error
#Name error
#Index error
#Key error

print("hello error")

while True:
    try:
     age = int(input("Enter your age = "))
     print("Your age is =",age/age)

    except ZeroDivisionError as error:
        print("enter valid age.",error)
    else:
        print("thanks for time!")
        break