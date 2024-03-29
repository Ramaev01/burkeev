x = [1,3,4,7,8,9,10]
max_speed = 0
delta_t = 0.01
for i in range(1, len(x)):
    speed = (x[i] - x[i-1]) / delta_t
    if abs(speed) > max_speed:
        max_speed = abs(speed)
print("Максимальный модуль скорости частицы (нм/с):", round(max_speed, 2))