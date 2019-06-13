# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # initialize an index for arrA (j)
    j = 0
    # initialize an index for arrB (k)
    k = 0

    # loop through elements
    for i in range(elements):
        # if the index j >= length of arrA
        if j >= len(arrA):
            # set the number at the ith index of merge_arr to the number at the kth index of arrB
            merged_arr[i] = arrB[k]
            # increment k
            k += 1

        # else if the index k >= length of arrB
        elif k >= len(arrB):
            # set the number at the ith index of merge_arr to the number at the jth index of arrA
            merged_arr[i] = arrA[j]
            # increment j
            j += 1

        # else if the number at the jth index of arrA is less than the number at the kth index of arrB
        elif arrA[j] < arrB[k]:
            # set the number at the ith index of merge_arr to the number at the jth index of arrA
            merged_arr[i] = arrA[j]
            # increment j
            j += 1

        else:
            # set the number at the ith index of merged_arr to the number at the kth index of arrB
            merged_arr[i] = arrB[k]
            # increment k
            k += 1
        

    # print("\n THIS IS WHAT I'M LOOKING FOR!!!\n ", merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if the length of the array is greater than 1
    if len( arr ) > 1:
        # set the left side with recursion passing an argument to merge_sort that slices the arr in half so you have the left side
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        # set the right side with recursion passing an argument to merge_sort that slices the arr i half so you have the right side
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        # set arr by using the merge helper function to sort and put the parts back together
        arr = merge( left, right )
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
