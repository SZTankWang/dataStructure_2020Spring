import random

def merge(temp_array1, temp_array2, array):
    """ Merge two sorted lists temp_array1 and temp_array2 into properly sized list S.

        (This is the merge step, merge two sorted lists.)

        :param temp_array1: left half array copy
        :param temp_array2: right half array copy
        :param array:       the original array being sorted
    """
    # To do
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(temp_array1) and ptr2 < len(temp_array2):
        if temp_array1[ptr1] < temp_array2[ptr2]:
            array[ptr1+ptr2] = temp_array1[ptr1]
            ptr1 += 1
        else:
            array[ptr1+ptr2] = temp_array2[ptr2]
            ptr2 += 1
    while ptr1 < len(temp_array1):
        array[ptr1+ptr2] = temp_array1[ptr1]
        ptr1 += 1
    while ptr2 < len(temp_array2):
        array[ptr1+ptr2] = temp_array2[ptr2]
        ptr2 += 1

    return array



def merge_sort(array):
    """ Sort the elements of Python list using the merge-sort algorithm.
        :param array: the original array being sorted
    """
    # To do
    if len(array) == 1:
        return array
    else:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        left_sub = merge_sort(left)
        right_sub = merge_sort(right)
        return merge(left_sub,right_sub,array)


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-1000, 1000))

    print("Before sorting:")
    print(array)
    merge_sort(array)
    print("After sorting:")
    print(array)
    print("sorted?")
    print(array == sorted(array))
    array2 = [8,5,2,0,6,4,5,1]
    print(array2)
    merge_sort(array2)
    print(array2)
    print("sorted?",array2==sorted(array2))
if __name__ == '__main__':
    main()
