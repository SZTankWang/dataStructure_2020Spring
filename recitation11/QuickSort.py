def find_median(array):
    #takes an array of 3 integers
    
    max_index = 0
    for i in range(len(array)):
        if array[i] > array[max_index]:
            
            max_index = i
            
    array[max_index],array[-1] = array[-1],array[max_index]
    array.pop()
    return max(array)
        

def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return                                      # range is trivially sorted
    #pivot = S[b]                                           # last element of range is pivot
    #left = a                                               # will scan rightward
    #right = b-1                                            # will scan leftward
    
    lst = [S[a],S[b],S[(a+b)//2]]
    
    ##make sure the head, tail, and median are in order
    S[a] = min(lst)
    S[b] = max(lst)
    S[(a+b)//2] = find_median(lst)
    
    ##swap median with the last element, in order to get it out of the way
    S[b],S[(a+b)//2] = S[(a+b)//2],S[b]
    
    #pick pivot, left ptr, right ptr
    pivot = S[b]
    left = a
    right = b-1
    
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                                    # scans did not strictly cross
            S[left], S[right] = S[right], S[left]              # swap values
            left, right = left + 1, right - 1                  # shrink range
            
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

def main():
    import random
    S = []
    for i in range(10):
        S.append(random.randint(-100, 100))

    print(S)
    inplace_quick_sort(S, 0, len(S) - 1)
    print(S)
    print("Is S sorted???", S == sorted(S))
    
if __name__ == '__main__':
    main()
