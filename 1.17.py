pol = input("Введите обозначение клетки: ")
letter_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
letter_num = letter_to_num[pol[0]]
digit_num = int(pol[1])
if (letter_num + digit_num) % 2 == 0:
    print("black")
else:
    print("white")
