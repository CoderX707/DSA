print("Enter your array: ")
str = input()
array = [int(value) for value in str.split(" ")]


def find_even_count_in_array(arr):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    # Pros: Simple and clear implementation to count even elements in an array.
    # Cons: None significant for basic counting operations; however, for very large arrays,
    # the overall performance can be influenced by factors like memory bandwidth and cache efficiency.
    count = 0
    for value in arr:
        if value % 2 == 0:
            count = count + 1
    print(f"even elements count: {count}")


find_even_count_in_array(array)


def even_elements_using_sum(arr):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    # Pros: Concise and utilizes Python's list comprehension and built-in sum() function for a potentially cleaner and more readable implementation.
    # Cons: Dependency on the comprehension and sum function may vary across different Python versions and implementations.
    val = sum(1 for value in arr if value % 2 == 0)
    print(f"even elements count: {val}")


even_elements_using_sum(array)
