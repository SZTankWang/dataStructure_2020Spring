from probe_hash_map import ProbeHashMap

def l1_contains_l2(l1, l2):
    dic1 = ProbeHashMap()


    for i in range(len(l1)):
        dic1[l1[i]] = i
    
    is_sub = True
    for j in range(len(l2)):
        if l2[j] not in dic1:
            is_sub = False
    return is_sub


def dic(l):
    dic = ProbeHashMap()
    for i in range(len(l)):
        dic[l[i]] = i
    return dic

def main():
    l1 = [1,2,3,4,5,6,7,8,9,0]
    l2 = [5,2,8,9,0,1]
    l3 = [5,2,8,9,0,1,"haha"]
    #print(("haha" in dic(l1)) == False)
    print("l2 should be subset of l1........")
    print("Your result:", l1_contains_l2(l1, l2))
    print("l3 should not be subset of l1........")
    print("Your result:", l1_contains_l2(l1, l3))
    
    
    
main()


