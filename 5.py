# Задайте число. Составьте список 
# чисел Фибоначчи, в том числе для 
# отрицательных индексов.ДОП
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

k=int(input('Введите число k - '))
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
fibonList = []
for i in range(k+1):
    fibonList.append(Fibonacci(i))
for j in range(-1,-k-1,-1):
    fibonList.insert(0,fibonList[1]-fibonList[0])
print(fibonList)