import random


def add_price_to_name():
    m = []
    with open('names.txt', 'r') as file:
        names = [name.rstrip() for name in file]
    for name in names:
        price = round(random.uniform(100.0, 2500.5),2)
        name_n_price_list = [name, price]
        m.append(name_n_price_list)

    return m

matrix = add_price_to_name()

for row_index, row in enumerate(matrix):
    for column_index, value in enumerate(row):
        names = matrix[row_index][0]
        price = matrix[row_index][column_index]

print(matrix)

print(names)
print("===!--_-_--_-_---!===")
print(price)
