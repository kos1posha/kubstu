lw = int(input("Номер лабы: "))

# лаба 01 вариант 02 : площадь прямоугольного треугольника
if lw == 1:
    from lw_01 import triangle_area
    triangle_area()

# лаба 02 вариант 02 : знак числа
if lw == 2:
    from lw_02 import sgn
    x = int(input('x: '))
    print(sgn(x))

# лаба 03 вариант 01 : последняя цифра числа
if lw == 3:
    from lw_03 import digit_last
    n = int(input('n: '))
    print(digit_last(n))

# лаба 04 вариант 08 : сумма факториалов
if lw == 4:
    from lw_04 import sum_of_factorials
    n = int(input('n: '))
    print(sum_of_factorials(n))

# лаба 05 вариант 03 : делаем срезы
if lw == 5:
    from lw_05 import slices
    string = input('string: ')
    print(slices(string))

# лаба 06 вариант 04 : утренняя пробежка
if lw == 6:
    from lw_06 import jog
    start = int(input('start: '))
    end = int(input('end: '))
    jog(start, end)

# лаба 07 вариант 11 : удалить элемент
if lw == 7:
    from lw_07 import remove
    lst = [int(i) for i in input().split(' ')]
    n = int(input('n: '))
    print(remove(lst, n))

# лаба 08 вариант 06 : числа Фибоначчи
if lw == 8:
    from lw_08 import fibonacci
    n = int(input('n: '))
    print(fibonacci(n))

# лаба 09 вариант 02 : снежинка
if lw == 9:
    from lw_09 import snowflake
    n = int(input('n: '))
    [print(' '.join(i)) for i in snowflake(n)]

# лаба 10 вариант 05 : кубики
if lw == 10:
    from lw_10 import kubiki
    borya = [int(i) for i in input().split(' ')]
    anya = [int(i) for i in input().split(' ')]
    [print(i) for i in kubiki(borya, anya)]

# лаба 11 вариант 02 : словарь синонимов
if lw == 11:
    from lw_11 import synonyms
    n = int(input('n: '))
    pairs = [[i for i in input().split(' ')] for _ in range(n)]
    dictionary = dict()
    for i in range(n): dictionary[pairs[i][0]] = pairs[i][1]
    word = input('word: ')
    print(synonyms(dictionary, word))

# лаба 12 вариант 23 : строки фиксированной длины
if lw == 12:
    from lw_12 import fixed_length
    path = input('path: ')
    fixed_length(path)

# лаба 13 вариант 22 : трапеция ромб квадрат
if lw == 13:
    from lw_13 import Point, Shape, LineSegment, Quadrangle, Trapezoid, Rhombus, Rectangle

    rect = Rectangle(2, 2, Point(2, 3))
    rhom =  Rhombus(2, 3, Point(2, 3))
    rect_quad = rect.to_quadrangle()
    rhom_quad = rhom.to_quadrangle()

    print(rect_quad)
    print(rhom_quad)

    # pts = [Point(2, 2), Point(2.5, 2.5), Point(4, 1), Point(3, 1),
    #       Point(2.75, 2.75), Point(3, 2), Point(2.5, 2), Point(3.75, 1.25), Point(3.75, 2.75),
    #       Point(1.5, 2.5), Point(0, 0), Point(2.5, 3.5), Point(5, 2)]
    #
    # for pt in pts:
    #    print(f"{rect_quad.is_include_point(pt)}:{rhom_quad.is_include_point(pt)}")

    print()

    for rhom_pt in rhom_quad.get_points():
        print(f"pt{rhom_pt}:intersect({rect_quad.is_intersect_point(rhom_pt)}):include({rect_quad.is_include_point(rhom_pt)})")

    print()

    print(f"{rect.is_include(rhom)}:{rect_quad.is_include_quadrangle(rhom_quad)}")
    print(f"{rect.is_intersect(rhom)}:{rect_quad.is_intersect_quadrangle(rhom_quad)}")
    print(f"{rhom.is_include(rect)}:{rhom_quad.is_include_quadrangle(rect_quad)}")
    print(f"{rhom.is_intersect(rect)}:{rhom_quad.is_intersect_quadrangle(rect_quad)}")
