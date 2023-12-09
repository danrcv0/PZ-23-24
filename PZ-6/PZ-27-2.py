




def main(A):
    try:
        A = A.split(' ')
        count = 1
        for x in range(int(len(A)/2)):
            print(int(A[count]))
            count+=2
    except:
        print('[error]-- попробуйте заново!\n\n')
        main(A=input('Введите список чисел через пробел: '))

main(A=input('Введите список чисел через пробел: '))