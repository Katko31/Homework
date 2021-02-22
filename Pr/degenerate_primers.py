"""
Домашнее задание1.Написать скрипт на Python, который представляет пару вырожденных праймеров в виде
регулярного выражения и ищет ампликоныв референсномгеноме.Геномзаписан в файл в формате FASTA.
Предусмотреть обработку исключений программы
"""
import re
import Consts
#пример праймера AC(G/T)T(T/A)GGG(G/A)C
degenerate_primer1, degenerate_primer2 = input(), input() #запрос на введение двух праймеров. Пример AC(G/T)T(T/A)GGG(G/A)C


def prim_convert(degenerate_primers): #функция, которая преобразует праймер в формат, необходимый для подачи в регулярное выражение
    c = []

    for x in degenerate_primers: #заменяю символы АТГЦ на комплиментарные, и знак / на |
        if x in '()':
            c.append(x)
        elif x in '/':
            c.append('|')
        elif x in 'ACGT':
            c.append(Consts.DNA_DICT[x])
        else:
            return ValueError('Неправильный формат записи вырожденного праймера')
    new_s = ''.join(c)
    #if len(new_s) != len(degenerate_primers):
     #   raise ValueError('Неправильный формат записи вырожденного праймера')
    if len(re.findall(r'\(\w\|\w\)', new_s))==int(len(re.findall(r'[\(\)\/]', degenerate_primers)))/3: #это проверка на правильное количество открытых и закрытых скобочек, а также наличие знака | , если есть скобочки. AC(GT)T(TA)GGG(G/A)C что-то такое должно отбраковаться, как неправильный вариант
        return new_s
    else:
        raise ValueError('Неправильный формат записи вырожденного праймера')


reg_primer1 = 'r' + '\'' + prim_convert(degenerate_primer1) + '\'' #это максимально корявая попытка впихнуть переменную в регулярное выражение. По-другому у меня не выходит
#reg_primer1 = prim_convert(degenerate_primer1)
#reg_primer2 = prim_convert(degenerate_primer2)
#print(reg_primer2)
print(reg_primer1)


try:

    with open("spades_scaffolds.fasta", "r") as file: #это открытие фаста файла

        for line in file:
            re.findall(reg_primer1, file.readlines())  #это поиск подстроки в строке


except FileNotFoundError:
    print("Невозможно открыть файл")
