"""Составить программу, в которой функция генерирует четырехзначное
 число и определяет, есть ли в числе одинаковые цифры."""




import random

def main():
    number = str(random.randint(1000,9999))
    lst = [number[0],number[1],number[2],number[3]]
    for i in lst:
        lst.remove(i)
        try:    
            lst.remove(i)
            print(f'В числе {number} присутствуют одинаковые символы...')
            break
        except: 
            print(f'В числе {number} отсутствуют одинаковые символы...')
            break
            
main()