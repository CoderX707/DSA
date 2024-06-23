print("Enter your array to reverse, eg: 1 2 3")
str = input()
array = str.split(" ")


def reverseArr(arr):
    # The function reverseArr provided uses an extra array to reverse the input array,
    # which has a time complexity of O(n) and an auxiliary space complexity of O(n).
    revArr = []
    for ind in range(len(arr)):
        revInd = len(arr) - ind
        revArr.append(arr[revInd - 1])
    print("reverse array: ", revArr)


reverseArr(array)


def inbuiltMethod():
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(n) (due to slicing creating a new list)
    # Pros: Very concise and leverages Python's built-in capabilities.
    # Cons: Still uses additional space for the new list.
    print("inbuilt method: ", array[::-1])


inbuiltMethod()


def iterativeReverseArr(arr, start, end):
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    # Pros: Does not use extra space, making it more space-efficient.
    # Cons: Slightly more complex to implement compared to the inbuilt method.
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    print("reverse array using iterative: ", arr)


iterativeReverseArr(array, 0, len(array) - 1)
