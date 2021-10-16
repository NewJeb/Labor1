import math
x = int(input('Введите x: '))
if 0 >= x:
    print('x не может быть равен 0!')
    while 0 >= x:
        x = int(input('Введите x: '))
b = int(input('Введите x: '))
if 0 >= b:
    print('x не может быть равен 0!')
    while 0 >= b:
        b = int(input('Введите b: '))
a = int(input('Введите a: '))
if 0 >= a:
    print('a не может быть равен 0!')
    while 0 >= a:
        x = int(input('Введите a: '))
w = math.sqrt(x**2 + b ) - (b**2 * math.sin(x+a)**3)/x
y = math.cos(x**3)**2-(x/math.sqrt(a**2+b**2))
print('━━━━━━━━━━━━━━━━━━━━━━━━')
print ('Ваш результат: ', int(w), int(y))