from random import randint

N = 30
array = []
for i in range (N):
    array.append(int(randint(1, 100)))
array.sort()

print(array)
#число которое требуется найти

number = int(input())

#нижний индекс
low = 0
#верхний индекс
high = N-1

#как только нижний индекс станет больше на 1 верхнего цикл прекратится
while low <= high:
    #находится индекс середины массива
    mid = (low + high) // 2
    # Если искомое число меньше числа с индексом середины
    if number < array[mid]:
        # то нижняя граница сдвигается вправо
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:
        print('Id mid = ', mid)
else:
    print('Not namber array')
