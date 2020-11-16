import copy

#this function is derived from the original kanpsack, where we could determine 
#that among the sublist we obtained from previous recursion, which one should 
#continue to be passed, as well as generating new sublist that satisfy the requirement
#That is, the sum of the new sublist should be no larger than the capacity.
#If we have reached the end of the recursion's returning process, we remove all
#non-satisfying elements.
def sublist_to_pick(target,previous,l,time):
        temp = copy.deepcopy(previous)
        for i in temp:
            if sum(i) > target:
                previous.remove(i)
            elif sum(i) < target:
                new_sum = sum(i) + l[0]
                if time > 0:
                    if new_sum <= target:
                        temp = copy.deepcopy(i)
                        temp.append(l[0])
                        previous.append(temp)
                    else:
                        continue
                else:
                    if new_sum < target:
                        previous.remove(i)
                    elif new_sum == target:
                        temp = copy.deepcopy(i)
                        temp.append(l[0])
                        previous.remove(i)
                        previous.append(temp)
                    else:
                        previous.remove(i)
            elif sum(i) == target:
                continue
        return previous

    
def knapsack(target,time,l):
    if len(l) == 1:
        if l[0] > target:
            return []
        else:
            return [l]
    
    else:
        previous = knapsack(target,time+1,l[1:])
        if l[0] == target:
            previous.append([l[0]])
            return previous
        else:
            sublist_to_pick(target,previous,l,time)
            if l[0] < target and time > 0:
                previous.append([l[0]])
            return previous



def main():   
    casts = [1, 2, 8, 4, 9, 1, 4, 5]
    # order does not matter, inner values order doesn't matter either.
    # [[9, 5], [9, 1, 4], [4, 1, 4, 5], [4, 9, 1], [8, 1, 5], [2, 8, 4], [2, 8, 4], [1, 9, 4], [1, 4, 4, 5], [1, 4, 9], [1, 8, 5], [1, 8, 1, 4], [1, 8, 4, 1]]
    print(knapsack(14, 0, casts))  

if __name__ == '__main__':
    main()

