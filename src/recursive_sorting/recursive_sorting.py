# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = b = 0

    #print( "pre-if:")
    #print( "a, arrA:", a, arrA)
    #print( "b, arrB:", b, arrB)
    for n in range( elements):
        #print( "n, merged arr:", n, merged_arr)
        if a >= len( arrA):
            merged_arr[n] = arrB[b]
            b += 1
        elif b >= len( arrB):
            merged_arr[n] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            #print( "if arrA[a] < arrB[b]:", arrA[a], arrB[b])
            merged_arr[n] = arrA[a]
            a += 1
        else:
            merged_arr[n] = arrB[b]
            b += 1

    return merged_arr     
    """

    merged_arr = []
    while (len( arrA) > 0) & (len( arrB) > 0):
        if arrA[0] < arrB[0]:
            merged_arr.append( arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append( arrB[0])
            arrB = arrB[1:]
    
    return merged_arr + arrA + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len( arr) <= 1:
        return arr
    if len( arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return [arr[1], arr[0]]
    else:
        half = len( arr) // 2
        arrLeft = arr[ :half]
        arrRight = arr[ half:]

#        arr = merge_sort( merge( arrLeft, arrRight))
        arr = merge( merge_sort( arrLeft), merge_sort( arrRight))

        return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    arr = arr
    start = start
    mid = mid
    end = end
#    if right_start is None:
#        right_start = mid + 1
    if (start <= mid and (mid+1) <= end):
        if arr[start] <= arr[mid+1]:
            start += 1
            merge_in_place( arr, start, mid, end)
        else:
            value = arr[mid+1]
            for i in reversed( range( start, mid+2)):
                arr[i] = arr[i -1]
                arr[start] = value
                start += 1
                mid += 1

                merge_in_place( arr, start, mid, end)


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = l + r - 1 // 2
        merge_sort_in_place( arr, l, mid)
        merge_sort_in_place( arr, mid+1, r)
        merge_sort_in_place( arr, l, mid, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here
    ...

    return arr
