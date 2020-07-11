# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    # initialize indeces for both arrays
    index_a = index_b = 0
    # loop through the arrays
    while index_a < len(arrA) and index_b < len(arrB):
        # compare elements at given index
        # set smaller value at given index of merged_arr
        print('\n')
        print(f'index: {index_a}, {index_b}')
        print(f'A:{arrA} || B:{arrB}')
        print(f'{arrA[index_a]} : {arrB[index_b]}')
        if arrA[index_a] < arrB[index_b]:
            merged_arr.append(arrA[index_a])
            print(merged_arr)
            print(index_a)
            index_a += 1
            print(index_a)
        else:
            merged_arr.append(arrB[index_b])
            print(merged_arr)
            index_b += 1
    if index_a == len(arrA):
        merged_arr.extend(arrB[index_b:])
    else:
        merged_arr.extend(arrA)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        print('\n')
        print(arr)
        return arr
    print('\n')
    print(arr)
    mid = int(len(arr)/2)
    print(mid)
    # split array and call merge_sort on each half
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return

def merge_sort_in_place(arr, l, r):
    # Your code here
    return

# array1 = [4,2,6]
# array2 = [7,3,1]
# result = merge(array1, array2)

# appended = array1 + array2
# result = merge_sort(appended)

# print(result)