
"""Дан список A размера N. Найти минимальный элемент из его элементов с четными
номерами: A2, A4, A6, ... ."""




def main(A):
        A = A.split(' ')
        lst_result = []
        count = 0
        for x in range(int(len(A)/2)):
            lst_result.append(A[count])
            count+=2
        print(f'\nсписок с числами четных номеров -- {lst_result}\nминимальный элемент списка -- {min(lst_result)}')

main(A=input('Введите список чисел через пробел: '))
