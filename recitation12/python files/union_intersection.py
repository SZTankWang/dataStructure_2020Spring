def union(l1, l2):
    """
        :param l1: List[Int] -- the first python list
        :param l2: List[Int] -- the second python list
        
        Return a new python list of the union of l1 and l2.
        Order of elements in the output list doesn’t matter.
        Use python built in dictionary for this question.

        return: union of l1 and l2, as a SingleLinkedList.
    """
    # To do
    dic = dict()
    union = []
    
    for i in l1:
        if i not in dic:
            dic[i] = 0
            union.append(i)
    
    for j in l2:
        if dic.get(j) == None:
            dic[j] = 0
            union.append(j)
            
    return union
    

def intersection(l1, l2):
    """
        :param l1: List[Int] -- the first python list
        :param l2: List[Int] -- the second python list
        
        Return a new python list of the intersection of l1 and l2.
        Order of elements in the output list doesn’t matter.
        Use python built in dictionary for this question.

        return: intersection of l1 and l2, as a SingleLinkedList.
    """
    # To do
    dic = dict()
    inter = []
    
    for i in l1:
        if i not in dic:
            dic[i] = 0
    
    for j in l2:
        if dic.get(j) != None:
            inter.append(j)
    return inter


def main():
    l1 = [10, 15, 4, 20]

    l2 = [8, 4, 2, 10]


    print(union(l1, l2), "||||should contain [10,15,4,20,8,2], order doesn't matter.")
    print(intersection(l1, l2), "||||should contain [4, 10], order doesn't matter.")

main()
    
