print("Дз 17")
a = int(input())
def expanded_form(num):
    if num <= 0:
        raise ZeroDivisionError("zero division")
    number = str(num)
    new_list = []
    for i in range(len(number)):
        if number[i] != "0":
            new_list.append(number[i] + "0" * (len(number) - (i + 1)))
    return "+".join(new_list)


print(expanded_form(a))

print("Дз 18")
a = int(input("Введіть число"))
def number_collaps(num):
    if num <= 0:
        raise ZeroDivisionError("zero division")
    number = str(num)
    if num <= 9:
        return num
    else:
        summa = sum(int(i)for i in number)
        return number_collaps(summa)


print(number_collaps(a))


print("Дз 19")
text = str(input("Введіть текст"))
def hash_tag_creator(text):
    if not text:
        raise AttributeError("text must be")
    if len(text) > 140:
        return False
    words = text.split()
    words1 = [a.capitalize() for a in words]
    words2 = "#" + "".join(words1)
    return words2


print(hash_tag_creator(text))



