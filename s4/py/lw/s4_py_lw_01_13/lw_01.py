# задание 1
def sum_of_three():
    op1 = int(input("Первое число: "))
    op2 = int(input("Второе число: "))
    op3 = int(input("Третье число: "))
    print("Сумма: ", op1 + op2 + op3)

# задание 2
def triangle_area():
    leg1 = int(input("Длина первого катета: "))
    leg2 = int(input("Длина второго катета: "))
    print("Площадь: ", leg1 * leg2 / 2)

# задание 3
def apples():
    kid_count = int(input("Школьников: "))
    apples_count = int(input("Яблок: "))
    print("У каждого школьника: ", apples_count // kid_count)
    print("В корзинке осталось: ", apples_count % kid_count)

# задание 4
def watch():
    minutes = int(input("Минут с начала дня: "))
    print(f"Время на электронных часах: {minutes // 60 % 24}:{minutes % 60}")

# задание 5
def desks():
    class1 = int(input("Учеников в первом классе: "))
    class2 = int(input("Учеников во втором классе: "))
    class3 = int(input("Учеников в третьем классе: "))
    print("Необходимо парт: ", (class1 + class2 + class3) // 2)

# задание 6
def laces():
    row_distance = int(input("Элитное расстояние между элитными рядами: "))
    hole_distance = int(input("Элитное расстояние между элитными дырочками: "))
    holes_count = int(input("Элитное количество элитных дырочек в каждом элитном ряду: "))
    free_length = int(input("Элитная длина свободного элитного конца: "))
    print("Элитная необходимая длина элитных шнурков для элитных ботинок с элитной шнуровкой: ",
          hole_distance * 2 * (holes_count - 1) + row_distance * (2 * holes_count - 1) + free_length * 2)