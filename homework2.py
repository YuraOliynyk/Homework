print("Дз 5")
a = int(input("Число"))
n = 0
min_value = a
max_value = a
par = 0
nepar = 0
suma = 0
while a > 0:
    n += 1
    if a < min_value:
        min_value = a
    if a > max_value:
        max_value = a
    if a % 2 == 0:
        par += 1
    if a % 2 != 0:
        nepar += 1
    if a > 0:
        suma += a
    a = int(input("Число"))
    if a == 0:
        break
avg = suma / n
print("Кількість чисел", n, "min_value", min_value, "max_value", max_value, "Кількість парних", par, "Кількість непарних", nepar, "Сумма", suma, "Середнє", avg)

print("Дз 6")
N = int(input())
a = 1
while a**2 <= N:
    print(a**2, end=" ")
    a = a + 1
