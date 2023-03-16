import random
print("Дз 20")

M = int(input("Введіть розмір матриці"))


def sort_matrix(M):
    if M < 6:
        raise ValueError("Невірне значення")

    random_numbers = [[random.randint(1, 50) for i in range(M)] for j in range(M)]
    summa_of_stolb = [sum(column) for column in zip(*random_numbers)]


    print("Несортована матриця")
    for row in random_numbers:
        for element in row:
            print("{:<4}".format(element), end="")
        print("")
    for q in summa_of_stolb:
        print("{:<4}".format(q), end="")


    summa_dict = {}
    for j in range(M):
        summa_dict[j] = summa_of_stolb[j]


    sorted_summa_dict = {}
    for i in range(M):
        min_key = min(summa_dict, key=summa_dict.get)
        sorted_summa_dict[min_key] = summa_dict.pop(min_key)


    sorted_numbers = [[random_numbers[i][j] for j in sorted_summa_dict.keys()] for i in range(M)]


    for j in range(M):
        if j % 2 == 0:
            for i in range(1, M):
                key_item = sorted_numbers[i][j]
                k = i - 1
                while k >= 0 and sorted_numbers[k][j] < key_item:
                    sorted_numbers[k + 1][j] = sorted_numbers[k][j]
                    k -= 1
                sorted_numbers[k + 1][j] = key_item
        else:
            for i in range(1, M):
                key_item = sorted_numbers[i][j]
                k = i - 1
                while k >= 0 and sorted_numbers[k][j] > key_item:
                    sorted_numbers[k + 1][j] = sorted_numbers[k][j]
                    k -= 1
                sorted_numbers[k + 1][j] = key_item



    print("\nСортована матриця")
    for row in sorted_numbers:
        for element in row:
            print("{:<4}".format(element), end="")
        print("")
    for q in sorted_summa_dict.values():
        print("{:<4}".format(q), end="")


sort_matrix(M)
print("Дз 21")

row = int(input('Введіть кількість рядків '))
col = int(input('Введіть кількість колонок '))

matrix_MN = [[random.randint(10, 51) for i in range(col)] for j in range(row)]

summa_row = []
for i in range(row):
    summ_row = 0
    for j in range(col):
        summ_row += matrix_MN[i][j]
    summa_row.append(summ_row)

summa_stolbets = []
for i in range(col):
    summ_stolbets = 0
    for j in range(row):
        summ_stolbets += matrix_MN[j][i]
    summa_stolbets.append(summ_stolbets)

for i in range(row):
    for j in range(col):
        print("{:<4}".format(matrix_MN[i][j]), end=" ")
    print("{:<4}".format(summa_row[i]))

for i in range(col):
    summ_stolbets = summa_stolbets[i]
    print("{:<4} ".format(summ_stolbets), end="")