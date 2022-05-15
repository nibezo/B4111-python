from turtle import *
goto(0,0)
while True:
  print("Ты можешь рисовать на данные кнопки:")
  print("1- вперед, 2 - направо повернуть, 3 - налево повернуть,4 - выход")
  x =int(input(''))
  if x ==1:
    forward(30)
  elif x == 2:
    right(90)
  elif x == 3:
    left(90)
  else:
    break
 
