# Общее описания решения
Данный проект-библиотека на языке Python, которая позволяет вычислять периметр и площадь геометрических фигур(треугольник квадрат), а также площадь круга и длину окружности.


# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Описание каждой функции с примерами вызова

## calculate
Выводит результат, ничего не возвращает

 ## triangle
area:
Возвращает площадь треугольника с заданными сторонами
a, b, c = 3, 4, 5
area(a, b, c) = 6.0

perimeter:
Возвращает периметр треугольника с заданными сторонами
a, b, c = 3, 4, 5
perimeter(a, b, c) = 12

## square
area:
Возвращает площадь квадрата с заданной стороной
a = 3
area(a) = 9

perimeter:
Возвращает периметр квадрата с заданной стороной
a = 3
perimeter(a) = 12

## circle
area:
Возвращает площадь круга с заданным радиусом
a = 3
area(a) = 28.274333882308138

perimeter:
Возвращает длину окружности с заданным радиусом
a = 3
perimeter(a) = 18.84955592153876

# Изменения с хэщами коммитов
<ad22f9288411df0ac19d23e7d88b47ad87c96514> исправлен файл triangle.py
<0fa162813b901cbecfd84738f941ff950ba53da9> исправлен файл square.py
<7caa185204031429c0746f8d0e56fa41c6c93cc4> исправлен файл circle.py
<b5b0fae727ca72c317c383b39c0af73d6adcd81c> (origin/develop, develop) L-04: Update docs for calculate.py
<d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71> L-04: Add calculate.py
<51c40ebfd0e0b65f52fe5e54740cbb038e492db3> L-04: Doc updated for triangle
<d080c7888b81955bad2ed78d58ad910526b5132a> L-04: Triangle added
<d078c8d9ee6155f3cb0e577d28d337b791de28e2> (origin/main, origin/HEAD, main) L-03: Docs added
<8ba9aeb3cea847b63a91ac378a2a6db758682460> L-03: Circle and square added



