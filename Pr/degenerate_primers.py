"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
import Dicts

one_primer, sec_primer = input('Введите первый праймер в формате IUPAC: '), input('Введите второй праймер в формате IUPAC: ') #запрос на введение двух праймеров.
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

def find_amplicons (fasta, primer1, primer2):

    try:
        if primer1 == '' or primer2 == '':
            print(ValueError('Вы ввели всего один праймер'))
        else:

            with open(fasta, "r") as file:
                filetext = file.read()
                matches1 = re.findall(primer1, filetext)
                matches2 = re.findall(primer2, filetext)
            return matches1, matches2


    except FileNotFoundError:
        print("Невозможно открыть файл")

reg_one = prim_convert(one_primer)
reg_sec = prim_convert(sec_primer)

# print(type(reg_one))
# print('Праймер 1 преобразованный в регулярное выражение ', reg_one)
# print('Праймер 2 преобразованный в регулярное выражение ', reg_sec)

amplicons1, amplicons2 = find_amplicons('spades_scaffolds.fasta', reg_one, reg_sec)
# print (len(amplicons1)) можно без len, тогда будет список
# print (len(amplicons2))



