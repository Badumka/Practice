import re

def openFile(name):
    a = []
    b = []
    file = open(name, 'r')
    strings = file.read()

    for string in strings.split('\n'):
        x, y = (re.split('\s+', string))
        a.append(float(x))
        b.append(float(y))
    return a, b

def funLagranzh(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z
