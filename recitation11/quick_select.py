import random

def quick_select(array, k):
    """ Return the kth smallest element of array, for k from 1 to len(array).
        :param array: List[Int] -- select kth smallest element from it.
        :param k:     Int -- kth smallest, ranging from 1 to len(array)

        return: value of kth smallest element within array
    """
    # To do
    
    #randomly pick a pivot
    
    #pay attention to special case
    if len(array) <1:
        return None
    if len(array) == 1:
        return array[0]
    
    length = len(array)
    rand = random.randint(0, length-1)
    pivot = array[rand]
    
    L = []
    E = []
    G = []
    
    for i in array:
        if i < pivot:
            L.append(i)
        elif i == pivot:
            E.append(i)
        else:
            G.append(i)
            
    if len(L) >= k:
        return quick_select(L,k)
    elif len(L)+len(E) == k:
        return pivot
    else:
        j = k-len(L)-len(E)
        return quick_select(G,j)

def main():
    array = []
    for i in range(20):
        array.append(random.randint(-100, 100))
    print(array)
    k = random.randint(1,20)
    print("Selecting:", k,"th element......")
    print("Your result is:", quick_select(array, k))

    array.sort()
    print("Correct result should be:", array[k - 1])

if __name__ == '__main__':
    main()