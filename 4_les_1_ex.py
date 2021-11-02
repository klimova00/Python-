# Вариант без функции
# from sys import argv

# script_name, output_in_hours, rate_per_hour, prize = argv

# print("Output in hours: ", output_in_hours)
# print("Rate per hour: ", rate_per_hour)
# print("Prize: ", prize)

# wage = (int(output_in_hours) * int(rate_per_hour)) + int(prize)
# print(f"Wage = {wage}")

from sys import argv


def wage():
    try:
        print("Output in hours: ", argv[1])
        print("Rate per hour: ", argv[2])
        print("Prize: ", argv[3])
        output_in_hours, rate_per_hour, prize = map(float, argv[1:])
        print(f"Wage = {int(output_in_hours) * int(rate_per_hour) + int(prize)}")
    except ValueError:
        print('Enter 3 param!')


wage()
