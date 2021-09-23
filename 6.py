
my_list = []

my_f = open("school_program.txt", "r")
for line in my_f:
    colon = line.find (': ')
    type_class = line.find ('(')
    subject = line [ 0 : colon ]
    num_string1 = line [ colon : type_class ]
    line = line [(type_class + 1) : ]
    type_class = line.find ('(')
    num_string2 = line [ 0 : type_class ]
    line = line [(type_class + 1) : ]
    type_class = line.find ('(')
    num_string3 = line [ 0 : ]
    num1 = ''
    num2 = ''
    num3 = ''
    for c in num_string1:
        if c.isdigit():
            num1 = num1 + c
            summ1 = int (num1)
            
    for c in num_string2:
        if c.isdigit():
            num2 = num2 + c
            summ2 = summ1 + int (num2)
        else:
            summ2 = summ1

    for c in num_string3:
        if c.isdigit():
            num3 = num3 + c
            summ3 = summ2 + int (num3)
        else:
            summ3 = summ2
    string = f'"{ subject }" : { summ3 }'
    my_list.append (string)

print (my_list)

        
    
