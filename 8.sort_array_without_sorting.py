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
