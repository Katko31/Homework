"""
Написать реализацию базовых структур данных (лист, стек и очередь)
"""
from functools import wraps


def show_data(func):

    """Декоратор, показывает что происходит с данными при выполнении функции, на которую "навешивается"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            self = args[0]
            print(f'{self.data}')
            return func(*args, **kwargs)
        except TypeError:
            print('Вы не ввели значение')

    return wrapper


class MyQueue:

    """Очередь - базовая труктура данных. Реализация через массив"""

    def __init__(self):
        self.data = []

    @show_data
    def add_new(self, value):
        if value is None:
            raise TypeError('Вы не ввели значение')
        self.data.append(value)
        return self.data

    @show_data
    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        raise IndexError('Очередь пуста')


class MyStack:

    """Стек - базовая труктура данных. Реализация через массив"""

    def __init__(self):
        self.data = []

    @show_data
    def add_new(self, value):
        if value is None:
            raise TypeError('Вы не ввели значение')
        self.data.append(value)
        return self.data

    @show_data
    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(-1)
        raise IndexError('Стек пуст')


if __name__ == "__main__":

    a = MyQueue()
    a.add_new()
    a.add_new(10)
    a.add_new(111)

    print(a.remove())
    print(a.remove())
    print(a.remove())

    b = MyStack()
    b.add_new(1)
    b.add_new(10)
    b.add_new(111)

    print(b.remove())
    print(b.remove())
    print(b.remove())
