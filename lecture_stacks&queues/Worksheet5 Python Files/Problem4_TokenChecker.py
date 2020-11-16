# Use this stack to perform token checking. No need to modify the stack class.
from exceptions import Empty

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop(-1)

    def __repr__(self):
        return str(self._data)

def check_tokens(filename):
    """
    :param filename: String -- the filename string

    Use a stack!

    :return: True if all "(""[""{""}""]"")" are matching.
             False otherwise.
    """
    # To do
    token = {"(":1,")":2,"{":3,"}":4,"[":5,"]":6}
    Stack = ArrayStack()
    f = open(filename,"r")
    read = f.readlines()
    f.close()
    for line in read:
        for i in line:
            if i not in token:
                continue
            elif token[i] % 2 == 1:
                Stack.push(i)
            elif token[i] % 2 == 0:
                if Stack.is_empty() == False and token[Stack.top()] == token[i]-1:
                    Stack.pop()
                    continue
                else:
                    return False

    return True
                 
                











##############TEST CODES#################
''' Comment out the test code if you are grading on gradescope.'''

def main():
    filename = "test.c"
    print(check_tokens(filename))  ### True

    # You can modify the test.c file to create your own test cases.

if __name__ == '__main__':
    main()



