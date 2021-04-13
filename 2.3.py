# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def param (name,surname,year,city,email):
    return name+" "+surname+" "+year+" "+city+" "+email

info=param(name="Viktoria",surname="Token",year="2000",city="Kyiv",email="tom_crus@gmail.com")
print(info)