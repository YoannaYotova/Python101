import unittest
from my_sort import my_sort


class TestMySort(unittest.TestCase):
    def test_with_no_arguments(self):

        exc = None
        try:
            my_sort()
        except Exception as err:
            exc = err

        self.assertIsNotNone(str(exc))
        self.assertEqual(str(exc), 'Calling the function with no arguments.')

    def test_with_one_empty_tuple_and_return_empty_tuple(self):
        arr = ()

        res = my_sort(arr)

        self.assertEqual(arr, res)

    def test_with_one_empty_list_and_return_empty_list(self):
        arr = []

        res = my_sort(arr)

        self.assertEqual(arr, res)

    def test_with_unordered_tuple_then_return_it_sorted_with_defaulted_ascending_true(self):
        arr = (10, 8, 9, 10, 100)

        res = my_sort(arr)

        self.assertEqual(res, (8, 9, 10, 10, 100))

    def test_with_unordered_list_then_return_it_sorted_with_defaulted_ascending_true(self):
        arr = [10, 8, 9, 10, 100]

        res = my_sort(arr)

        self.assertEqual(res, [8, 9, 10, 10, 100])

    def test_with_unordered_list_with_true_ascendig_and_return_it_sorted(self):
        arr = [10, 8, 9, 10, 100]
        ascending = True

        res = my_sort(arr, ascending)

        self.assertEqual(res, [8, 9, 10, 10, 100])

    def test_with_unordered_list_with_false_ascendig_and_return_it_sorted(self):
        arr = [5, 3, 18, 14, 100]
        ascending = False

        res = my_sort(arr, ascending)

        self.assertEqual(res, [100, 18, 14, 5, 3])

    def test_with_list_of_dictionaries_defaulted_ascending_true_and_key_value_int_return_sorted_list_of_dictionaries(self):
        dic = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

        res = my_sort(dic, key='age')

        self.assertEqual(res, [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}])

    def test_with_list_of_dictionaries_false_ascending_and_key_value_int_return_sorted_list_of_dictionaries(self):
        dic = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

        res = my_sort(dic, ascending=False, key='age')

        self.assertEqual(res, [{'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}])

    def test_with_list_of_dictionaries_defaulted_ascending_and_key_value_string_return_sorted_list_of_dictionaries(self):
        dic = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

        res = my_sort(dic, key='name')

        self.assertEqual(res, [{'name': 'Ivo', 'age': 27}, {'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}])

    def test_with_list_of_dictionaries_false_ascending_and_key_value_string_return_sorted_list_of_dictionaries(self):
        dic = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]

        res = my_sort(dic, ascending=False, key='name')

        self.assertEqual(res, [{'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}])


if __name__ == '__main__':
    unittest.main()
