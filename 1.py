name = input ('Введите Ваше имя: ')
age = input ('Ваш возраст: ')
city = input ('Город: ')
lines = ["data"]
with open(r"my_data.txt", "w") as file:
    for  line in lines:
        file.write('Имя: ' + name + '\n')
        file.write('Возраст: ' + age + '\n')
        file.write('Город: ' + city + '\n')
        file.write((' ' * 80) + '\n')
        file.write(('=' * 80) + '\n')

                                                                                
