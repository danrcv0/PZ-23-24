
"""2. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3."""



import random
def Main():
    matrix = [[random.randint(-2, 2) for x in range(3)] for x in range(3)]
    print(f'{matrix[0]}\n{matrix[1]}\n{matrix[2]}')
    elem = int(input('Введите номер строки: '))
    matrix[0] = [i+3 for i in matrix[elem-1]]
    print(matrix[elem-1])

if __name__ =="__main__":
    Main()
