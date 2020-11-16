import random

def bubble_sort(array):
    """ Compares each pair of adjacent items and swaps them if they are in the wrong order. 
        :param array: the python list being sorted
    """
    # Your code
    swap = None
    while swap != False:
        swap = False
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i-1],array[i] = array[i],array[i-1]
                swap = True
    

    

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-1000, 1000))

    print("Before sorting:")
    print(array)
    bubble_sort(array)
    print("After sorting:")
    print(array)
    print("sorted?")
    print(array == sorted(array))
if __name__ == '__main__':
    main()