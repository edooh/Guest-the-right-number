import random
x= random.randint(1,7)
while x:
  a = int(input('enter a value = '))
  if a < x:
    print('too low')
  elif a>x:
    print('above the number')
  elif a ==x:
    print('you are right!')
    break