"""2.Составить генератор (yield), который переведет символы строки из нижнего
регистра в верхний."""




def Generator(strng):
    for i in strng:
        yield i.lower()

def rtrn(result):
    answer = ''
    for i in result:
        answer = f'{answer}{i}'
    return answer

if __name__ =="__main__":
    result = Generator(strng=input('Введите строку: '))
    print(rtrn(result=result))




