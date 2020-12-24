'''5. Создать классы, описывающие биологические последовательности ДНК, РНК,
белков, наследующие от общего класса «последовательность».
Каждый класс должен иметь свойство алфавит, уметь возвращать название последовательности
(название гена или белка), саму последовательность, ее длину, статистику по использованию в ней
символов,
ее молекулярную массу, а также специфичные функции (возврат комплементарной последовательности,
транскрипция ДНК -> РНК, трансляция РНК -> белок)'''

'''
DNA ('A', 'T', 'G', 'C')
Комплиментарность ДНК-ДНК (A=T, G=C, T=A, C=G)

RNA ('A', 'U', 'G', 'C') 
Комплиментарность РНК-РНК (A=U, G=C, C=G, U=A)
Комплиментарность ДНК-РНК (A=U, G=C, C=G, T=A)

Aminoacids. 3 буквы РНК кодируют 1 аминокислоту. 
Phe = ('UUU', 'UUC')
Leu = ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG')
Ile = ('AUU', AUC', AUA')
Met(START) = ('AUG')
Val = ('GUU', 'GUC', 'GUA', 'GUG')
Ser = ('UCU', 'UCC', 'UCA', 'UCG')
Pro = ('CCU', 'CCC', 'CCA', 'CCG')
Thr = ('ACU', 'ACC', 'ACA', 'ACG')
Ala = ('GCU', GCC', 'GCA', GCG')
Tyr = ('UAU', 'UAC')
STOP = ('UAA', 'UAG', 'UGA')
His = ('CAU', 'CAC')
Gln = ('CAA', 'CAG')
Asn = ('AAU', 'AAC')
Lys = ('AAA', 'AAG')
Asp = ('GAU', 'GAC')
Glu = ('GAA', 'GAG')
Cys = ('UGU', 'UGC')
Trp = ('UGG')
Arg = ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG')
Ser = ('AGU', 'AGC')
Glu = ('GGU', 'GGC', 'GGA', 'GGG')

Молекулярная масса ДНК и РНК:
молекулярная масса одного нуклеотида – 345 г/моль;

Молекулярная масса белка:
Масса одной аминокислоты – 100. Чтобы узнать молекулярную массу белка, нужно умножить массу одной аминокислоты на их количество. 

Пример последовательности: 
>NC_011748.1 Escherichia coli 55989, complete genome
GTAAGTATTTTTCAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT
GTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAA
ATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTACACAACATCCATGAAACG
CATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGTACAGGAA
ACACAGAAAAAAGCCCGCACCTGACAGTGCGGGCTTTTTTTTCGACCAAAGGTAACGAGGTAACAACCAT
GCGAGTGTTGAAGTTCGGCGGTACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTG



'''
from collections import Counter
import Consts

class CreateSequence:
    def __new__(cls, name, sequence): #Dna --> RNA --> protein
        if 'U' in sequence:
            rna = RNA(name,sequence)
            prot = rna.get_protein()
            return None, rna, prot

        elif check_prot(sequence):
            return None, None, Protein(name, sequence)
        else:
            dna = DNA(name, sequence)
            rna = dna.get_transcript()
            prot = rna.get_protein()
            return dna, rna, prot


def check_prot(seq):
    for i in seq:
        if i in 'DEFHIKLMNPQRSVWY':
            return True
    return False

class Sequence: #класс-родитель, в который мы передаем последовательность
    MOLL_MASS = 345

    def __init__(self, n, s):
        self.name = n
        self.seq = s

    def alphabite(self):
        return 'abc'

    def get_name(self): # чтобы возвращалось название последовательности (гена)
        return self.name

    def get_seq(self):  # чтобы возвращалось сама последовательность
        return self.seq

    def get_len(self): # чтобы возвращалось длина последовательности
        return len(self)

    def __len__(self): # чтобы возвращалось длина последовательности, с использованием magic method
        return len(self.seq)

    def statist(self): # чтобы возвращалась статистика по использованным символам
        return dict(Counter(self.seq))

    def get_mol_mass(self):  # молекулярная масса последовательности
        return Sequence.MOLL_MASS * len(self)

    '''
     10. Добавить к классу последовательностей метод, который принимает в качестве аргумента функцию,
    задающую правила замены символов, и который заменяет по этому правилу символы в последовательности
    '''
    def changed(self, func):
        result = ''

        for l in self.seq:
            result += func(l)
        return self.__class__(self.name, result)

    '''
    11. Модифицировать метод из предыдущей задачи так, что функция с правилом замены принимает не только
        заменяемый символ, но и предыдущий
    '''


    def changed_2(self, func):
        result = ''

        for i in range(len(self.seq)):
            prev_letter = None
            if i > 0:
                prev_letter = self.seq[i - 1]

            cur_letter = self.seq[i]

            result += func(prev_letter, cur_letter)
        return self.__class__(self.name, result)




class DNA(Sequence):

    def alphabite(self): #свой алфавит (A,T,G,C)
        return 'A, T, G, C'

    def get_complimentary(self):
        compliment = ''
        for i in self.seq:
            compliment += Consts.DNA_DICT[i]
        return compliment

    def get_transcript(self):
        transcript = ''
        for i in self.seq:
            transcript += Consts.DNA_RNA_DICT[i]
        return RNA(self.name, transcript) #надо чтобы было видно, какую цепочку я получаю

    def __str__(self):
        return f'DNA gene name: {self.name}, sequence: {self.seq}'



class RNA(Sequence):

    def alphabite(self): #свой алфавит (A, U, G ,C)
        return 'A, U, G, C'

    def get_complimentary(self):
        compliment = ''
        for i in self.seq:
            compliment += Consts.RNA_DICT[i]
        return compliment

    def __str__(self):
        return f'RNA gene name: {self.name}, sequence: {self.seq}'

    def get_protein(self):
        protein = ''
        i = 0
        j = 3
        while j <= len(self.seq):
            if Consts.AMINOACID_DICT[self.seq[i:j]] != 'Stop':
                protein += Consts.AMINOACID_DICT[self.seq[i:j]]
                i += 3
                j += 3
            else:
                break
        return Protein(self.name, protein)


class Protein(Sequence):
    MOLL_MASS = 100

    def alphabite(self):
        r = set(Consts.AMINOACID_DICT.values())
        r.remove('Stop')
        return sorted(r)

    def get_mol_mass(self):
        return Protein.MOLL_MASS * len(self)

    def __str__(self):
        return f'Protein name: {self.name}, sequence: {self.seq}'


def func1(letter):  #написать другую функцию
    if letter == "C": return "N"
    else: return letter

def func2(prev, current):
    if current == 'A' and prev == "A": return 'N'
    else: return current



a,b,c = CreateSequence('>NC_011748.1', 'GTAAGTATTTTTCAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT')


print(a)
print(b)
print(c)

print(a.get_complimentary())
# print(a.get_transcript())
# print(b.get_transcript())
#
# print(c.alphabite())
# print(b.get_transcript())
#
# print(a.get_transcript())
#
#
#
# print(a)
# print(a.changed(func1))
# print(a.changed_2(func2))
