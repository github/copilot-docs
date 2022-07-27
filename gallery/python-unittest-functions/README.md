# [Copilot examples](../README.md) › [Unit testing with Copilot](README.md) (Python)

In this example we write simple function using Copilot and then let it create mock data and unittests for us, thus giving complete control over our code to the Copilot.


## Setup:

Requires Python (>3.8) and unittest library.

## Steps:

- Create a new file called `your_func_name.py`

- Type `#function that delets number from array` on line 1 then on the next line start writing `def your_function_name` and press <kbd>Tab</kbd> to let Copilot complete your code. 
- You can also use <kbd>Ctrl</kbd> + <kbd>Enter</kbd> to view other suggestions

- Accept the following solution(example function `delete_numbers`):

  ```python
    def delete_numbers(numbers, number):
        for i in range(len(numbers)):
            if numbers[i] == number:
                del numbers[i]
        return numbers
  ```

- Type `#unit test for function delete_numbers`, go on to the next line and use <kbd>Tab</kbd> to allow Copilot complete code with the suggestions.
It should suggest mock data, like the following:

  ```python
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_number = 5
  ```

- Go onto the next line and import `unittest`- this will hint Copilot you want to use `unittest` library for testing. On the next line start typing `class` and let Copilot autocomplete your code with proper unit test and assertions:

  ```python
    import unittest
    class TestDeleteNumbers(unittest.TestCase):
        def test_delete_numbers(self):
            self.assertEqual(delete_numbers(test_list, test_number), [1, 2, 3, 4, 6, 7, 8, 9, 10])
  ```

And you are done! You let copilot suggest and autocomplete code. It wrote a function you wanted and then you hinted it that you want to use `unittest` library for creating unittest. It provided you with data and even auto created a correct assertion. Amazing! Now creating simple functions and simple unit tests should be a breeze. You can see full file that was created by Github Copilot in the repo.

#

‹ [back to list of Copilot examples](../README.md)
