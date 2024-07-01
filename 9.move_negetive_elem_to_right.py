def reArrangeArr(arr):
    # Rearranges the array such that all negative numbers appear before positive numbers.

    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1).
    # Pros: Simple implementation, operates in linear time.
    # Cons: Requires additional logic to handle edge cases or different conditions.
    low = 0
    high = len(arr) - 1
    while low < high:
        if arr[low] < 0:
            low += 1
        elif arr[high] > 0:
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
    print(arr)


reArrangeArr([-1, 2, 5, 10, -2, 5, -7])


def sort_negative_first(arr):
    # Sorts an array such that all negative numbers appear before non-negative numbers.

    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1).
    # Pros: Efficient for sorting negative numbers first in linear time.
    # Cons: Limited to sorting based on one condition (negative vs non-negative).
    j = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    print(arr)


sort_negative_first([-1, 2, 3, -2, -8])
