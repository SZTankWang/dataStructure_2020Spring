#1. 从未排好的序列中拿出首元素，并把它赋值给key变量；
#2. 从排好的序列中，依次与key进行比较，如果元素比key大，则将元素后移（实际上放置key的元素位置已经空出）
#3. 直到找到一个元素比key小， 将key放入该位置；

def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i] 
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

array = [1,2,3,6,4,5]
print(insertion_sort(array))





        

                