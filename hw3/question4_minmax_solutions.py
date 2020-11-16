import sys

def minmax(list1):
    minimum = sys.maxsize
    maximum = -sys.maxsize

    for i in range(len(list1) // 2):     # Compare in pairs
        if (list1[2*i] > list1[2*i + 1]):     # O(n/2)
            smaller = list1[2*i + 1]
            larger = list1[2*i]
        else:
            smaller = list1[2*i]
            larger = list1[2*i + 1]
        if minimum > smaller:                       # O(n/2)
            minimum = smaller
        if maximum < larger:                        # O(n/2)
            maximum = larger
    return minimum, maximum


'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(minmax([150, 24, 79, 50, 98, 88, 345, 3]))    # (3, 345)
    print(minmax([678, 227, 764, 37, 956, 982, 118, 212, 177, 597, 519, 968, 866, 121, 771, 343, 561, 100]))  # (37, 982)

if __name__ == '__main__':
    main()