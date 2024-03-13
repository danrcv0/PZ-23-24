
"""Вариант 27.
1. В матрице найти среднее арифметическое положительных элементов, кратных 3.
"""

import random
def Main():
   matrix = [[random.randint(-6,6) for x in range(3)] for x in range(3)]
   print(matrix)
   elem = [[i for i in row if i > 0 and i % 3 == 0 ] for row in matrix]
   print(sum([sum(i) for i in elem])/len([i for i in [sum(i) for i in elem] if i>0]))

if __name__ == '__main__':
    Main()
