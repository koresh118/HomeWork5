str_list = []

my_f = open("digits.txt", "r")

for line in my_f:
    a = line.find (' - ')
    numeral = (line [ 0 : a ])
    digit = (line [ (a + 3) :])
    numeral_rus = ''
    if (numeral == 'One'):
        numeral_rus = 'Один'
    elif (numeral == 'Two'):
        numeral_rus = 'Два'
    elif (numeral == 'Three'):
        numeral_rus = 'Три'
    elif (numeral == 'Four'):
        numeral_rus = 'Четыре'
    string = numeral_rus + ' - ' + digit
    str_list.append (string)

my_f.close ()

out_f = open("digits_rus.txt", "w")
out_f.writelines(str_list)
out_f.close()
