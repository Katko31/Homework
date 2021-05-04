"""
 Написать программу, которая принимает в качестве параметра
размер k-mer’а (до 11нт), на вход (stdin) последовательность
нуклеотидов, на выходе возвращает таблицу, где строке
соответствует k-mer, для него дано количество вхождений,
позиция первого вхождения, последнего, и среднее по всем
позициям. Из встроенных структур данных можно использовать
только [].
"""


def kmer_value(step_kmer, kmer):
    '''Функция, которая считает общую сумму кмера, на основании весов каждой буквы в зависимости от позиции в кмере.
    Возвращаемое значение в дальнейшем будет являться индексом, по которому в массиве будет сохранятся иформация о кмере'''
    count = 0
    for i in range(0, len(step_kmer)):
        if step_kmer[i] == 'G':
            for j in range(0, len(g[0:kmer])):
                if i == j:
                    count += g[j][0]
        elif step_kmer[i] == 'A':
            for j in range(0, len(a[0:kmer])):
                if i == j:
                    count += a[j][0]
        elif step_kmer[i] == 'T':
            for j in range(0, len(t[0:kmer])):
                if i == j:
                    count += t[j][0]
        elif step_kmer[i] == 'C':
            for j in range(0, len(c[0:kmer])):
                if i == j:
                    count += c[j][0]
        else:
            raise ValueError('Вы ввели некорректную последовательность')

    return count


# def kmer_value2(step_kmer, kmer):
#     '''Функция, которая считает общую сумму кмера, на основании весов каждой буквы в зависимости от позиции в кмере.
#     Возвращаемое значение в дальнейшем будет являться индексом, по которому в массиве будет сохранятся иформация о кмере'''
#     count = 0
#     for i in range(0, len(step_kmer)):
#         if step_kmer[i] in 'GATC':
#             for j in range(0, len(g[0:kmer])):
#                 if i == j and step_kmer[i] == 'G':
#                     count += g[j][0]
#                 elif i == j and step_kmer[i] == 'A':
#                     count += a[j][0]
#                 elif i == j and step_kmer[i] == 'T':
#                     count += t[j][0]
#                 elif i == j and step_kmer[i] == 'C':
#                     count += c[j][0]
#                 else:
#                     raise ValueError('Вы ввели некорректную последовательность')
#     return count


def hash_table(sequence, kmer):

    '''Надо создать массив в котором будем хранить индексы. Индексами будет являться сумма весов каждой буквы,
    в заисимости от ее положения в кмере. Наибольший вес у букв G, соответственно при ситуации, когда все буквы в кмере G
    длина массива будет определяться весами всех значений G'''

    massiv = [['nill' for i in range(5)] for j in range(sum(i[0] for i in g[0:kmer]) + 1)]

    for i in range(0, len(sequence) - kmer + 1):
        step_kmer = sequence[i:i + kmer]
        ind = kmer_value(step_kmer, kmer)
        if massiv[ind][0] == 'nill':
            massiv[ind][0] = step_kmer
            massiv[ind][1] = 1
            massiv[ind][2] = i
            massiv[ind][3] = i
        elif massiv[ind][0] == step_kmer:
            massiv[ind][1] += 1
            massiv[ind][3] = i
        elif massiv[ind][0] != step_kmer and isinstance(massiv[ind][0], str):
            massiv[ind] = [massiv[ind], [step_kmer, 1, i, i, 'nill']]
        else:
            table = massiv[ind]
            for j in range(0, len(table)):
                if table[j][0] == step_kmer:
                    table[j][1] += 1
                    table[j][3] = i
                    break
            else:
                table.append([step_kmer, 1, i, i, 'nill'])

    return massiv


'''Для того, чтобы написать реализацию хэш функции, создадим 4 листа из кортежей для 4 букв (A, T, G, C), где каждой 
букве в зависимости от её позиции присвоим определенный вес'''
a = list(zip(range(0, 11), 'A'*11))
t = list(zip(range(20, 31), 'T'*11))
c = list(zip(range(40, 51), 'C'*11))
g = list(zip(range(60, 71), 'G'*11))


if __name__ == "__main__":
    sequence = input("Введите последовательность: ")  #AACCGGAAATGTG
    kmer = int(input("Введите длину k-мера от 1 до 11: "))
    table = hash_table(sequence, kmer)
    print(len(table))
