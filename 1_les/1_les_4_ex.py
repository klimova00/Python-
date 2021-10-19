a = int(input("Введите число: "))
print(f"a = {a}")
count = 0
sk = a
while (sk != 0):
    sk = sk // 10
    count += 1
c = 10 ** (count - 1)
a1 = a // c
a = a % c

while (count > 0):
    prob = a // (10 ** (count - 2))
    a = a % (10 ** (count - 2))
    if (prob > a1):
        a1 = prob
    count -= 1
print(f"Старшая цифра: {a1}")
