'''
Написать программу, которая запрашивает на ввод целые числа, до тех пор,
пока не будет введена пустая строка. После каждого введенного числа программа возвращает ответ,
делиться ли это число на 2, 3, 5, 7, 11.
'''

def true_func():
    divisor = [2, 3, 5, 7, 11]
    result = 0

    while True:
        number = input("Введите число: ")
        ls = []

        if number != "" and number.isdigit():

            for i in divisor:
                if int(number) % i == 0:
                    result += 1
                    ls.append(i)

            if result > 0:
                print(f'Ваше число {number} делится на {ls}')
                del ls

        elif number != "" and isinstance(number, str):
            continue

        else:
            print("Вы ввели пустое значение")
            break


true_func()
