a = int(input("Введите число: "))
almostZero = 1e-15
x = a
while abs(x - a/x)>almostZero:
    x = (a/x+x)/2.0
print("Квадратный корень: ", x)
