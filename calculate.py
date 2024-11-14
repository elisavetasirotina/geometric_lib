import math
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


def area(a, b, c):
    """Принимает числа a, b, c, считает полупериметр треугольника и
    возвращает площадь."""
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    """Принимает числа a, b, c и возвращает периметр
    треугольника."""
    return a + b + c


def calc(fig, func, size):
    """
    Вычисляет периметр и площадь заданной фигуры.
    (Для круга - длину окружности и площадь).
    """
    figs = ["circle", "square", "triangle"]
    funcs = ["perimeter", "area"]

    assert fig in figs
    assert func in funcs

    # Проверка на отрицательные значения
    if any(s <= 0 for s in size):
        raise ValueError("Размеры не могут быть отрицательными или нулевыми")

    if fig == "circle" and func == "perimeter":
        return circle_perimeter(*size)
    elif fig == "circle" and func == "area":
        return circle_area(*size)
    elif fig == "square" and func == "perimeter":
        return square_perimeter(*size)
    elif fig == "square" and func == "area":
        return square_area(*size)
    elif fig == "triangle" and func == "perimeter":
        return triangle_perimeter(*size)
    elif fig == "triangle" and func == "area":
        return triangle_area(*size)



if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in ["circle", "square", "triangle"]:
        fig = input(
            "Enter figure name, available are ['circle', 'square', 'triangle']:\n"
        )

    while func not in ["perimeter", "area"]:
        func = input("Enter function name, available are ['perimeter', 'area']:\n")

    while True:
        size = list(
            map(
                int,
                input(
                    "Input figure sizes separated by space\n"
                    "1 for circle and square, 3 for triangle\n"
                ).split(),
            )
        )
        
        # Проверяем на отрицательные значения
        if any(i < 0 for i in size):
            print("Error: Sizes must be positive numbers. Exiting.")
            exit(1)

        # Проверяем на правильное количество параметров для каждой фигуры и функции
        if len(size) == {
            "circle-perimeter": 1,
            "circle-area": 1,
            "square-perimeter": 1,
            "square-area": 1,
            "triangle-perimeter": 3,
            "triangle-area": 3,
        }.get(f"{func}-{fig}", 1):
            break
        else:
            print("Error: Invalid number of dimensions for the selected figure.")

    result = calc(fig, func, size)
    print(f"{func} of {fig} is {result}")
