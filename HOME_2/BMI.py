a = int(input("Введите ваш вес (кг):"))
b = int(input("Введите ваш рост(см):"))
bmi = round(a/(b/100)**2)
print('Ваш индекс массы тела:',bmi)
print(str(16),"="*(bmi-16),"|","="*(32-bmi),str(32),sep='')

