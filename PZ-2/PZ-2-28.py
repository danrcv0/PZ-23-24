

def Main(N=input('кол-во секунд: ')):
    while True:
        try:
            print(f'Кол-во минут, прошедших с начала последнего часа: {int((int(N)/60)%60)}')
            break
        except:
            print('Что-то пошло не так, попробуйте еще раз!')

if __name__ == "__main__":
    Main()
