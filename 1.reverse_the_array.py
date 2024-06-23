print("Enter your array to reverse, eg: 1 2 3")
str = input()
array = str.split(" ")


def reverseArr(arr):
    # Array Reverse Using an Extra Array
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(n)
    revArr = []
    for ind in range(len(arr)):
        revInd = len(arr) - ind
        revArr.append(arr[revInd - 1])
    print("reverse array: ", revArr)


reverseArr(array)


def inbuiltMethod():
    # inbuild array method in python for reverse
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(n)
    print("inbuilt method: ", array[::-1])


inbuiltMethod()


def iterativeReverseArr(arr, start, end):
    # Iterative python program to reverse an array
    # Time Complexity: O(n)
    # Auxiliary Space Complexity: O(1)
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print("reverse array using iterative: ", arr)


iterativeReverseArr(array, 0, len(array) - 1)
