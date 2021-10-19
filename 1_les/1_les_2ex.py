number = int(input("Введите время в секундах: "))
hour = number // 3600
number = number - hour * 3600
minut = number // 60
number = number - minut * 60
secund = number
print("Your time: %.2d:%.2d:%.2d" % (hour, minut, secund))
