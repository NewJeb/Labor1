h = float(input('Введите час: '))
if 0 >= h or h >= 12:
  print('Число ≤ 0 & 12 ≤ Число')
while 0 >= h or h >= 12:
  h = float(input('Введите час: '))
m = float(input('Введите минуты: '))
if 0 >= m or m >= 61:
  print('Число ≤ 0 & 61 ≤ Число')
while 0 >= m or m >= 61:
  m = float(input('Введите минуты: '))
s = float(input('Введите секунды: '))
if 0 >= s or s >= 61:
  print('Число ≤ 0 & 61 ≤ Число')
while 0 >= s or s >= 61:
  s = float(input('Введите секунды: '))
s = h * 3600 + m * 60 + s
u = 360 * s / 12 / 3600
print('Угол ⌚:', int(u), 'градусов')
exit