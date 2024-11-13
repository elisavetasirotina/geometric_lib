import sys
import os
import unittest

script_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(script_dir, ".."))
sys.path.insert(0, project_dir)

# Теперь можно импортировать модули
import circle
import square
import triangle
from calculate import calc


class TestShapes(unittest.TestCase):
    # Тесты для окружности
    def test_circle_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [5]  # Радиус
        result = calc(fig, func, size)
        expected = circle.perimeter(5)
        self.assertEqual(result, expected)

    def test_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]  # Радиус
        result = calc(fig, func, size)
        expected = circle.area(5)
        self.assertEqual(result, expected)

    def test_circle_area_large(self):
        fig = "circle"
        func = "area"
        size = [100]  # Большой радиус
        result = calc(fig, func, size)
        expected = circle.area(100)
        self.assertEqual(result, expected)

    # Тесты для квадрата
    def test_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [4]  # Сторона
        result = calc(fig, func, size)
        expected = square.perimeter(4)
        self.assertEqual(result, expected)

    def test_square_area(self):
        fig = "square"
        func = "area"
        size = [4]  # Сторона
        result = calc(fig, func, size)
        expected = square.area(4)
        self.assertEqual(result, expected)

    def test_square_area_large(self):
        fig = "square"
        func = "area"
        size = [100]  # Большая сторона
        result = calc(fig, func, size)
        expected = square.area(100)
        self.assertEqual(result, expected)

    # Тесты для треугольника
    def test_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, 5]  # Стороны
        result = calc(fig, func, size)
        expected = triangle.perimeter(3, 4, 5)
        self.assertEqual(result, expected)

    def test_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]  # Стороны
        result = calc(fig, func, size)
        expected = triangle.area(3, 4, 5)
        self.assertEqual(result, expected)

    def test_triangle_area_large(self):
        fig = "triangle"
        func = "area"
        size = [100, 100, 100]  # Большие стороны
        result = calc(fig, func, size)
        expected = triangle.area(100, 100, 100)
        self.assertEqual(result, expected)

    def test_triangle_area_invalid(self):
        fig = "triangle"
        func = "area"
        size = [3, 4]  # Недостаточно сторон
        with self.assertRaises(TypeError):
            calc(fig, func, size)

    def test_triangle_area_invalid_sides(self):
        fig = "triangle"
        func = "area"
        size = [1, 1, 10]  # Невозможный треугольник
        with self.assertRaises(ValueError):
            calc(fig, func, size)

    # Тесты для некорректных фигур
    def test_invalid_shape(self):
        fig = "hexagon"
        func = "perimeter"
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_function(self):
        fig = "circle"
        func = "volume"
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_size(self):
        fig = "triangle"
        func = "area"
        size = [3, 4]  # Неверное количество параметров (должно быть 3)
        with self.assertRaises(TypeError):
            calc(fig, func, size)

    def test_invalid_size_large(self):
        fig = "circle"
        func = "perimeter"
        size = [1000]  # Очень большой радиус
        result = calc(fig, func, size)
        expected = circle.perimeter(1000)
        self.assertEqual(result, expected)

    # Дополнительные тесты
    def test_perimeter_all_shapes(self):
        fig = "circle"
        func = "perimeter"
        size = [7]
        result = calc(fig, func, size)
        expected = circle.perimeter(7)
        self.assertEqual(result, expected)

        fig = "square"
        func = "perimeter"
        size = [5]
        result = calc(fig, func, size)
        expected = square.perimeter(5)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
