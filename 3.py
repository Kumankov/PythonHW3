# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

inputList = [1.1, 1.2, 3.1, 5, 10.01]
fractionalList =[0]*len(inputList)
for i in range(len(inputList)):    #создаем список дробных частей
    accurancy=len(str(inputList[i]))-len(str(inputList[i]).split('.')[0])
    fractionalList[i]=round(inputList[i] - int(inputList[i]),accurancy)
for j in range(len(fractionalList)-1,-1,-1): #удалаяем нули из списка дробных частей
    if fractionalList[j] == 0:
        fractionalList.pop(j)
print(max(fractionalList)-min(fractionalList))    
