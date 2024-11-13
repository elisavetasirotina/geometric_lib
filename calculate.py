import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
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
    """Принимает числа a, b, c и возвращает периметр"
    "треугольника."""
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
            "Enter figure name, available are ['circle', 'square'," "'triangle']:\n"
        )

    while func not in ["perimeter", "area"]:
        func = input("Enter function name, available are ['perimeter', 'area']:\n")

        while len(size) != {
            "circle-perimeter": 1,
            "circle-area": 1,
            "square-perimeter": 1,
            "square-area": 1,
            "triangle-perimeter": 3,
            "triangle-area": 3,
        }.get(f"{func}-{fig}", 1):
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space\n"
                        "1 for circle and square\n"
                    ).split(),
                )
            )
    result = calc(fig, func, size)
    print(f"{func} of {fig} is {result}")
