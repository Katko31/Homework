

class Box:

    def __init__(self, data):
        self.data = data
        self.link = None    # ссылка, которая смотрить на предыдущий элемент


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






a = MyList()


a.append_start(12)
a.append_start(11)
a.append_start(15)
a.append_start(19)

print(a)