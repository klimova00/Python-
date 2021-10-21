my_list = [7, 5, 3, 3, 2]
new_element = int(input("Введите новый элемент рейтинга"))
if (new_element in my_list):
    pos = my_list.index(new_element)
    count = my_list.count(new_element)
    my_list.insert(pos + count - 1, new_element)
else:
    my_list.append(new_element)
    my_list.sort()
    my_list.reverse()
print(my_list)
