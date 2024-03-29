room = int(input("Введите номер квартиры: "))
x = room % 8
a = (room // 8) + 1
if (room % 8 ) == 0:
    x = 8
    a = room // 8
print("Этаж: ",x)
print ("Подъезд: ",a)