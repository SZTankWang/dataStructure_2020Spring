import random


def insertion_sort(array):
    """ Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. 
        :param array: the python list being sorted
    """
    # To do
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >=0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-1000, 1000))

    print("Before sorting:")
    print(array)
    insertion_sort(array)
    print("After sorting:")
    print(array)
    print("sorted?")
    print(array == sorted(array))

if __name__ == '__main__':
    main()
