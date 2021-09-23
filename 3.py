def average_earnings ():
    return int (summa / e)

poor_mans = []
summa = 0
e = 0
my_f = open("salary.txt", "r")
for line in my_f:
    a = line.find ('')
    b = line.find ('rub')
    c = line.find ('- ')
    d = line.find (' -')
    e += 1
    name = line [ 0 : d ]
    prize = int (line [ (c + 2): b] )
    summa += prize
    if (prize < 20000):
        poor_mans.append (name)

print (f'''Сотрудники, которые получают заработную плату меньше 20000 руб:
{ poor_mans }''')
print (f'''Средний доход на одного сотрудника :
{ average_earnings () } руб''')
