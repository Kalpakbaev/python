
#Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |
number = int (input("Введите трехзначное число: "))
if number > 999:
     print('Введите корректное число!:')
if number < 100:
     print('Введите корректное число!:') 
else:
    summa = 0
    while number > 0:
         x = number % 10
         number = number // 10
         summa = summa + x

print("Сумма цифер введенного числа равно = " , summa)          
    
