
def is_prime(value):
    bound = value // 2
    for n in range(2,bound + 1):
        if value % n == 0:
            return False
    return True

def is_funny(value):
    bound = value // 2
    factors = set()
    field = {2,3,5}
    for n in range(2,bound + 1):
        if value % n == 0:
            factors.add(n)
    if factors.issubset(field):
        return True
    return False

num = 21
print(is_funny(num))



