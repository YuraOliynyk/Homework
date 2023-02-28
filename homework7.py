print("Дз 16")
print("A")
h = int(input("Введить висоту фігури: "))

for i in range(h):
    for x in range(2 * h - 1):
        print('*' if x == h-1-i or x == h-1+i or i == h-1 else ' ', end=' ')
    print()

print("B")
h = int(input("Введить висоту фігури: "))

for i in range(h):
    for x in range(h*2-1):
        if x >= h - 1 - i and x <= h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print("C")
h = int(input("Введить висоту фігури: "))

for i in range(h):
    for x in range(h*2-1):
        if x >= h-1-i and x <= h-1+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

for i in range(h-2, -1, -1):
    for x in range(h*2-1):
        if x == h-1-i or x == h-1+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print("D")
h = int(input("Введить висоту фігури: "))

for i in range(h):
    for x in range(h * 2 - 1):
        if x >= h - 1 - i and x <= h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()


for i in range(h - 2, - 1, - 1):
    for x in range(h * 2 - 1):
        if x == h - 1 - i or x == h - 1 + i or x == h * 2 - 2 - x:
            print('* ', end='')
        else:
            print('  ', end='')
    print()


