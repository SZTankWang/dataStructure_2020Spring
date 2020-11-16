def is_vowel(string):
    vowel = {'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
    if vowel.get(string) == 0:
        return True
    return False





def vc_count(word):
    """
    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!
    
    :param word: String -- the input string
    :return: List[Int] -- the first integer is the number of vowels, 
                          the second integer is the number of consonants.
    """
    if len(word) == 0:
        return [0,0]
    else:
        previous = vc_count(word[1:])
        if is_vowel(word[0]):
            previous[0] += 1
            return previous
        else:
            previous[1] += 1
            return previous
    

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

if __name__ == '__main__':
    main()
