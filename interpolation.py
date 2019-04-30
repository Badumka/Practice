import matplotlib.pyplot as plt
import function as fun
import numpy as np

x, y = fun.openFile('some.txt')
xa = np.array(x, dtype=float)           # np.array() создает массив из списков
ya = np.array(y, dtype=float)
x1 = np.linspace(np.min(xa), np.max(ya))
y1 = [fun.funLagranzh(xa, ya, i) for i in x1]
                                    # np.linspace() создает массив из чисел

plt.plot(x1, y1, 'green')
plt.scatter(x, y)
plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.legend(('Interpolation F(x)', 'F(x)'))
plt.grid(True)
plt.show()