'''
    9. Написать функцию, которая принимает как аргумент алфавит последовательности, а возвращает функцию
    получения статистики встречаемости символов в последовательности
'''

from collections import Counter

def get_statistic(alphabite): #ACTG
    def count_symbols(sequence):
        d = dict(Counter(sequence))
        for i in d.copy():
            if i not in alphabite:
                del d[i]
        return d
    return count_symbols


a = get_statistic('ACTG')
print(a('HGHHYU'))


