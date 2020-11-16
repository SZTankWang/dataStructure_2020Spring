def single(inputlist):
    result = inputlist[0]
    for i in inputlist[1:]:
        result ^= i

    return result

list1 = [7,1,5,3,6,4,7,1,5,6,4]

print(single(list1))
