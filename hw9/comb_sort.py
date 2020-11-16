import random

def comb_sort(array):
    ''' Comb sort uses gap > 1, where bubble sort fixes gap size = 1.
        Start with gap size = len(array) // 1.3, 
        then keep shrinking by 1.3 until gap size reaches 1.

        Once gap size 1 is reached, continue using gap size 1 until the list is completely sorted.

        :param array: the python list being sorted
    '''
    gap = len(array) // 1.3
    swap = None
    
    
    #comb sorting...
    while gap > 1:
        index = 0
        while index + gap < len(array):
            if array[index] > array[int(index+gap)]:
                array[index],array[int(index+gap)] = array[int(index+gap)],array[index]
            index += 1
        gap = gap // 1.3 #shrink gap size
    
    #normal bubble sort, with gap = 1
    while swap != False:
        swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swap = True
            


def main():
    array = []
    for i in range(20):
        array.append(random.randint(-1000, 1000))

    print("Before sorting:")
    print(array)
    comb_sort(array)
    print("After sorting:")
    print(array)
    print("sorted?")
    print(array == sorted(array))
if __name__ == '__main__':
    main()