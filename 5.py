a = float(input('Введите a: '))
if 0 >= a:
    print('Сторона треугольника не может быть равна 0!')
    while 0 >= a:
        a = float(input('Введите a: '))
b = float(input('Введите b: '))
if 0 >= b:
    print('Сторона треугольника не может быть равна 0!')
    while 0 >= b:
        b = float(input('Введите b: '))
c = float(input('Введите c: '))
if 0 >= c:
    print('Сторона треугольника не может быть равна 0!')
    while 0 >= c:
        c = float(input('Введите c: '))
print('━━━━━━━━━━━━━━━')
s = a * b * c
print('Площадь ▲:', int(s))
p = a + b + c
print('Периметр ▲:', int(p))
exit