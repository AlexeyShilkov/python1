# utf - 8

num = int(input('Введите целое положительное число: '))

max = num % 10

while (num // 10) != 0:
    if (num // 10) < 10:
        last_num = num // 10
    else:
        last_num = num % 10
    num = num // 10
    if last_num > max:
        max = last_num

print(f"Наибольшая цифра в данном числе: {max}")

