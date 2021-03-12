

class DataList:   # базовая структура данных лист

    def __init__(self):
        self.values = []

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть числом')
        if item >= len(self.values) or item < -len(self.values):
            raise IndexError('Объекта с таким индексом не существует')

        return self.values[item]

    def __setitem__(self, item, value):
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть числом')
        if item >= len(self.values) or item < -len(self.values):
            raise IndexError('Объекта с таким индексом не существует')

        self.values[item] = value

    def delete(self, var):
        if var not in self.values:
            raise ValueError('Такого значения в списке нет')
        self.values.remove(var)


    def vstavka(self, index, value):
        self.values.insert(index, value)



if __name__ == "__main__":

    a = DataList()
    print(a.values)
    a.delete(45)
    a[1] = 100
    print(a.values)
