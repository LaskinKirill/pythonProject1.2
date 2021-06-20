last = input('Введите Фамилию ')
name = input('Имя ')
patronymic = input('Введите Отчество ')
full_names = [last, name, patronymic]
print(full_names[0] + ' ' + full_names[1] + ' ' + full_names[2])
short_names = [last, name[0], patronymic[0]]
print(short_names[0] + ' ' + short_names[1] + '.' + short_names[2] + '.')

str1 = str(input('Введите строку '))
print(str1)
s = 0
for n in str1:
    if n.isdigit():
        s += int(n)
        print(n)
print('Сумма цифр в строке равна: ', s)
