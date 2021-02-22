"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
import Dicts

degenerate_primer1, degenerate_primer2 = input(), input() #запрос на введение двух праймеров.


def prim_convert(degenerate_primers): #функция, которая преобразует праймер в формат, необходимый для подачи в регулярное выражение
    c = []

    for x in degenerate_primers:
        if x in 'ATCGBDHKMNRSVWY':
            c.append(Dicts.PRIMER_DICT[x])
        else:
            return ValueError('Неправильный формат записи вырожденного праймера')
    new_s = ''.join(c)
    return new_s

# def find_amplicons(fasta, primer1, primer2):
#
#     try:
#
#         with open(fasta, "r") as file:
#             filetext = file.read()
#             matches1 = re.findall(primer1, filetext)
#             matches2 = re.findall(primer2, filetext)
#
#
#     except FileNotFoundError:
#         print("Невозможно открыть файл")

reg_primer1 = prim_convert(degenerate_primer1)
# reg_primer2 = prim_convert(degenerate_primer2)

#print(reg_primer2)
print(type(reg_primer1))
print(reg_primer1)


try:

    with open('spades_scaffolds.fasta', "r") as file:
        filetext = file.read()
        matches = re.findall(reg_primer1, filetext)
        print(matches)

except FileNotFoundError:
    print("Невозможно открыть файл")

# filetext = 'TTGGGGTAC'
# matches = re.findall(reg_primer1, )
# print(matches)

# DACGT