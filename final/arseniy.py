from random import randint
balance = 200
print(balance)
name = input("как тебя зовут? ")
print("привет  " + name)
add = int(input("сколько ты вложишь на свой счет: "))
balance = balance + add
print("сумма вашего бюджета равна: " + str (balance))
products = ['пс 4', 'Нинтендо', 'Пк', 'Айфон', 'Пс 5']
tovar = input('Наличие какого товара вы хотите узнать: ')
if tovar in products:
 print('У нас есть- ', tovar)
if tovar == 'Айфон':
 balance = balance + 1000
elif tovar == 'Нинтендо':
 balance = balance + 500
elif tovar == "Пк":
 balance = balance + 500
elif tovar == 'Пс 5':
 balance = balance + 500
elif tovar == 'пс 4':
 balance = balance + 500

print('Будете брать?- ', tovar)
add = int(input("сколько ты выведешь из своего счета: "))
balance = balance - add
print("сумма вашего бюджета равна: " + str (balance))
answer = input ("Хочешь поддержать автора ")
if answer.upper() == 'ДА':
  print("спасибо- кидать сюда 4276 1000 2549 0365")
if answer.upper() == 'НЕТ':
  print("Ну и не надо")
print("Вот все наши продукты: айфон-1000$","Пк-500$","Нинтендо-200$","пс4-300$","пс5-800$")
