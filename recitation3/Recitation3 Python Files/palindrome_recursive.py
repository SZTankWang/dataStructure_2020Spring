def palindrome_recursive(string, index):
    """
    # Complete the palindrome algorithm --- with recursion
    # Think about how to break a large problem into smaller sub problems.
    What is our base case in this problem?

    # Another way to ask: what is our smallest problem?
    How to get to this smallest problem?

    :param string: String -- the string to check whether it is a palindrome
    :param index: Int -- additional parameter for recursion tracking

    :return: True if @string is palindrome, False otherwise
    """
    if index >= len(string)//2 - 1 and string[index] == string[len(string)-1-index]:
        return True
    elif index<len(string)//2 - 1 and string[index] == string[len(string)-1-index]:
        return palindrome_recursive(string,index+1)
    else:
        return False
        


    


def main():
    s1 = "nodevillivedon"
    s2 = "livenoevil!liveonevil"
    s3 = "beliveivileb"
    s4 = "ab!ba"
    r1 = palindrome_recursive(s1, 0)
    r2 = palindrome_recursive(s2, 0)
    r3 = palindrome_recursive(s3, 0)
    r4 = palindrome_recursive(s4, 0)

    print("s1 is", r1)  # Should be True
    print("s2 is", r2)  # Should be True
    print("s3 is", r3)  # Should be False
    print("s4 is", r4)

main()

    
