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


# Метод поперечного сечения
def Half_Division_Method(xmin, xmax):
    while (abs((xmin - xmax)) > 0.02):
        middle_point = (xmin + xmax) / 2
        if (f(middle_point + 0.01) > f(middle_point - 0.01)):   #min <; max >
            print("{0:.4f} || {1:.4f} || Правый".format(middle_point, f(middle_point)))
            xmin = middle_point

        else:
            print("{0:.4f} || {1:.4f} || Левый".format(middle_point, f(middle_point)))
            xmax = middle_point
    print("Интервал нахождения максимума / минимума функции: [{0:.4f} ; {1:.4f}]".format(xmin, xmax))


Half_Division_Method(xmin, xmax)

# Шаг между точками
dx = 0.1

# Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [f(x) for x in xlist]

# Нарисуем одномерный график
pylab.plot(xlist, ylist)
plt.grid(True)

# Покажем окно с нарисованным графиком
pylab.show()