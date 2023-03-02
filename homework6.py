print("Дз 15")
a = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
    ]


for i in a:
    f = i[2] * i[3]
    if f < 100:
        f += 10
    print(f'Order:{i[0]}, \t , Price:{round(f,2)}')
