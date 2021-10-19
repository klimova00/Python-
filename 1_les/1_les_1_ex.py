a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
oper = input('Enter the operation you want to perform (*, /, +, -)')
if oper == '*':
    print(f'{a} * {b} = ', a * b)
else:
    if oper == '/':
        print(f'{a} / {b} = ', a / b)
    else:
        if oper == '+':
            print(f'{a} + {b} = ', a + b)
        else:
            if oper == '-':
                print(f'{a} - {b} = ', a - b)
            else:
                print('Введена неправильная операция!')
