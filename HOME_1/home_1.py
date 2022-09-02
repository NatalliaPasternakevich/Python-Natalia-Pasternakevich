text = "Не знаю, как там в Лондоне, я не была."\
" Может, там собака - друг человека."\
" А у нас управдом - друг человека!"
print(text)
text_1 = "Шаг 1 - Количество символов -"
print(text_1,(len(text)))
text_2 = "Шаг 2 - Развернутая строка -"
def reverse(text):
    return text[::-1]
print(text_2, reverse(text))
text_3 = "Шаг 3 - Каждое слово с большой буквы -"
print(text_3, text.title())
text_4 = "Шаг 4 - Весь текст прописными буквами -"
print(text_4, text.upper())
text_5 = "Шаг 5 - Число вхождений в строку -"
counter1 = text.count('нд')
counter2 = text.count('ам')
counter3 = text.count('о')
print("Шаг 5 - Число вхождений 'нд' -", counter1,  ",'ам' - ", counter2,",'o' - ", counter3,)
t = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
splitted = t.split(' ')
print('Шаг 6 - Собственное упражнение -','\n'.join(splitted))
s = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
def string_reverse(s):
    list = s.split () 
    return ' ' .join (list [:: - 1]) 
print ('Шаг 7 - Развернуть предложение -',string_reverse (s)) 