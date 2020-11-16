class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        if denominator != 0:  
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def __add__(self, other):
        """
        create and return a new Fraction object, which is the sum of self + other. 
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the sum of self + other.
        """             
        new_denominator = self.denominator*other.denominator
        new_numerator = self.numerator*other.denominator + other.numerator*self.denominator
        return Fraction(new_numerator,new_denominator)
                       

    def __iadd__(self, other):
        """
        modify the self Fraction object, which adds other Fraction object value to self.

        :param other: Fraction -- the other fraction number.
        :return: self. The value of self should become the sum of self + other.
        """
        self.numerator = self.numerator*other.denominator + other.numerator*self.denominator
        self.denominator = other.denominator*self.denominator
        return self

    def __sub__(self, other):
        """
        create and return a new Fraction object, which is the subtraction of self - other. 
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the subtraction of self - other.
        """
        new_numerator = self.numerator*other.denominator - other.numerator*self.denominator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)

    def __mul__(self, other):
        """
        create and return a new Fraction object, which is the multiplication of self * other. 
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the multiplication of self * other.
        """
        new_numerator = self.numerator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator,new_denominator)

    def __eq__(self, other):
        """
        Compare if self Fraction object has equal numerical value to the other Fraction object.
        Example: 2/3 == 4/6 --> True
                 2/3 == 2/3 --> True
        If you use the reduce() function here, it is fine.

        :param other: Fraction -- the other fraction number.

        :return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        """
        value_self = self.numerator/self.denominator
        value_other = other.numerator/other.denominator
        if value_self == value_other:
            return True
        
        return False
    
    def factor(self,numer,denom):
        factor = []
        for i in range(1,numer+1):
            if numer%i == 0 and denom%i == 0:
                factor.append(i)
        return factor
            

    def reduce(self):
        """
        Reduces (Simpilifies) the self Fraction object. 
        Modifies both self.numerator and self.denominator.
        For example: 12 / 24 --> 1 / 2;  16 / 20 --> 4 / 5

        :return: Nothing.
        """
        factors = self.factor(self.numerator,self.denominator)
        if len(factors) != 0:
            factor = factors[len(factors)-1]
        self.numerator = self.numerator/factor
        self.denominator = self.denominator/factor
        

    def __str__(self):
        """
        Displays the self Fraction object nicely. 
        Recommended format:
        Suppose,
        self.numerator = 5
        self.denominator = 6
        Then, should return "5 / 6"

        :return: The string representation of self Fraction object.
        """
        return str(int(self.numerator))+ ' / '+ str(int(self.denominator))



'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    x = Fraction(3, 4)
    y = Fraction(4, 6)
    #x += y
    #print(x)
    
    print(x)        # 3 / 4
    print(y)        # 4 / 6
    print(x + y)    # 34 / 24 or any value that is equal
    z = x + y
    print(x * y)    # 12 / 24 or any value that is equal
    print(x - y)    # 2 / 24 or any value that is equal
    y.reduce()
    print(y)        # 2 / 3
    z.reduce()
    print(z)        # 17 / 12

    print(z == Fraction(-17, -12))  # True
    print(z == Fraction(51, 36))  # True
    print(z == Fraction(-7, 4))   # False
    
    
if __name__ == '__main__':
    main()
