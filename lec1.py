# print('hello world')

# # типы данных и переменная
# # int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# value = 12345
# # print (type(a))
# # print(type(b))
# # print(type(value))

# s = 'Hello world'
# print(s) # вывод строки
# print(a, b, s)

# f = False
# print(f)

# list = [1,2,3] # строка
# print(list)

# list = ['1', '2', '3'] # столбцы
# print(list) 
# col = [1,2,3]
# print(col) 


# ввод и вывод данных

# print('Ведите a')
# a = float(input())

# print('Ведите b')
# b = float(input())

# print(a, '+', b, '=', a+b)


# Арифметические операции
# +,-,*,/,%,//,**
# () Сокращеные операции

# a = 1.3221654885
# b = 3
# c = round(a*b, 6) # значение после запятой говорит о числе знаков после запятой
# print(c)

# a = 3
# a *= 5
# print(a)

# ЛОгические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 'asd'
# b = 'asd'
# print(a==b)

# a = 1<3<5
# print(a)


# func = 1
# T = 4
# x = 123

# print(func<T>x)

# f = 1>2 or 4<6
# print(f)

# f = [1,2,3,4]
# print(f)
# print( 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)


# Управляющие конструкции
# if, if - else

# a = int(input('a = '))
# b = int(input('b = '))

# if a > b:
#     print(a)
# else:
#     print(b)

# Использование управляющих конструкций if, if-else, if-elif
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так вас ждал, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Как сделать зеркальное число:
# original = 5472
# inverted = 0
# while original !=0:
#     inverted = inverted*10+(original%10)
#     original //=10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит)')
# print(inverted)    

# Использование управляющих конструкций for:

# for i in range(1, 10, 2):
#     print (i**2)

# немного о строках

# text = 'съешь ещё этих французских булок'
# print(len(text))    #кол-во символов в тексте
# print('ещё'in text)     #есть ли слово ЕЩЁ в тексте - да
# print(text.isdigit())   # все ли значения в строке числа? - нет
# print(text.islower())   # все ли значения - символы нижнего регистра? - да
# print(text.replace('ещё', 'ЕЩЁ'))   # замена

# for c in text:
#     print(c)

# help(isinstance)

# списки: введение

# numbers = [1,2,3,4,5]
# print(numbers)

# numbers = list(range(1,6))
# print(numbers)
# print(f'{len(numbers)} len')
# numbers[0] = 10
# print(numbers)

# for i in numbers:
#     i *=2
#     print(i)
# print(numbers)

# numbers = [1,2,3,4,5]
# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(numbers)
# print(type(numbers))

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)    # red green blue

# for e in colors:
#     print(e*2)   # redred greengreen blueblue

# colors.append('gray')   # добавить в конец
# print(colors == ['red', 'green', 'blue', 'grey']) #True
# colors.remove('red')  # удалить
# print(colors)

# функции (как задавать):

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 3
print(f(arg))
print(type(f(arg)))    



