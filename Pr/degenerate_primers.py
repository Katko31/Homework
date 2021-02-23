"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
import Dicts

one_primer, sec_primer = input(), input() #запрос на введение двух праймеров.
# input 1: ATCGBDTTCGG
# input 2: GBDHKMRSVW

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

reg_one = prim_convert(one_primer)
reg_sec = prim_convert(sec_primer)

#print(reg_primer2)
print(type(reg_one))
print(reg_one)
print(reg_sec)


try:

    with open('spades_scaffolds.fasta', "r") as file:
        filetext = file.read()
        matches1 = re.findall(reg_one, filetext)
        # matches2 = re.findall(reg_sec, filetext)
        print(matches1)
        # print(matches2)


except FileNotFoundError:
    print("Невозможно открыть файл")

# filetext = 'TTGGGGTAC'
# matches = re.findall(reg_primer1, )
# print(matches)


