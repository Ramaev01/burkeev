melt = {
    'Sn': 232,
    'Zn': 420,
    'Fe': 1539,
    'Ni': 1455,
    'Si': 1415,
    'Be': 1287}
element1 = input("Первый элемент: ")
element2 = input("Второй элемент: ")
if element1 in melt and element2 in melt:
    difference = melt[element1]-melt[element2]
    print(f"Температура плавления {element1} на {abs(difference)} градусов {'выше' if difference > 0 else 'ниже'} чем у {element2} ")
else:
    if element1 not in melt:
        print(f"Элемент {element1} не найден")
    if element2 not in melt:
        print(f"Элемент {element2} не найден")
