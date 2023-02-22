print("Дз 12")
a = str(input())
b = a.split()
d = {}
for i in b:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

print("Дз 13")
dict_1 = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}
dict_2 = {}
for key, value in dict_1.items():
    for i in value:
        if i not in dict_2:
            dict_2[i] = [key]
        else:
            dict_2[i].append(key)
for key, values in dict_2.items():
    print(f"  '{key}': {values},")



print("Дз 14")
set_1 = {2, 243, 56, 456, 1342, 6, 5, 7}
set_2 = {54, 3456, 2, 6, 243, 453, 7}
print(len(set_1 ^ set_2))

