# =============================================================================
# def binary_search(lst,value):
#     if len(lst) == 1:
#         if lst[0] == value:
#             return True
#         else:
#             return False
#     else:
#         start = 0
#         end = len(lst)
#         index = (start + end) // 2
#         if lst[index] == value:
#             return True
#         elif lst[index] > value:
#             return binary_search(lst[:index],value)
#         else:
#             return binary_search(lst[index+1:],value)
#         
# =============================================================================
# =============================================================================
# lst = [1,2,3,4,5,6]
# print(binary_search(lst,2))
# 
# =============================================================================
def search(mtx,value):
    low = 0
    high = len(mtx)*len(mtx[0])-1
    while low <= high:
        pivot = (low+high) //2
        target = mtx[pivot//len(mtx[0])][pivot%len(mtx[0])]

        if target > value:
            high = pivot -1
        elif target < value:
            low = pivot +1
        else:
            return True




mtx = [[1,3,5,7],
       [10,11,16,20],
        [23,30,34,50]]

print(search(mtx,16))

