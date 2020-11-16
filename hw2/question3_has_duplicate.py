def has_duplicate(list1):
    """
    remember to mention your runtime as comment!

    :param l: List -- list of integers
    :return: True if list1 has duplicate, return False otherwise.
    """
    mem = {}  #----O(1)
    for n in list1:    #-----This for loop has O(n) runtime
        if n in mem:
            mem[n] += 1 #----O(1)
        else:
            mem[n] = 1  #----O(1)
    for i in mem.values(): #------This for loop has another O(n) runtime
        if i != 1:
            return True  #----O(1)
    return False

###In all, the program has an O(n) runtime
    

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(has_duplicate([0,6,2,4,9]))   # False

    print(has_duplicate([0,6,2,4,9,1,2]))   # True

if __name__ == '__main__':
    main()