#include <iostream>

// create a function that reverses the order of the elements in an array and returns the new array
int *reverse(int *arr, int size)
{
    int *newArr = new int[size];
    for (int i = 0; i < size; i++)
    {
        newArr[i] = arr[size - i - 1];
    }
    return newArr;
}

// test the reverse function
int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int *newArr = reverse(arr, 5);
    for (int i = 0; i < 5; i++)
    {
        std::cout << newArr[i] << " ";
    }
    std::cout << std::endl;
    delete[] newArr;
    return 0;
}
