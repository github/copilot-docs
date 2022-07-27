#function that delets number from array
def delete_numbers(numbers, number):
    for i in range(len(numbers)):
        if numbers[i] == number:
            del numbers[i]
    return numbers

#unit test for function delete_numbers
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_number = 5

import unittest
class TestDeleteNumbers(unittest.TestCase):
    def test_delete_numbers(self):
        self.assertEqual(delete_numbers(test_list, test_number), [1, 2, 3, 4, 6, 7, 8, 9, 10])