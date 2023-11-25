"""Дано число N (>0). Найти сумму чисел 1+ 1/2 + 1/3 + ... + 1/n"""


def Main(N):
    try:
        if int(N) > 0:
            number = 1
            cycle = 2
            for x in range(int(N)):
                number+=1/cycle
                cycle+=1
            print(number)

        else:
            print('Число N больше 0!!!\nПопробуйте заново!')
            Main(N=input('Введите число: '))
    except Exception as e:
        print(f'Вы ввели неправильное число! {e} \nПопробуйте заново!')
        Main(N=input('Введите число: '))

if __name__ == '__main__':
    Main(N=input('Введите число: '))