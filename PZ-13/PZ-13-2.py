

"""2. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3."""



def Main():
    matrix = [[int(input('Введите первое эелемент: ')), int(input('Введите второй эелемент: ')), int(input('Введите третий эелемент: '))]]
    print(matrix)
    matrix[0] = [i+3 for i in matrix[0]]
    print(matrix)

if __name__ =="__main__":
    Main()