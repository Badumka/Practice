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


# Метод золотого сечения
def Golden_Section_Method(xmin, xmax, eps):
    iteration = 1.0
    print((" {0:.8s} || {1:.5s}  || {2:.8s} || {3:.5s}  || {4:.8s}").format("Итерация", "x_min", "f(x_min)", "x_max",
                                                                            "f(x_max)"))
    coefficient = (math.sqrt(5) - 1) / 2
    d = xmin + (xmax - xmin) * coefficient
    c = xmax - (xmax - xmin) * coefficient
    sc = f(c)
    sd = f(d)
    while (xmax - xmin) > eps:
        if (sd < sc):           #max <; min >
            xmax = d
            d = c
            c = xmax - (xmax - xmin) * coefficient
            sd = sc
            sc = f(c)
        else:
            xmin = c
            c = d
            d = xmin + (xmax - xmin) * coefficient
            sc = sd
            sd = f(d)
        iteration += 1
        print(("     {0:.0f}    || {1:.4f} || {2:.4f}   || {3:.4f} || {4:.4f}").format(iteration - 1, xmin,
                                                                                       f(xmin), xmax,
                                                                                       f(xmax)), eps)


Golden_Section_Method(xmin, xmax, 0.02)

# Шаг между точками
dx = 0.1

# Создадим список координат по оси X на отрезке [-x_min; x_max], включая концы
xlist = mlab.frange(x_min, x_max, dx)

# Вычислим значение функции в заданных точках
ylist = [f(x) for x in xlist]

# Нарисуем одномерный график
pylab.plot(xlist, ylist)
plt.grid(True)

# Покажем окно с нарисованным графиком
pylab.show()