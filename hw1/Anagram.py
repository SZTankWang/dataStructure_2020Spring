def anagram(string1, string2):
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """
    # To do
    list1 = []
    list2 = []
    for i in string1:
        if i != ' ':
            list1.append(i)
    for i in string2:
        if i != ' ':
            list2.append(i)
    if set(list1)^set(list2) == set():
        return True
    return False

'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    string1 = "william shakespeare"
    string2 = "i am a weakish speller"
    print(anagram(string1, string2))   

    string1 = "software"
    string2 = "swear oft"
    print(anagram(string1, string2))  

if __name__ == '__main__':
    main()
