print("Enter your array: ")
str = input()
array = [int(num_ele) for num_ele in str.split(" ")]


def get_min_max_arr(arr):
    # Time Complexity: O(n) - The function iterates through the array once.
    # Auxiliary Space Complexity: O(1) - The function uses a constant amount of extra space.
    # Pros: Efficient with a linear time complexity. Does not require additional space.
    n = len(arr)
    if n == 0:
        max = arr[0]
        min = arr[0]

    if arr[0] > arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        min = arr[0]
        max = arr[1]

    for i in range(2, n):
        if max < arr[i]:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]

    print(f"Min: {min}, Max: {max}")


get_min_max_arr(array)


def min_max_by_sort(arr):
    # Time Complexity: O(n log n) (due to the sort operation)
    # Auxiliary Space Complexity: O(1) (sort is in-place)
    # Pros: Simple and leverages Python's built-in sort capabilities.
    # Cons: Sorting the array is not the most efficient way to find min and max
    arr.sort()
    print(f"Min: {arr[0]}, Max: {arr[-1]}")


min_max_by_sort(array)
