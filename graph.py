import re
import matplotlib.pyplot as plt         # подключение библиотек

myfile = open('info.txt', 'r')          # открывает файл только для чтения
array = myfile.read()                   # читает содержимое файла

for i in array.split('\n'):             # разделяет файлы на строки
    x, y = (re.split('\s+', i))         # разделяет переменную i на две: х и у
    x = float(x)
    y = float(y)
    plt.scatter(x, y, color='black')    # выводит черные точки
                                        # (plt.plot)-соединяет точки
plt.xlabel('X', fontsize=10)            # подписи координатных осей
plt.ylabel('Y', fontsize=10)
plt.grid(True)                          # выводит сетку
plt.show()                              # выводит график на экран
