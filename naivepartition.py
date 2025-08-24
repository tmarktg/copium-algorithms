# QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

# It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

# There are mainly three steps in the algorithm:

# Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
# Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

# Partition Algorithm

# The key process in quickSort is a partition(). There are three common algorithms to partition. All these algorithms have O(n) time complexity.

# Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.

# Naive partition
def partition(arr):
    tempArr = []
    n = len(arr)
    pivot = arr[n - 1]

    for i in range(n):
        if (pivot >= arr[i]):
            tempArr.append(arr[i])

    for i in range(n):
        if (pivot < arr[i]):
            tempArr.append(arr[i])
    
    for i in range(n):
        arr[i] = tempArr[i]


def quicksort(arr):
    partition(arr)

    print(arr)

arr = [5, 13, 6, 9, 12, 11, 8]
