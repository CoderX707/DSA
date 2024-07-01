def sort_array_without_sorting(arr):
    # Sorts an array in non-decreasing order without using Python's built-in sorting functions.

    # Time Complexity: O(n^2), where n is the number of elements in the array.
    # Auxiliary Space Complexity: O(1).
    # Pros: Simple implementation, suitable for small arrays.
    # Cons: Inefficient for large arrays due to quadratic time complexity.
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    print(arr)


sort_array_without_sorting([-1, 1, -2])


def sort_0s_1s_2s(arr):
    # Sorts an array of 0s, 1s, and 2s in non-decreasing order without using Python's built-in sorting functions.

    # Time Complexity: O(n).
    # Auxiliary Space Complexity: O(1).
    # Pros: Efficient for arrays containing only 0s, 1s, and 2s. Simple implementation.
    # Cons: Limited to specific input (0s, 1s, and 2s).
    i = 0
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1

        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high = high - 1
    print(arr)


sort_0s_1s_2s([1, 0, 1, 2, 0, 2, 0])
