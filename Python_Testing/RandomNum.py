import random
answer = random.randint(1,10)
while True:
   try:
     guess = int(input('Guess number between 1-10: '))
     if 0 < guess < 10:
       if guess == answer:
          print('You are genius!')
          break
     else:
      print('Number between 1-10')
   except ValueError:
    print('Enter number between 1-10')
    continue



 

     