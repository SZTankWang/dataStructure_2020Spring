#Given a 32-bit signed integer, return the reversed digits of this integer.

def get_digit(value):
    digit = 1
    num = abs(value)
    while num // 10 > 0:
        num = num // 10
        digit += 1
    return digit

#print(get_digit(1234))

def reverse(value):
    length = get_digit(value)
    res = abs(value)
    output = 0
    print(length)
    for i in range(1,length+1):
        print(i,'th operation')
        print('when this operation begin, res is',res)
        new_digit = res % 10
        print('new digit is ', new_digit)
        res = res // 10
        print('res is ',res)
        output += new_digit * (10**(length - i))
        print('output is now', output)
    if value >= 0:
        return output
    else:
        return -output

    

print(reverse(3421))





