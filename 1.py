n = int(input("Введите число: "))
s = str(n) 
l = len(s)
for i in range(l//2):
    if s[i] != s[-1-i]: 
       print("False")
       break
else:
    print("True")
