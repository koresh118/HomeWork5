content = ''
strings = content.count ('\n', 0)
words = content.count (' ', 0)

my_f = open("text.txt", "r")
content = str (my_f.read())
strings = (content.count ('\n', 0) + 1)
words = (content.count (' ', 0) + 2)
print(f'''Количество строк в файле - { strings }.
Количество слов - { words }''')
my_f.close()
