import circle
import square
import triangle


figs = ['circle', 'square','triangle']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
        '''
        Вычисляет периметр и площадь заданной фигуры(для круга-длину окружности и площадь).

        Args:
        fig(str): название фигуры.
        func(str): функция для вычисления.
        size (list): список параметров фигуры(длина стороны/длины сторон/радиус окружности)
        выводит периметр или площадь заданной фигуры(для круга-длину окружности и площадь) в консоль
        '''
	assert fig in figs
	'''Проверка на допустимость фигуры'''
	assert func in funcs
	'''Проверка на допустимость фигуры'''

	result = eval(f'{fig}.{func}(*{size})')
	'''вычисление периметра или площади фигуры(для круга площадь и длину окружности)'''
	print(f'{func} of {fig} is {result}')
	'''вывод результата'''

if __name__ == "__main__":
	func = ''
	'''инициализация переменной,содержащей название функции'''
	fig = ''
	'''инициализация переменной,содержащей название функции'''
	size = list()
	'''инициализация списка,содержащего параметры фигуры'''
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
		'''запрос названия фигуры'''
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
		'''запрос названия функции'''
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
		'''запрос параметров фигуры'''
	
	calc(fig, func, size)
	'''вызов функции'''



