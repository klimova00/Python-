res_day = int(input("Введите результат в первый день: "))
km = int(input("Введите количество километров: "))
count = 1
while (res_day < km):
    res_day = res_day * 1.1
    count += 1
print(f"В {count} день спортсмен достиг результата - не менее {km} км")
