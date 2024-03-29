def check_point(x0, y0):
    in_cycle = (x0 - 1)**2 + y0**2 > 1**2 and (x0 - 1)**2 + y0**2 < 2**2
    in_rectangle = abs(x0 - 4) < 2 and abs(y0 - 2) < 3
    
    # Формирование и вывод результата
    if in_cycle and in_rectangle:
        print("yes yes")
    elif in_cycle:
        print("yes no")
    elif in_rectangle:
        print("no yes")
    else:
        print("no no")

# Пример ввода
x0, y0 = map(float, input("Введите координаты точки P (x0 y0): ").split())
check_point(x0, y0)
