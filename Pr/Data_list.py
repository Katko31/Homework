

class Box:

    def __init__(self, data):
        self.data = data
        self.link = None    # ссылка, которая в конструкторе коробки всегда пустая


class MyList:

    def __init__(self):
        self.pointer = None

    def append_start(self, new_data):
        new_element = Box(new_data)
        new_element.link = self.pointer
        self.pointer = new_element

    def append_end(self, new_data):
        new_element = Box(new_data)
        if self.pointer is None:
            self.pointer = new_element
            return
        end = self.pointer
        while end.link:
            end = end.link
        end.link = new_element

    def remove_first_box(self):
        if self.pointer is None:
            raise ValueError('Список пуст')
        else:
            self.pointer = self.pointer.link

    def remove_last_box(self):
        if self.pointer is None:
            raise ValueError('Список пуст')
        end = self.pointer
        while end.link:
            end = end.link
        end.link = None

    def insert(self, new_data, position):
        new_element = Box(new_data)
        if self.pointer is None:
            self.pointer = new_element
            return

        mid1 = self.pointer
        i = 0
        while mid1.link:
            if i != position:
                mid1 = mid1.link
                i += 1

            new_element.link = mid1.link
            mid2 = self.pointer
            i = 0
            while mid2.link:
                if i != position - 1:
                    mid2 = mid2.link
                    i += 1
                mid2.link = new_element
                break
            break

    def get_data_value(self, data):
        if self.pointer is None:
            raise ValueError('Список пуст')
        finder = self.pointer
        i = 0
        while finder.link:
            if finder.data != data:
                finder = finder.link
                i += 1
            else:
                return f'{data}[{i}]'

    def get_index_value(self, index):
        if self.pointer is None:
            raise ValueError('Список пуст')
        finder = self.pointer
        i = 0
        while finder.link:
            if i != index:
                finder = finder.link
                i += 1
            else:
                return f'{finder.data}[{i}]'

        return f'{finder.data}[{i}]'

    def __getitem__(self, item):
        return self.pointer.data[item]


if __name__ == "__main__":
    a = MyList()
    a.append_start(12)
    a.append_start(11)
    a.append_start(15)
    a.append_start(19)
    print(a.get_index_value(3))
