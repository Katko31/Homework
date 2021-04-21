"""
 Написать программу, которая принимает в качестве параметра
размер k-mer’а (до 11нт), на вход (stdin) последовательность
нуклеотидов, на выходе возвращает таблицу, где строке
соответствует k-mer, для него дано количество вхождений,
позиция первого вхождения, последнего, и среднее по всем
позициям. Из встроенных структур данных можно использовать
только [].
"""
# AACCGTAAATCCAGT


def nested_list(seq, kmer):

    """функция, которая создает таблицу (вложенные списки):
    kmer_table [[Название кмера, количества вхождений, первое вхождение, последнее вхождение, покрытие?], ..., и т.д.]
    """

    table = []
    for i in range(0, len(seq)-kmer+1):

        step_kmer = seq[i:i+kmer]
        for j in range(0, len(table)):
            if table[j][0] == step_kmer:
                table[j][1] += 1
                table[j][3] = i
                break
        else:
            table.append([step_kmer, 1, i, i])

    for kmer in table:
        kmer.append(kmer[1]/len(seq))

    return table


if __name__ == "__main__":
    sequence = input("Введите последовательность: ")
    kmer = int(input("Введите длину k-мера от 1 до 11: "))

    if kmer >= 12 or kmer < 1 or sequence == "" or not sequence.isalpha():
        raise ValueError("Вы ввели некорректное значение длины k-мера")

    table = nested_list(sequence, kmer)
    print(table)
