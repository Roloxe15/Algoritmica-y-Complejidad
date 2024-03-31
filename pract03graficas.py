import time
import numpy as np
import matplotlib.pyplot as plt
from pract03 import Iter2, Iter1, Recursivo



# Complejidad temporal
n = 1000
T = [[0], [0], [0]]
D = []

for i in range(n):
  D.append([0])

for i in range(n // 10, n, n // 10):

  t = time.time()
  Iter1(D)
  T[0].append(time.time() - t)


  t = time.time()
  Recursivo(D)
  T[1].append(time.time() - t)


  print(f'Iteración {i // 10000} de 100')

with plt.style.context('ggplot'):
    plt.plot(np.array(T[0]), label ='Mayoritario1$')

    plt.xticks(
        [    x               for x in range(0, 100, 10)],
       [f'${x} \cdot 10^7$' for x in range(0, 100, 10)])
    plt.xlabel(        '$n$', fontsize = 12)
    plt.ylabel('$T(n)$ en s', fontsize = 12)
    plt.title('Complejidad temporal')
    plt.legend()

plt.show()
