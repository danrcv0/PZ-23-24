"""Дан целочисленный список A размера N. Переписать в новый целочисленный
список B все четные числа из исходного списка (в том же порядке) и вывести размер
полученного список B и его содержимое."""



import random

def main(Q):
    try:
        if Q == 'y':
            A = []
            for x in range(random.randint(5,50)):
                A.append(random.randint(1,100))
            print(f'Список A -- {A}')

        if Q == 'n':
            A = input('ведите список чисел через пробел: ')
            A = A.split(' ')
        B = []
        count = 1
        for i in A:
            if int(i)%2 == 0:
                B.append(i)
                count+=2
            else:
                count+=2

        print(f'Список -- {B}\nДлинна -- {len(B)}')
    except:
        print('[error]- попробуйте заново!\n\n')
        main(Q=input('Хотите ли вы получить список рандомно? (y/n): '))

main(Q=input('Хотите ли вы получить список рандомно? (y/n): '))
