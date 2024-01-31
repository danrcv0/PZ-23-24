"""1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Элементы первого файла, присутствующие во втором:
Элементы второго файла, присутствующие в первом:
Количество элементов:
Количество отрицательных элементов:
Количество положительных элементов:
"""

import random

def Write():
    with open('file_1.txt', 'w') as file_1:
        for x in range(20):
            file_1.write(f'{random.randint(-20, 20)}\n')

    with open('file_2.txt', 'w') as file_2:
        for x in range(20):
            file_2.write(f'{random.randint(-20, 20)}\n')

def Processing():
        nums_1 = open('file_1.txt', 'r').read().split('\n')
        nums_2 = open('file_2.txt', 'r').read().split('\n')

        print(f'Элементы первого и второго файлов: {nums_1} {nums_2}')

        result = []
        for num_1 in nums_1:
            for num_2 in nums_2:
                if num_1 == num_2:
                    result.append(num_1)
        print(f'Элементы первого файла, присутствующие во втором: {result}')

        result = []
        for num_1 in nums_1:
            for num_2 in nums_2:
                if num_2 == num_1:
                    result.append(num_2)
        print(f'Элементы второго файла, присутствующие в первом: {result}')
        print(f'Количество элементов: {len(nums_1) + len(nums_2)}')

        negative = []
        positive = []
        for i in nums_1:
            try:
                if int(i) >= 0:
                    positive.append(int(i))
                if int(i) < 0:
                    negative.append(int(i))
            except:     pass


        for x in nums_2:
            try:
                if int(i) >= 0:
                    positive.append(int(i))
                if int(i) < 0:
                    negative.append(int(i))
            except:     pass

        print(f'Количество отрицательных элементов: {len(negative)}\nКоличество положительных элементов: {len(positive)}')


if __name__=="__main__":
    Write()
    Processing()
