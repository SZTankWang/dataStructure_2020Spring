def pascal(n):
    """
    :param n: Int -- Levels of pascal triangle

    :return: List[List[Int]] -- a list of sublists, which contains pascal values.
    """
    if n == 1:
        return [[1]]
    else:
        previous = pascal(n-1)
        if n == 2:
            initial = [1,1]
            previous.append(initial) # writing result = previous.append(x) would lead to nonetype error.
            return previous
            
        elif n > 2:
            initial = [0]*n
            for i in range(1,n-1):
                initial[i] = previous[n-2][i-1]+previous[n-2][i]
            initial[0] = 1
            initial[-1] = 1
            previous.append(initial)
            return previous
            

def main():
    print(pascal(5))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

if __name__ == '__main__':
    main()




