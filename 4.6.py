# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
def first(fr,do):
    for el in count(fr):
        if el > do:
            break
        else:
            print(el)

cc=["r","o", "m", "a"]
def second(do1):
    с = 0
    for el in cycle(cc):
        if с > do1:
            break
        print(el)
        с += 1

first(fr=int(input("З якого числа будемо виводити? ",)), do=int(input("А до якого? ",)))
second(do1=int(input("До якого виводимо? ",)))
