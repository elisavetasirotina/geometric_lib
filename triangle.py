import math
def area(a, b, c):
    '''Принимает числа a,b,c, считает полупериметр треугольника и возвращает площадь треугольника'''
    p=(a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))



def perimeter(a, b, c):
    '''Принимает числа a,b,c, возвращает периметр треугольника'''
    return a + b + c
