#Given an array of integers, the majority number is the number that occurs more than half of 
#the size of the array. Write a function to find the majority number.

def major_number(array):
    memo = {}
    count = 1
    length = len(array)
    for i in array:
        if i not in memo:
            memo[i] = count
        else:
            memo[i] += 1
    for n in memo.keys():
        if memo[n] > length//2:
            return n
test_array = [1,1,1,1,2,2,3]    
print(major_number(test_array))

            