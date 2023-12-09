



def main(A):
    try:
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
        main(A=input('Введите список чисел через пробел: '))

main(A=input('Введите список чисел через пробел: '))