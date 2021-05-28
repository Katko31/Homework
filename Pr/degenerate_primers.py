"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
from Pr.Dicts import PRIMER_DICT1, PRIMER_DICT2


def string_for_regular(primer, dic):
    """Функция преобразует из формата IUPAC в формат, который нужен для регулярного выражения"""
    c = []
    if primer == '':
        raise ValueError('Необходимо ввести два праймера')
    else:
        for x in primer:
            if x in 'ATCGBDHKMNRSVWY':
                c.append(dic[x])
            else:
                raise ValueError('Неправильный формат записи вырожденного праймера')
        new_s = ''.join(c)
    return new_s


def regular_shablon(primer1, primer2):
    """функция, которая преобразует праймеры в формат, необходимый для подачи в регулярное выражение"""
    new_s1_forward = string_for_regular(primer1, PRIMER_DICT1)
    new_s2_forward = string_for_regular(primer2, PRIMER_DICT2)

    new_s1_reverse = string_for_regular(primer1, PRIMER_DICT2)
    new_s2_reverse = string_for_regular(primer2, PRIMER_DICT1)

    reg_shab_reverse = f'{new_s1_reverse}.*{new_s2_reverse}'
    reg_shab_forward = f'{new_s1_forward}.*{new_s2_forward}'

    print(new_s1_forward)
    print(new_s2_forward)
    print(reg_shab_forward)
    print(reg_shab_reverse)

    return reg_shab_forward, reg_shab_reverse


def find_amplicons(fasta, shablon):
    """ Функция ищет подстроку (шаблон) в файле фаста и возвращает массив с последовательностями"""
    try:

        with open(fasta, "r") as file:
            filetext = file.read()
            matches = re.findall(shablon, filetext)

        return matches

    except FileNotFoundError:
        print("Невозможно открыть файл")


if __name__ == "__main__":

    primer1, primer2 = input('Введите первый праймер в формате IUPAC: '),\
                       input('Введите второй праймер в формате IUPAC: ') # запрос на введение двух праймеров.
    # input 1: ATCGBDTTC развернуть
    # input 2: GBDHKMRSV
    # primer1, primer2 = 'ACBD', 'GBDH'
    shablon_forward, shablon_reverse = regular_shablon(primer1, primer2)

    amplicons1 = find_amplicons('/home/kate/PycharmProjects/Homework/Pr/spades_scaffolds.fasta', shablon_forward)
    amplicons2 = find_amplicons('/home/kate/PycharmProjects/Homework/Pr/spades_scaffolds.fasta', shablon_reverse)
    print(len(amplicons1))
    print(len(amplicons2))






