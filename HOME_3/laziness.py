name = "Введите числа от 0 до 100"
a = int(input("Введите первое значение a:" ))
b = int(input("Введите второе значение b:" ))
c = int(input("Введите третье значение c:" ))

resalt = a > 0 and b > 0 and c > 0 and print('"Нет нулевых значений!!!"') 

resalt = a == 0 and b == 0 and c == 0 and print('"Введены все нули"')

if a > (b + c):
    print("a-b-c")
else:
    print("b+c-a")
    
if a > 50 and c > a:
    print("Вася")
elif a > 5 or b == 7 and c == 7:
    print("Петя")
else:
    print(a, b, c)