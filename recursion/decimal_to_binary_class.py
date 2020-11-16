# Suppose n is a positive integer, n >= 0 .
# Convert n to its binary representation without using any library function.

def recursive_decimal_to_binary_str(n):
    # To do
    result = ''
    if n == 0:
        return result
    else:
        result = recursive_decimal_to_binary_str(n//2)
        return result + str(n%2)





def main():
    print(recursive_decimal_to_binary_str(6)) #110
    print(recursive_decimal_to_binary_str(13)) #1101
    print(recursive_decimal_to_binary_str(126)) #1111110
    print(recursive_decimal_to_binary_str(509)) #111111101
    
	
if __name__ == '__main__':
    main()
