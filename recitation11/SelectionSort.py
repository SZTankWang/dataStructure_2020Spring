import random

def selection_sort(array):
    """ The algorithm proceeds by finding the smallest element in the unsorted sublist, 
        exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), 
        and moving the sublist boundaries one element to the right. 
        :param array: List[Int] -- the python list being sorted
    """
    # Your code
    ptr = 0;
    
    while ptr <= len(array)-2:
        mini = array[ptr]
        for i in range(ptr+1,len(array)):
            if array[i] < mini:
                mini = array[i]
        temp = array[ptr]
        array[ptr] = mini
        array[i] = temp
        ptr += 1
        

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))

    print("Before sorting:")
    print(array)
    print("After sorting:")
    selection_sort(array)
    print(array)

    print(array == sorted(array))
if __name__ == '__main__':
    main()
