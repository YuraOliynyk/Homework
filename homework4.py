print("Дз 10")
a = []
counter = 0
while True:
    num = int(input("Введіть число"))
    if num == 0:
        break
    a.append(num)
for i in range(1, len(a)-1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        counter += 1
print(counter)


print("Дз 11")
b = []
while True:
    num = int(input("Введіть число"))
    if num == 0:
        break
    b.append(num)
k = int(input("Введіть індекс"))
b = b[:k] + b[k+1:]
print(b)
