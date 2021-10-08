x = int(input('Введите x: '))
if 0 >= x:
    int('x не может быть равен 0!')
    while 0 >= x:
        x = int(input('Введите x: '))
o = 3*(x*x*x*x)-5*(x*x*x)+2*(x*x)-x+7
print('━━━━━━━━━━━━━━━━━━━━━━━━')
print ('Ваш результат: ', (o))
exit