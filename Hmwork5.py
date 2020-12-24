'''
Написать программу, которая запрашивает на ввод целые числа, до тех пор, пока не будет введена пустая строка.
Затем она выводит: а) введенную последовательность чисел; б) сумму введенных чисел; в) самое большое число из введенных.
(а), (б) и (в) – это разные варианты одной программы.
...
#a)
'''
ls = []
while True:
    number = input("Введите целое число ")
    if number != "" and number.isdigit():
        ls.append(number)
    elif number != "" and isinstance(number, str):
        continue
    else:
        print("Вы ввели пустое значение")
        break
print(ls)

...
# б)
...
ls = []
while True:
    number = input("Введите целое число ")
    if number != "" and number.isdigit():
        ls.append(int(number))
    elif number != "" and isinstance(number, str):
        continue
    else:
        print("Вы ввели пустое значение")
        break
print("Сумма всех введенных вами чисел = " + str(sum((ls))))

# в)

ls = []
while True:
    number = input("Введите целое число ")
    if number != "" and number.isdigit():
        ls.append(int(number))
    elif number != "" and isinstance(number, str):
        continue
    else:
        print("Вы ввели пустое значение")
        break
print("Максимальное число в списке = " + str(max((ls))))


# И наконец-то я поняла, как можно написать функцию, которая создает список из введенных чисел.
def list_with_numbers(number, ls=[]):
    if number != "" and number.isdigit():
        ls.append(int(number))
        while True:
            number = input("Введите целое число ")
            if number != "" and number.isdigit():
                ls.append(int(number))
            elif number != "" and isinstance(number, str):
                continue
            else:
                print("Вы ввели пустое значение")
                break
        return ls
    else:
        print("Введено некорректное значение")
        list_with_numbers(input("Введите число: "))


list_with_numbers(input("Введите число: "))

print(list_with_numbers(input("Введите число: ")))  # выводит просто список
print(sum(list_with_numbers(input("Введите число: "))))  # выводит сумму чисел
print(max(list_with_numbers(input("Введите число: "))))  # выводит максимальное значение