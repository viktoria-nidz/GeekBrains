# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    el=[a, b, c]
    big=max(el)
    el.remove(big)
    big2=max(el)
    return(big + big2)

print(my_func(2, 4, 1))
