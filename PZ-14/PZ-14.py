"""Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
год и поместить ее в новый текстовый файл."""





import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

match = re.search(r'1857 год(.*?)\d{4} год', text, re.DOTALL).group(1).strip()
try:
    with open('result.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(match)
    print("Информация за 1857 год была успешно извлечена!")
except:
    print("Информация за 1857 год не найдена.")