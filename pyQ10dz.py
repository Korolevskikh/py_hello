# 10.	Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А ')
x1 = int(input())
y1 = int(input())
print('Введите координаты точки B ')
x2 = int(input())
y2 = int(input())
x = (x1-x2)**2
y = (y1-y2)**2
l = round((x+y)**(0.5), 2)

print(l)
