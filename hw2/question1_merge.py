def merge(I1, I2):  
    """
    takes two iterable objects and merges them alternately
    required runtime: O(len(I1) + len(I2)).

    :param I1: Iterable -- the first iterable object. Can be a string, tuple, etc
    :param I2: Iterable -- the second iterable object. Can be a string, tuple, etc

    :return: List -- alternately merged I1, I2 elements in a list.
    """      
    if len(I1)<len(I2):
        result = [0]*(2*len(I1))
        for i in range(len(I1)):
            result[2*i]=I1[i]
            result[2*i+1]  =I2[:len(I1)][i]
        for j in I2[len(I1):]:
            result.append(j)
        return result
        
    elif len(I1)>=len(I2):
        result = [0]*(2*len(I2))
        for i in range(len(I2)):
            result[2*i] = I1[i]
            result[2*i+1] = I2[i]
        for j in I1[len(I2):]:
            result.append(j)
            
    
        return result

        



'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print([i for i in merge("what",range(100,105))])
    print([i for i in merge(range(5),range(100,101))])
    print([i for i in merge(range(1),range(100,105))])

if __name__ == '__main__':
    main()