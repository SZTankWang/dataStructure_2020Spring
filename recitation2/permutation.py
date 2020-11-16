import timeit
import matplotlib.pyplot as plt
import random

def timeFunction(f,n,repeat=1):
    return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat


def permutation1(N):
    """
    generate a random permutation from 0 to N-1. 

    :param N: Int - The boundary integer.
    :return: List -- A list of integers from 0 to N - 1. Random permutation.
    """
    array = [0] * N
    '''
    for i in range(len(array)):
        candidate = random.randint(0,N-1)
        while candidate in array[:i]:
            candidate = random.randint(0,N-1)
        array[i] = candidate
    return array
'''
    i = 0
    while i < N:
        ran = random.randint(1,N)
        if ran not in array[:i]:
            array[i] = ran
            i += 1
        else:
            continue
    return array
    

        
        
        
        
            

    


def permutation2(N):
    """
    generate a random permutation from 0 to N-1. 

    :param N: Int -- The boundary integer.
    :return: List -- A list of integers from 0 to N - 1. Random permutation.
    """
    used = [0]*N
    array = [0]*N
    for i in range(len(array)):
        ran = random.randint(0,N-1)
        while used[ran] == True:
            ran = random.randint(0,N-1)
        array[i] = ran
        used[ran] = True
    return array
        
            
            
        
    
    

def permutation3(N):
    """
    generate a random permutation from 0 to N-1. 

    :param N: Int -- The boundary integer.
    :return: List -- A list of integers from 0 to N - 1. Random permutation.
    """
    array = [i for i in range(N)]
    for i in range(len(array)):
        random_index = random.randint(0,i)
        array[i],array[random_index] = array[random_index],array[i]
    return array
        
        

def plot_data():
    x = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
    y = []
    z = []
    j = []
    for each in x:
        y.append(timeFunction(permutation1, each))
        z.append(timeFunction(permutation2, each))
        j.append(timeFunction(permutation3, each))
    line1, = plt.plot(x, y, label="permutation1")
    plt.legend()
    line2, = plt.plot(x, z, label="permutation2")
    plt.legend()
    line3, = plt.plot(x, j, label="permutation3")
    plt.legend(handles=[line1,line2,line3])
    plt.xlabel("Input Size")
    plt.ylabel("Run time -- Seconds")
    plt.show()

if __name__ == '__main__':
    plot_data()

        
