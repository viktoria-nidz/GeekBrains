# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
n = int(input('Введи ціле позитивне число:',))
max=0
while n>0:
    k =n % 10
    n=int(n/10)
    if max < k:
        max = k
print(max)
