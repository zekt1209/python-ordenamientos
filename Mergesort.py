def merge_sort(arr):        # Mergesort O(n log n)
    if len(arr) > 1:
        left_arr=arr[:len(arr)//2]
        right_arr=arr[len(arr)//2:]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i = 0
        j = 0
        k = 0

        while i<len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test=[2,3,5,1,7,4,4,2,6,0]

merge_sort(arr_test)
print(arr_test)







arreglo = [1,3,2,5,4,7,6,9,8]


"""
def merge(arr, l, a, b):
    n1 = a - l + 1
    n2 = b - a

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[a + 1 + j]

        # merge the temp arrays back into arr[l..b]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there  are any

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there areany

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
def mergeSort(arr, l, b):
    if l < b:
        # Same as (l+b)//2, but avoids overflow for
        # large l and h
        a = (l + (b - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, a)
        mergeSort(arr, a + 1, b)
        merge(arr, l, a, b)

    # Driver code


arr = [66, 11, 99, 23, 6, 66, 45, 20]
n = len(arr)
print(" Given Array ")
for i in range(n):
    print("%d" % arr[i]),

mergeSort(arr, 0, n - 1)
print("\nSorted Array is")
for i in range(n):
    print("%d" % arr[i])

"""