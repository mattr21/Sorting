# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)      

        # loop through the remaining numbers
        for j in range (cur_index, len(arr)):
            # if the number you are looking at is smaller than the current smallest
            if arr[j] < arr[smallest_index]:
                # replace the current smallest with the number you are looking at
                smallest_index = j

        # TO-DO: swap

        # set the number at current index to the number at smallest index & set the number at smallest index to number at current index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # set up a swapped variable and default it to true
    swapped = True

    # while swapped = true
    while swapped:
        swapped = False
        # loop through all numbers
        for i in range(0, len(arr) - 1):
            # if the number at the current index is greater than the number at the next index
            if arr[i] > arr[i + 1]:
                # swap the number at current index with number at next index
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # set swapped = true
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr