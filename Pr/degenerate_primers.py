"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
import Dicts

primer1, primer2 = input('Введите первый праймер в формате IUPAC: '), input('Введите второй праймер в формате IUPAC: ') #запрос на введение двух праймеров.
# input 1: ATCGBDTTC
# input 2: GBDHKMRSV

def regular_shablon(primer1, primer2): #функция, которая преобразует праймер в формат, необходимый для подачи в регулярное выражение
    c = []
    d = []

    if primer1 == '' or primer2 == '':
        raise ValueError('Вы ввели всего один праймер')
    else:

        for x in primer1:
            if x in 'ATCGBDHKMNRSVWY':
                c.append(Dicts.PRIMER_DICT1[x])
            else:
                return ValueError('Неправильный формат записи вырожденного праймера')
        new_s1 = ''.join(c)

        for x in primer2:
            if x in 'ATCGBDHKMNRSVWY':
                d.append(Dicts.PRIMER_DICT2[x])
            else:
                return ValueError('Неправильный формат записи вырожденного праймера')
        new_s2 = ''.join(d)

        frame1 = int(50 - len(primer1) - len(primer2))
        frame2 = int(150 - len(primer1) - len(primer2))

        reg_shab = new_s1 + '([ATGC]' + '{' + str(frame1) + ',' + str(frame2) + '})' + new_s2

        return reg_shab

def find_amplicons (fasta, shablon):

    try:

        with open(fasta, "r") as file:
            filetext = file.read()
            matches = re.findall(shablon, filetext)
            #matches2 = re.findall(primer2, filetext)
        return matches

    except FileNotFoundError:
        print("Невозможно открыть файл")


shablon = regular_shablon(primer1, primer2)
print(shablon)

# print(type(reg_one))
# print('Праймер 1 преобразованный в регулярное выражение ', reg_one)
# print('Праймер 2 преобразованный в регулярное выражение ', reg_sec)

amplicons = find_amplicons('spades_scaffolds.fasta', shablon)
print(amplicons)
print(len(amplicons))
# print (len(amplicons1)) можно без len, тогда будет список
# print (len(amplicons2))



