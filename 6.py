# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на |K| элементов вправо, если K – положительное и влево, если отрицательное.
# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N, во второй
# строке записаны N целых чисел Ai, а в последней – целое число K. (1 ≤ N ≤ 105, |K| ≤ 105, |Ai| ≤ 100).
# Выходные данные
# В выходной файл OUTPUT.TXT выведите полученную последовательность.

with open("input.txt") as inputFile:
    inputList = [row.strip() for row in inputFile]
N=int(inputList[0])
K=int(inputList[2])
mainList = inputList[1].split()
resultList = [0]*N
if K>=0:
    for i in range(N):
        if i-K>-N:
            resultList[i]=mainList[i-K]
        else:
            resultList[i]=mainList[i-K+N]
else:
    for j in range(N):
        if j-K<N:
            resultList[j]=mainList[j-K]
        else:
            resultList[j]=mainList[j-K-N]
with open("output.txt", "w") as outputFile:
    for k in range(len(resultList)):
        outputFile.write(str(resultList[k]) + ' ')