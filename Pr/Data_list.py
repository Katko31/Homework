

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
        cutter = None
        while end.link != None:
            cutter = end
            end = end.link
        cutter.link = None

    def insert(self, new_data, position):
        if position == 0:
            self.append_start(new_data)

        else:
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
                else:
                    new_element.link = mid1
                    break

            if i == position:
                new_element.link = mid1

            mid2 = self.pointer
            i = 0
            while mid2.link:
                if i != position - 1:
                    mid2 = mid2.link
                    i += 1
                else:

                    mid2.link = new_element
                    break
            if position > i:
                mid2.link = new_element

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
        if finder.data == data:
            return f'{data}[{i}]'
        if finder.data != data and finder.link == None:
            raise ValueError('В списке такого значения нет')

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

        if index > i:
            raise IndexError('Такого индекса нет')
        else:
            return f'{finder.data}[{i}]'

    def remove_data_value(self, data):
        if self.pointer is None:
            raise ValueError('Список пуст')

        back = None
        mid = self.pointer

        while mid != None:
            if mid.data != data:
                back = mid
                mid = mid.link

            elif mid.data == data and mid == self.pointer:
                self.remove_first_box()
                break

            else:
                back.link = mid.link
                break


if __name__ == "__main__":
    a = MyList()

    a.append_end(3)
    a.append_start(7)
    a.append_start(15)
    a.remove_last_box()
    a.append_start(19)
    print(a.get_index_value(3))
    print(a.get_data_value(11))
    a.remove_data_value(12)
    a.insert(56, 4)
    print(a.get_data_value(56))
