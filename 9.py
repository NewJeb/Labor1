a1 = int(input('Введите a1: '))
b1 = int(input('Введите b1: '))
c1 = int(input('Введите c1: '))
d1 = int(input('Введите d1: '))
a2 = int(input('Введите a2: '))
b2 = int(input('Введите b2: '))
c2 = int(input('Введите c2: '))
d2 = int(input('Введите d2: '))
a3 = int(input('Введите a3: '))
b3 = int(input('Введите b3: '))
c3 = int(input('Введите c3: '))
d3 = int(input('Введите d3: '))
r = a1*b2*c3+b1*c2*a3+c1*a2*b3-c1*b2*a3-a1*c2*b3-b1*a2*c3
if r == 0:
    print('Переменная не может быть равна 0!')
    while r == 0:
        a1 = int(input('Введите a1: '))
        b1 = int(input('Введите b1: '))
        c1 = int(input('Введите c1: '))
        d1 = int(input('Введите d1: '))
        a2 = int(input('Введите a2: '))
        b2 = int(input('Введите b2: '))
        c2 = int(input('Введите c2: '))
        d2 = int(input('Введите d2: '))
        a3 = int(input('Введите a3: '))
        b3 = int(input('Введите b3: '))
        c3 = int(input('Введите c3: '))
        d3 = int(input('Введите d3: '))

r1 = d1*b2*c3+b1*c2*d3+c1*d2*b3-c1*b2*d3-d1*c2*b3-b1*d2*c3
r2 = a1*d2*c3*d1*c2*a3+c1*a2*d3-c1*d2*a3-a1*c2*d3-d1*a2*c3
r3 = a1*b2*d3+b1*d2*a3+d1*a2*b3-d1*b2*a3-a1*d2*b3-b1*a2*d3
x = r1/r
y = r2/r
z = r3/r
print('━━━━━━━━━━━━━━━━━━━━━━━━')
print('Ваш результат: ', int(x), int(y), int(z))
exit


