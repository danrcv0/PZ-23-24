"""Дано число N (>1). Найти наибольшее из целых чисел К для которого сумма 1 + 2 + 3 + ... + K будет меньше или равна числу N"""


def Main(N):
    try:
        if int(N) > 1:
            number = int(N)
            while True:
                addititon = 0
                count = 0
                for x in range(number):
                    addititon+=count
                    count+=1

                if addititon <= int(N):
                    print(f'Наибольшее число - {number}\nСумма - {addititon}')
                    break
                
                else:
                    number = number - 1

        else:
            print('Число N больше 1!!!\nПопробуйте заново!')
            Main(N=input('Введите число: '))
    except Exception as e:
        print(f'Вы ввели неправильное число! {e} \nПопробуйте заново!')
        Main(N=input('Введите число: '))

if __name__ == '__main__':
    Main(N=input('Введите число: '))