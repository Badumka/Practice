# Подключение библиотек
import math
import pylab
import matplotlib.pyplot as plt
from matplotlib import mlab

# Определение границ
xmin = 2.2
xmax = 4.4

# Функции:
# max
f = lambda x: (x ** xmin) * math.sin(xmax * x)
# f = lambda x: ((math.e ** (xmin * x)) * (math.cos(xmax * x)))
# f = lambda x: (1 - math.fabs(xmin) * (x ** 2)) * math.atan(1 + math.fabs(xmax) * (x ** 2))
# min
# f = lambda x: (x ** 2) + (xmin * (math.e ** xmax) * x)
# f = lambda x: (x ** 4) + math.atan(xmax * x)
# f = lambda x: xmax * x + (math.e ** (abs(x - xmin)))

number_of_iterations = int(input(" Введите количество итераций: "))


# Число Фибоначчи
def Fibonacci(n):
    return int(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5)))


print((" {0:.8s} || {1:.5s}  || {2:.8s} || {3:.5s}  || {4:.8s}").format("Итерация", "x_min", "f(x_min)", "x_max",
                                                                        "f(x_max)"))

# Метод Фибоначчи
def Fibonacci_Method(xmin, xmax, iteration=0):
    if (iteration == number_of_iterations): return
    x_lhs = xmin + (((xmax - xmin) * Fibonacci(number_of_iterations - iteration - 1)) / Fibonacci(
        number_of_iterations - iteration + 1))
    x_rhs = xmin + (((xmax - xmin) * Fibonacci(number_of_iterations - iteration)) / Fibonacci(
        number_of_iterations - iteration + 1))
    if (f(x_lhs) < f(x_rhs)):     #min >; max <
        print(("     {0:.0f}    || {1:.4f} || {2:.4f}   || {3:.4f} || {4:.4f}").format(iteration + 1, x_lhs,
                                                                                       f(xmin), x_rhs,
                                                                                       f(xmax)))
        Fibonacci_Method(x_lhs, xmax, iteration + 1)
    else:
        print(("     {0:.0f}    || {1:.4f} || {2:.4f}   || {3:.4f} || {4:.4f}").format(iteration + 1, x_lhs,
                                                                                       f(xmin), x_rhs,
                                                                                       f(xmax)))
        Fibonacci_Method(xmin, x_rhs, iteration + 1)


Fibonacci_Method(xmin, xmax)

# Шаг между точками
increment = 0.01

# Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(xmin, xmax, increment)

# Вычислим значение функции в заданных точках
ylist = [f(x) for x in xlist]

# Нарисуем одномерный график
pylab.plot(xlist, ylist)
plt.grid(True)

# Покажем окно с нарисованным графиком
pylab.show()