# QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

# It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.

# There are mainly three steps in the algorithm:

# Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
# Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.

# Partition Algorithm

# The key process in quickSort is a partition(). There are three common algorithms to partition. All these algorithms have O(n) time complexity.

# Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.

# Step-by-step explanation of algorithm:

# Choose the last element of the array as the pivot.
# Initialise pointer i at the start of the array; this pointer will act as the boundary of elements that are smaller than or equal to the pivot.
# Traverse the array with pointer j, checking each element arr[j]:
# If arr[j] <= pivot, swap arr[i] with arr[j] to move the smaller element to the left and increment i to adjust the boundary.
# After traversing, elements smaller than or equal to the pivot will be at the start of the array, with i marking the boundary.
# Finally, swap arr[i] with the pivot (last element) to place pivot in its correct position.


def partition(arr, low, high):
   
   pivot = arr[high]
#    keep track of i 
   i = low - 1
   for j in range(low, high):
       if arr[j] < pivot:
           i+=1
           swap(arr, i, j)
   swap(arr, i + 1, high)
   return i + 1
#    arr[i + 1], arr[high] = arr[high], arr[i + 1]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


arr = [5, 13, 6, 9, 12, 11, 8]
# [5, 6, 13, 9, 12, 11, 8]
# [5, 6, 9, 13, 12, 11, 8]
# [5, 6, 9, 8, 11, 13, 12]
n = len(arr)
quicksort(arr, 0, n - 1)
print(arr)
