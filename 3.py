# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict
year=['winter','spring','summer','autumn']
year1={1:'winter',2:'spring',3:'summer',4:'autumn'}
a=int(input('Введіть місяць року: '))
if a==12 or a==1 or a==2:
    print(year[0])
    print(year1[1])
elif a==3 or a==4 or a==5:
    print(year[1])
    print(year1[2])
elif a==6 or a==7 or a==8:
    print(year[2])
    print(year1[3])
elif a==9 or a==10 or a==11:
    print(year[3])
    print(year1[4])
else:
    print('ОШИБОЧКА ВИЙШЛА')
