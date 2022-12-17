# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal=int(input('Введите десятичное число - '))
quotient=decimal
result =''
while quotient>0:
    remainder =str(quotient%2)
    result=remainder+result
    quotient=int(quotient/2)
print(result)
