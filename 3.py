a = int(input("Введите целое число: "))
b = 0
c = 0

if a < 0:
    b=int(a)*-1
else:
    b=a
 
while b > 0:
    digit = b % 10
    b = b // 10
    c = c * 10
    c = c + digit  

if a < 0:
    c=int(c)*-1

print('Обратное число:', c)


