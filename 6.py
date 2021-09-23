quantity = 0



my_f = open("school_program.txt", "r")
for line in my_f:
    colon = line.find (': ')
    type_class = line.find ('(')
    subject = line [ 0 : colon ]
    print (subject)
    class_count = line.count ('(': 0)
    for i in range (class_count):
        
    
