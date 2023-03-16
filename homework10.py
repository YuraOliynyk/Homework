print("Дз 22")
with open('file.txt', 'a') as file:
    file.seek(0)
    while True:
        line = input("Введіть рядок, або натисніть Enter, щоб закінчити введення: ")
        if not line:
            break
        file.write(line + '\n')
        print(line)