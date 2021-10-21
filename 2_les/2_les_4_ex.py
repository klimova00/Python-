str = input("Введите слова через пробелы:")
count = 1
for el in str.split():
    print(f'Str № {count}: {el[:10]}')
    count +=1
