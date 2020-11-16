"""
Data Structures Recitation1 Part1
Topic 5 Coding problem #2 Solution
"""
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def evaluate_at(self, x):
        return sum(self.coeffs[-power - 1]*x**power for power in range(len(self.coeffs)))

    def __iadd__(self, otherPoly):
        if len(self.coeffs) > len(otherPoly.coeffs):
            longer, shorter = self.coeffs.copy(), otherPoly.coeffs.copy()
        else:
            longer, shorter = otherPoly.coeffs.copy(), self.coeffs.copy()
        for i in range(len(shorter)):
            longer[-i - 1] += shorter[-i - 1]
        self.coeffs = longer
        return self


    def __str__(self):
        l = [str(self.coeffs[x]) + "x^" + str(len(self.coeffs) - x - 1) + " + " for x in range(len(self.coeffs) - 1)]
        return "".join(l) + str(self.coeffs[-1])


def main():
    # 1x^4 + 2x^3 + 3x^2 + 4x + 5
    coeffs = [1,2,3,4,5]
    poly = Polynomial(coeffs)
    print(poly.evaluate_at(2))   # 57
    print(poly.evaluate_at(3))   # 179
    print(poly)  # Outputs: 1x^4 + 2x^3 + 3x^2 + 4x^1 + 5

    # 4x^3 + 6x^2 + 8x^1 + 10
    coeffs = [4,6,8,10]
    poly2 = Polynomial(coeffs)
    print(poly2)     # Outputs: 4x^3 + 6x^2 + 8x^1 + 10
    poly += poly2
    print(poly)
    
if __name__ == '__main__':
    main()
