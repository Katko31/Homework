import unittest
from Data_list import MyList, Box


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.my_list = MyList()

    def test_box_init(self):
        box = Box(7)
        self.assertEqual(box.data, 7)
        self.assertIsNone(box.link)

    def test_my_list_init(self):
        self.assertIsNone(self.my_list.pointer)

    def test_append_start(self):
        self.my_list.append_start(7)
        self.my_list.append_start(8)
        self.my_list.append_start(9)

        self.assertEqual(self.my_list.get_data_value(9), self.my_list.get_index_value(0))
        self.assertEqual(self.my_list.get_data_value(8), self.my_list.get_index_value(1))
        self.assertEqual(self.my_list.get_data_value(7), self.my_list.get_index_value(2))
        self.assertNotEqual(self.my_list.get_data_value(8), self.my_list.get_index_value(0))

    def test_append_end(self):
        self.my_list.append_end(7)
        self.my_list.append_end(1)
        self.assertEqual(self.my_list.get_data_value(1), self.my_list.get_index_value(1))
        self.assertNotEqual(self.my_list.get_data_value(7), self.my_list.get_index_value(1))

    def test_remove_first_box(self):
        self.my_list.append_start(0)
        self.my_list.append_end(7)
        self.assertEqual(self.my_list.get_data_value(0), self.my_list.get_index_value(0))
        self.my_list.remove_first_box()
        with self.assertRaises(ValueError):
            self.my_list.get_data_value(0)
        self.assertEqual(self.my_list.get_data_value(7), self.my_list.get_index_value(0))

        with self.assertRaises(ValueError):
            test_list2 = MyList()
            test_list2.remove_first_box()

    def test_remove_last_box(self):
        self.my_list.append_start(0)
        self.my_list.append_end(7)
        self.assertEqual(self.my_list.get_data_value(0), self.my_list.get_index_value(0))

        self.my_list.remove_last_box()

        with self.assertRaises(ValueError):
            self.my_list.get_data_value(7)

    def test_get_index_value(self):
        self.my_list.append_start(4)
        test_value = self.my_list.get_index_value(0)

        self.assertEqual(test_value, '4[0]')
        self.assertNotEqual(test_value, 'None')
        with self.assertRaises(IndexError):
            self.my_list.get_index_value(1)

    def test_get_data_value(self):
        self.my_list.append_end(10)
        test_value = self.my_list.get_data_value(10)

        self.assertEqual(test_value, '10[0]')
        self.assertNotEqual(test_value, 'None')
        with self.assertRaises(ValueError):
            self.my_list.get_data_value(4)

    def test_insert(self):
        self.my_list.append_start(0)
        self.my_list.append_end(2)
        self.my_list.insert(1, 1)

        self.assertEqual(self.my_list.get_data_value(1), self.my_list.get_index_value(1))
        self.assertNotEqual(self.my_list.get_data_value(2), self.my_list.get_index_value(1))


if __name__ == '__main__':
    unittest.main()
