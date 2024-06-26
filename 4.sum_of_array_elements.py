print("Enter your array: ")
str = input()
array = [int(value) for value in str.split(" ")]


def sum_of_arr_elements(arr):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    # Pros: Simple and straightforward implementation.
    # Cons: None significant for basic summing operations; however, for large arrays,
    # the overall performance can be influenced by factors like memory bandwidth and cache efficiency.
    sum = 0
    for value in arr:
        sum = sum + value

    print(f"Sum: {sum}")


sum_of_arr_elements(array)


def inbuilt_sum_method(arr):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    # Pros: Leveraging built-in functions like sum() can lead to cleaner and potentially more optimized code.
    # Cons: Dependency on the implementation details of sum() in Python,
    # which might vary across different Python versions and implementations.
    s = sum(arr)
    print(f"Sum: {s}")


inbuilt_sum_method(array)
