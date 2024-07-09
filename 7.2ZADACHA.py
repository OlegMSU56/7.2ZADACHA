def custom_write(file_name, strings):
    strings_positions = {}
    for string in strings:
        file = open(file_name, 'a', encoding='utf-8')
        file.write(string + '\n')
        position = file.tell()
        strings_positions[(strings.index(string) + 1, position)] = string
        file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('7.2text.txt', info)
for elem in result.items():
  print(elem)