class Empty(Exception):
    ''' Raise this class for exceptions '''
    pass

class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()
        return self.array.pop(-1)

    def __repr__(self):
            return str(self.array)
        
def spans1(X):
    '''
    :param X: List[Int] -- list of integers.

    No stack allowed. For each index, 
    we look to the front of array until we find a value that is greater.

    @return: list of span values.
    '''
    span = []
    for i in range(len(X)):   #O(n)
        if i == 0:
            span.append(1)
            continue
        else:
            count = 1
            for j in range(1,i+1):   #O(n)
                if X[i-j]<=X[i]:   #O(1)
                    count += 1
                    continue
                if X[i-j]>X[i]:    ##O(1)
                    break
            span.append(count)
            
    return span
                #the total runtime should be O(n^2)
                    
                
            
        



def spans2(X):
    '''
    :param X: List[Int] -- list of integers.

    Use a stack. We use the stack to compute the span distance.

    If the top of the stack is “Smaller” than the next data, 
    top of the stack should be popped.

    :return: list of span values.
    '''
    S = [0]* len(X)
    A = ArrayStack()
    for i in range(len(X)):   #O(n)
        while A.is_empty() == False and X[A.top()] <= X[i]:   
            #The worst case of this while loop is run n time in one single loop, however, 
            #it's on the assumption that all previous index has not been poped, which means 
            #it should be a descendent sequence, that this while loop has not been operated before
            #So the amortized runtime would still be n/n = 1
            #Run time for this while loop: Amortized O(1)
            A.pop()
        if A.is_empty():
            S[i] = i+1
        else:
            S[i] = i - A.top()
        A.push(i)
    return S

#Total runtime O(n)
        


def main():
    print(spans1([6,3,4,5,2])) # [1, 1, 2, 3, 1]
    print(spans1([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]
    print(spans2([6,3,4,5,2])) # [1, 1, 2, 3, 1]
    print(spans2([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]

if __name__ == '__main__':
    main()

 



        
