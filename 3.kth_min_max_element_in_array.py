print("Enter your array: ")
str = input()
array = [int(ele) for ele in str.split(" ")]

print("Enter kth postion to find min and max:")
kth = int(input())


def kth_min_max_arr(arr, k):
    # Time Complexity: O(n log n) - due to sorting
    # Auxiliary Space Complexity: O(1) - sorting in-place
    # Pros: Simple implementation using built-in sorting
    # Cons: Sorting the entire array is inefficient for large arrays
    arr.sort()
    print(f"Min: {arr[k-1]}, Max: {arr[len(arr)-k]}")


kth_min_max_arr(array, kth)


def kth_bubble_sort(arr, k):
    # Time Complexity: O(n^2) - due to nested loops of bubble sort
    # Auxiliary Space Complexity: O(1) - sorting in-place
    # Pros: Simple implementation
    # Cons: Inefficient for large arrays due to quadratic time complexity
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"Min: {arr[k-1]}, Max: {arr[n-k]}")


kth_bubble_sort(array, kth)


def kth_selection_sort(arr, k):
    # Time Complexity: O(n^2) - due to nested loops of selection sort
    # Auxiliary Space Complexity: O(1) - sorting in-place
    # Pros: Simple implementation
    # Cons: Inefficient for large arrays due to quadratic time complexity
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    print(f"Min: {arr[k-1]}, Max: {arr[n-k]}")


kth_selection_sort(array, kth)


def kth_insertion_sort(arr, k):
    # Time Complexity: O(n^2) - due to nested loops of insertion sort
    # Auxiliary Space Complexity: O(1) - sorting in-place
    # Pros: Simple implementation
    # Cons: Inefficient for large arrays due to quadratic time complexity
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(f"Min: {arr[k-1]}, Max: {arr[len(arr)-k]}")


kth_insertion_sort(array, kth)
