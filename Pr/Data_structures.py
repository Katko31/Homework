"""
Написать реализацию базовых структур данных (лист, стек и очередь)
"""
from functools import wraps

def show_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        print(f'{self.data}')
        return func(*args, **kwargs)

    return wrapper

# class DataList(list):   # базовая структура данных лист
#
#     # def __init__(self):
#     #     self.list = []
#
#     def __getitem__(self, item):
#         if item >= len(self):
#             raise IndexError('Объекта с таким индексом не существует')
#         return super(DataList, self).__getitem__(item)
#
#     def __setitem__(self, item, value):
#         if item >= len(self):
#             self.append(value)
#         else:
#             super(DataList, self).__setitem__(item, value)

# a = DataList([1, 2, 3])
# a[2] = 10
# print(a)

class MyQueue:

    def __init__(self):
        self.data = []

    @show_data
    def add_new(self, value):
        self.data.append(value)
        # print(self.queue)
        return self.data

    @show_data
    def remove(self):
        return self.data.pop(0)

class MyStek:

    def __init__(self):
        self.data = []

    @show_data
    def add_new(self, value):
        self.data.append(value)
        return self.data

    @show_data
    def remove(self):
        return self.data.pop(-1)

if __name__ == "__main__":

    a = MyQueue()
    a.add_new(1)
    a.add_new(10)
    a.add_new(111)

    print(a.remove())
    print(a.remove())
    print(a.remove())

    b = MyStek()
    b.add_new(1)
    b.add_new(10)
    b.add_new(111)

    print(b.remove())
    print(b.remove())
    print(b.remove())
