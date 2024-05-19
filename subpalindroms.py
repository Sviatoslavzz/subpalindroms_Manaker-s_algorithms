option = int(input("Введите 1 для ввода строки из консоли / введите 2 для загрузки из файла\n"))
if option == 1:
    s = input("Введите строку: ")
else:
    path = input("Введите путь к файлу: ")
    with open(path, "r") as file:
        s = file.read()
        s.strip('\n')

x = 257
p = 10 ** 9 + 7
h = [0]
x_list = [0]
res = 0
mul_x = 1
len_s = len(s)
for i in range(len_s):
    res = ((res * x) + ord(s[i])) % p
    h.append(res)
    mul_x = (mul_x * x) % p
    x_list.append(mul_x)


def string_compare(len_sub, start_1, start_2):
    return (h[start_1 + len_sub] + h[start_2] * x_list[len_sub]) % p == (
            h[start_2 + len_sub] + h[start_1] * x_list[len_sub]) % p


pal_odd = [0] * len_s
pal_even = [0] * len_s
l = 0
r = - 1
for i in range(len_s):
    min_side = min(i, len_s - 1 - i)

    if i <= r:
        counter = min(r - i, pal_odd[r - i + l])
    else:
        counter = 0

    while counter != min_side and string_compare(1, i - 1 - counter, i + 1 + counter):  # зайдем, начиная с 2-го символа
        counter += 1
    pal_odd[i] = counter

    if i + counter > r:
        l, r = i - counter, i + counter

l = 0
r = - 1
for i in range(len_s):
    min_side = min(i + 1, len_s - 1 - i)

    if i <= r:
        counter = min(r - i + 1, pal_even[r - i + l + 1])
    else:
        counter = 0

    # отдельная проверка четного палиндрома для 1-го символа
    if i == 0:
        if string_compare(1, i, i + 1):
            pal_even[i] = 1
    else:
        while counter != min_side and string_compare(1, i - counter, i + counter + 1):
            counter += 1
        pal_even[i] = counter

    if i + counter - 1 > r:
        l, r = i - counter, i + counter - 1

print(sum(pal_odd) + sum(pal_even) + len_s)
