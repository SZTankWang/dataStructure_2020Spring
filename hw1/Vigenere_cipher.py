def vigenere_encrypt(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    dict_raw = ['A','B','C','D','E','F','G','H','I','J','K',
                'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if len(plain) >= len(key):
        new_key = key*(len(plain)//len(key)) + key[:len(plain)%len(key)]
    else:
        new_key = key[:len(plain)]
    encrypt = ''
    for i in range(len(plain)):
        order = dict_raw.index(plain[i])
        dict_crypt = dict_raw[order:]+dict_raw[:order]
        encrypt_order = dict_raw.index(new_key[i])
        encrypt += dict_crypt[encrypt_order]
    return encrypt
        
        
    
    

def vigenere_decrypt(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    # To do
    dict_raw = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    if len(cipher) >= len(key):
        new_key = key*(len(cipher)//len(key)) + key[:len(cipher)%len(key)]
    else:
        new_key = key[:len(cipher)]
    decrypt = ''
    for i in range(len(cipher)):
        order = dict_raw.index(new_key[i])
        dict_key = dict_raw[order:]+dict_raw[:order]
        decrypt_order = dict_key.index(cipher[i])
        decrypt += dict_raw[decrypt_order]
    return decrypt
        
        

    


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL

    print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY

    print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM

    print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW

    print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
    print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
    print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE

if __name__ == '__main__':
    main()
