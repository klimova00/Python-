month = int(input("Введите номер месяца: "))
list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]
my_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
if (month in list_winter):
    print(my_dict.get(1))
elif (month in list_spring):
    print(my_dict.get(2))
elif (month in list_summer):
    print(my_dict.get(3))
else:
    print(my_dict.get(4))
