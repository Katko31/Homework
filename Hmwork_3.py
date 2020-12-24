'''
3. Написать программу, которая запрашивает на ввод произвольную строку текста (написанную с  использованием латинского алфавита).
Программа выводит: а) эту же строку, но без гласных; б) список использованных гласных; в) количество использованных гласных;
г) статистику по встречаемости (буква – количество ее вхождений в строку). (а), (б), (в) и (г) – это разные варианты одной программы.
'''


def consonant(s):  # a) строка без гласных

    c = []
    for x in s:
        if x not in 'eyuioaEYUIOA':
            c.append(x)
    new_s = ''.join(c)
    print("Ваша строка без гласных :" + new_s)


consonant(input("Введите строку "))


def vowel(s):  # б) список использованных гласных

    c = []
    for x in s:
        if x in 'eyuioaEYUIOA':
            c.append(x)
    new_s = ''.join(c)
    print("Список использованных гласных :" + new_s)


vowel(input("Введите строку "))


def counter(s):  # в) количество гласных в строке
    result = 0
    for x in s:
        if x in 'eyuioaEYUIOA':
            result += 1
    print("Количество гласных в строке равно " + str(result))


counter(input("Введите строку "))


def vowel_count(s):  # г) статистику по встречаемости

    c = {}
    for x in s:
        if x not in c and x in 'eyuioaEYUIOA':
            c[x] = s.count(x)
    print(c)


vowel_count(input())
