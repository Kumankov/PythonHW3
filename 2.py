# Напишите программу, которая найдёт 
# произведение пар чисел списка. Парой 
# считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

inputList = [2,3,4,5,6]
if len(inputList)%2:
    count = int(len(inputList)/2)+1
else:
    count = int(len(inputList)/2)
print(count)
product=[0]*count
for i in range(count):
    product[i]=inputList[i]*inputList[-(i+1)]
print(product)    