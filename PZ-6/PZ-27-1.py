
"""Дан список A размера N. Найти минимальный элемент из его элементов с четными
номерами: A2, A4, A6, ... ."""



import random


def main(Q):
    if Q == 'y':
        A = []
        for x in range(random.randint(5,50)):
            A.append(random.randint(1,100))
        print(f'Список А: {A}')

    if Q == 'n':
        A = input('Введите список числе  через пробел: ')
        A = A.split(' ')
        print(A)
    lst_result = []
    count = 0
    for x in range(int(len(A)/2)):
        lst_result.append(A[count])
        count+=2
    lst_result.pop(0)
    print(f'\nсписок с числами четных номеров -- {lst_result}\nминимальный элемент списка -- {min(lst_result)}')

main(Q=input('Хотите ли вы ввести список ранодомно? (y/n): '))
