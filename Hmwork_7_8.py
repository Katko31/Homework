'''
7.Написать генератор случайных дезоксинуклеотидов, нуклеотидов  и аминокислот.
'''
import Consts
import random
dna = sorted(set(Consts.DNA_DICT.values()))
rna = sorted(set(Consts.RNA_DICT.values()))
p = set(Consts.AMINOACID_DICT.values())
p.remove('Stop')
protein = sorted(p)

def get_deoxyribonucleotide(name):
    print(random.choice(dna))

def get_ribonucleotide(name):
    print(random.choice(rna))

def get_aminoacid(name):
    print(random.choice(protein))

name = input('Введите название для вашего нуклеотида: ')
get_deoxyribonucleotide(name)

'''
8.Написать генераторы случайных последовательностей с использованием random.choices/генераторов из предыдущего задания
фиксированной длины (1000 символов)/случайной длины в заданном диапазоне (от 10 до 1000 символов).
'''
def get_dna_seq(name):
    print(''.join(random.choices(dna, k = 1000)))

def get_rna_seq(name):
    print(''.join(random.choices(rna, k = 1000)))

def get_protein(name):
    print(''.join(random.choices(protein, k = 1000)))

get_protein(name)
