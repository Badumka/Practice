# coding: utf8
import re
import matplotlib.pyplot as plt         # подключение библиотек

file = open('info.txt', 'r')
array = file.read()

for i in array.split('\n'):             # разделяет файлы на строки
    x, y = (re.split('\s+', i))         # разделяет переменную i на две: х и у
    x = float(x)
    y = float(y)
    plt.scatter(x, y, color='black')    # вывод черных точек
                                        # (plt.plot)-соединяет точки
plt.xlabel('X', fontsize=10)            # подписи координатных осей
plt.xlabel('Y', fontsize=10)
plt.grid(True)                          # сетка
plt.show()                              # вывод на экран

