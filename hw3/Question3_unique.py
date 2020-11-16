def unique(s):
    """
    :param s: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    if len(s) == 1:
        return True
    else:
        for i in s[1:]:
            if s[0] == i:
                return False
        return unique(s[1:])
    

def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True

if __name__ == '__main__':
    main()

