"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
import Dicts


def string_for_regular(primer, dict):
    c = []
    if primer == '':
        raise ValueError('Необходимо ввести два праймера')
    else:
        for x in primer:
            if x in 'ATCGBDHKMNRSVWY':
                c.append(dict[x])
            else:
                raise ValueError('Неправильный формат записи вырожденного праймера')
        new_s = ''.join(c)
    return new_s


def regular_shablon(primer1, primer2): #функция, которая преобразует праймер в формат, необходимый для подачи в регулярное выражение

    new_s1 = string_for_regular(primer1, Dicts.PRIMER_DICT1)
    new_s2 = string_for_regular(primer2, Dicts.PRIMER_DICT2)

    frame1 = int((50) - len(primer1) - len(primer2))
    frame2 = int((150) - len(primer1) - len(primer2))

    if frame1 > frame2 or frame1 < 0:
        raise ValueError('Недпустимые значения границ рида')

    reg_shab = new_s1 + '([ATGC]' + '{' + str(frame1) + ',' + str(frame2) + '})' + new_s2
    return reg_shab


def find_amplicons(fasta, shablon):

    try:

        with open(fasta, "r") as file:
            filetext = file.read()
            matches = re.findall(shablon, filetext)

        return matches

    except FileNotFoundError:
        print("Невозможно открыть файл")

primer1, primer2 = input('Введите первый праймер в формате IUPAC: '), input('Введите второй праймер в формате IUPAC: ') #запрос на введение двух праймеров.
# input 1: ATCGBDTTC
# input 2: GBDHKMRSV

shablon = regular_shablon(primer1, primer2)
print(shablon)

amplicons = find_amplicons('spades_scaffolds.fasta', shablon)
print(amplicons)
print(len(amplicons))





