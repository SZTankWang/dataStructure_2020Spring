import random
def binary_search_rec(x, sorted_list):
    # this function uses binary search to determine whether an ordered array
    # contains a specified value.
    # return True if value x is in the list
    # return False if value x is not in the list
    # If you need, you can use a helper function.
    # TO DO
    low = 0
    high = len(sorted_list)-1
    if low == high:
        if sorted_list[low] == x:
            return True
        else:
            return False
    if len(sorted_list) == 0:
        return False
    
    else:
        mid_value = len(sorted_list) // 2
        if sorted_list[mid_value] == x:
            return True
        elif sorted_list[mid_value] > x:
            sorted_list = sorted_list[:mid_value]
            return binary_search_rec(x,sorted_list)
        elif sorted_list[mid_value] < x:
            sorted_list = sorted_list[mid_value+1:]
            return binary_search_rec(x,sorted_list)

        
    
   

def binary_search_iter(x, sorted_list):
    # TO DO
    # return True if value x is in the list
    # return False if value x is not in the list
    low = 0
    high = len(sorted_list)-1
    find = False
    while low <= high and find == False:
        mid_value = (low+high)//2
        if sorted_list[mid_value] == x:
            find = True
        elif sorted_list[mid_value] > x:
            high = mid_value-1
        elif sorted_list[mid_value] < x:
            low = mid_value +1
    return find
            
            
        
    
 



def main():
    sorted_list = []
    for i in range(100):
        sorted_list.append(random.randint(0, 100))
    sorted_list.sort()

    print("Testing recursive binary search ...")
    for i in range(5):
        value = random.randint(0, 100)
        answer = binary_search_rec(value, sorted_list)
        if (answer == True):
            print("List contains value", value)
        else:
            print("List does not contain value", value)

    print("Testing iterative binary search ...")
    for i in range(5):
        value = random.randint(0, 100)
        answer = binary_search_iter(value, sorted_list)
        if (answer == True):
            print("List contains value", value)
        else:
            print("List does not contain value", value)
    
main()









