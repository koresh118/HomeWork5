summa = 0

string = input ('Введите набор чисел, разделённых пробелами: ')

print ('Записываем строку в файл...')
print ('Готово!')
out_f = open("string_digit.txt", "w")
out_f.write(string)
out_f.close()

print ('Открываем файл...')
my_f = open("string_digit.txt", "r")
content = my_f.read()
my_f.close()

print ('Считываем данные...')
space = content.find (' ')
space_count = content.count (' ', 0)

for i in range (space_count + 1):
    if (space < 0):
        digit = int (content)
        summa += digit
    else:
        digit = int (content [ 0 : space ])
        content = content [ (space + 1) : ]
        space = content.find (' ')
        summa += digit

print (f'Итак, сумма записанных в файл чисел составляет { summa }')
        
