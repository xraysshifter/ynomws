import random

def add_price_to_name():
    m = []
    with open('names.txt', 'r') as file:
        names = [name.rstrip() for name in file]
    for name in names:
        price = round(random.uniform(100.0, 2500.5),2)
        name_n_price_list = [name, price]
        m.append(name_n_price_list)

    print(m)

add_price_to_name()
