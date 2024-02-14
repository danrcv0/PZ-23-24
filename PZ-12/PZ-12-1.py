"""Вариант 27.
1.В последовательности их N чисел в первой ее половине найти
произведение элементов меньших 0.
"""



import random

def Main():
    lst = []
    for x in range(20):
        lst.append(random.randint(-20, 20))
    answer = 1
    count = 0
    for x in range(int(len(lst)/2)):
            if lst[count] < 0:
                answer = answer*lst[count]
                count = count+1
            else:
                count = count+1
    print(f'Сгенерированная последовательность чисел -- {lst}\nПроизведение отрицательных чисел -- {answer}')

if __name__ =="__main__":
    Main()
