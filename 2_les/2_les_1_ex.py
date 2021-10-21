my_list = [12, 12.12, "12", True, {12, 12}, [12, 12], (12, 12)]
el = 0
print(type(my_list[el]))
for el in my_list:
    print(f"Элемент {el} типа {type(el)}")
