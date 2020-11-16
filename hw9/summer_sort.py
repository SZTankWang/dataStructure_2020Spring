import random

def find_max(array, a, b):
    ''' Finds the position of the largest element between two indices in the array.
        @array: the python list
        @a:     the index of first element to check
        @b:     the index of last element to check

        return: index of the largest element
    '''
    maxPos = a
    for i in range(a, b):
        if (array[maxPos] < array[i]):
            maxPos = i
    return maxPos

def reverse(array, a, b):
    ''' Reverses the elements between two indices in the array. 
        @array: the python list
        @a:     the index of first element to reverse
        @b:     the index of "one past" last element to reverse
    '''
    l = a
    r = b
    while (l < r):
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1

def summer_sort(array):
    ''' Sorts the array using find_max(array, a, b) and reverse(array, a, b) functions.
        :param array: the python list
    '''
    # To do
    
    
    i = len(array)
    
    while i >= 1:
        max_index = find_max(array, 0, i) #find max in current indices
        
        reverse(array,max_index,i-1) #put current max value to the end 
        
        i -= 1 #shift one backward
        
        
        
        
def main():
    array = []
    for i in range(20):
        array.append(random.randint(-1000, 1000))

    print("Before sorting:")
    print(array)
    summer_sort(array)
    print("After sorting:")
    print(array)
    print("sorted?")
    print(array == sorted(array))


if __name__ == '__main__':
    main()