# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате
# чч:мм:сс.
# Используйте форматирование строк.
time = int(input('Input time in second please : ',))
 hour = time // 3600
minuts = ((time - (hour * 3600))//60)
second = ((time - (hour * 3600)- minuts * 60))
while hour > 24:
     hour = hour - 24
 print('%02d' %hour, ':','%02d' %minuts,':','%02d' %second)
