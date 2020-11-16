class Empty(Exception):
    ''' Raise this class for exceptions '''
    pass

class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()
        return self.array.pop(-1)

    def __repr__(self):
        return str(self.array)
    
def calculation(a,b,op):
        result = 0
        if op == '+':
            result += (a + b)
        elif op == '-':
            result += (a - b)
        elif op == '*':
            result += (a * b)
        elif op == '/':
            result += (a / b)
        return result

    
    

def evaluate(string):
    """
    :param string: Str -- The string arithmetic expression input

    :return: Float -- the float answer for the given arithmetic expression.
    """
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    table = {"+":2, "-":2, "*":3, "/":3, "(":1, ")":1}
    string_pro = string.split()
    for i in string_pro:
        if i not in table.keys():
            operand_stack.push(int(i))
        elif i == '(':
            operator_stack.push(i)
        elif i == ')':
            while len(operator_stack) >0 and operator_stack.top() != '(':
                op = operator_stack.pop()
                operand0 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = calculation(operand1,operand0,op)
                operand_stack.push(result)
                
            operator_stack.pop()

        elif table[i] > 1:
                if len(operator_stack) > 0:
                    while len(operator_stack) >0 and table[operator_stack.top()]>= table[i]:
                        op = operator_stack.pop()
                        operand0 = operand_stack.pop()
                        operand1 = operand_stack.pop()
                        result = calculation(operand1,operand0,op)
                        operand_stack.push(result)
                    operator_stack.push(i)

                else:
                    operator_stack.push(i)
                    
    while len(operator_stack) > 0:
        op = operator_stack.pop()
        operand0 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = calculation(operand1,operand0,op)
        operand_stack.push(result)
        
    return operand_stack.pop()
                    
                    
            
            
                    
            
            

if __name__ == '__main__':
    print(evaluate("9 + 8 * ( 7 - 6 ) / ( 2 / 8 )"))  #41
    print(evaluate("9 + 8 * 7 / ( 6 + 5 ) - ( 4 + 3 ) * 2"))  # 0.0909090909
    print(evaluate("9 + 8 * 7 / ( ( 6 + 5 ) - ( 4 + 3 ) * 2 )")) # -9.66666666667
     
