my_list = []
len_my_list = int(input("Введите длину списка: "))
for i in range(len_my_list):
    new_element = input(f"Введите {i} элемент списка: ")
    my_list.append(new_element)
print(f"Введённый my_list = {my_list}")
count = 1
while (count < len_my_list):
    my_list[count], my_list[count - 1] = my_list[count - 1], my_list[count]
    count += 2
print(f"Результирующий my_list = {my_list}")4
