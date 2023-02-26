
# Q1: Напишите программу, которая принимает на входе 
# два числа и проверяет, является ли одно число квадратом
# другого.

# print('Введите a ')
# a = int(input())
# print('Введите b ')
# b = int(input())
# if a**2 == b:
#     print('да')
# elif b**2 == a:
#     print('да')
# else:
#     print('нет')    

# Q1/1	Напишите программу, которая считывает длины 
# катета и высоты в прямоугольном треугольнике и выводит
# его площадь. Каждое число записывается с новой строки

# print('Введите h ')
# h = int(input())
# print('Введите b ')
# b = int(input())
# S = h*b/2   # print(f'S={1/2*h*b}')
# print(S)

# Q1/2: Для подготовки к экзамену Рон каждый день учит х заклинаний, а Гермиона
#  на у заклинаний больше. Сколько заклинаний они выучат вместе через n дней?
# В первой строке вводится х – количество заклинаний, которые учит Рон.
# Во второй строке у – на сколько заклинаний больше учит Гермиона.

# print('Введите x ')
# x = int(input())
# print('Введите y ')
# y = int(input())
# print('Введите n ')
# n = int(input())
# res = (x+x+y)*n
# print(res)


# Q2: Напишите программу, которая на вход принимает 5 чисел и находит 
# максимальное из них

# print('Введите a ')
# a = int(input())
# print('Введите b ')
# b = int(input())
# print('Введите c ')
# c = int(input())    
# print('Введите d ')
# d = int(input())
# print('Введите e ')
# e = int(input())  
# mx = max(list([a,b,c,d,e]))
# print(mx)

# Пробуем задать ряд с консоли
# print('Введите a, b, c, d, e ')
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# res = list([a,b,c,d,e])
# print(res)

# Пробуем задать ряд с консоли
# res = list(map(int, input().split()))
# print(max(res))     #Ввод данных через TAB!!!!!


# Q3: Напишите программу, которая на вход будет 
# принимать число N, а на выходе выдавать от –N до N

# print('Введите N ')
# N = int(input())
# res = list(range(-N, N+1))

# print(res)

# Q4: Напишите программу, которая будет принимать на вход дробь,
# и показывать первую цифру дробной части числа

# a = float(input())
# res = int((a*10)%10)
# if res == 0:
#     print('нет')
# else:
#     print(res)

# Q5: Напишите программу, которая будет принимать на вход число, и будет проверять, кратно ли оно
# 5, 10 или 15, но не 30

print('Введите N ')
N = int(input())
if N%5 == 0 and (N%10 == 0 or N%15 == 0) and N%30 != 0:
    print('да')
else:
    print('нет')

echo "# py_hello" >> README.md 
git init 
git add README.md 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/Korolevskikh/py_hello.git
 git push - ты главный