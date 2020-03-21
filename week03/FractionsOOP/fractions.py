from math import gcd
from operator import attrgetter

class Fraction:
    def __init__(self, nominator, denominator):
        assert denominator >= 1, 'Given zero or negative denominator'
        self.nominator = nominator
        self.denominator = denominator
        self.num = self.nominator/ self.denominator

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'

    def __repr__(self):
        return f'Fraction: {self}'

    def __eq__(self, other):
        return self.nominator / self.denominator == other.nominator / other.denominator

    def  __add__(self, other):
        new_nominator = (self.nominator * other.denominator) + (other.nominator * self.denominator)
        new_denominator = self.denominator * other.denominator

        return Fraction(new_nominator, new_denominator).simplify()
    
    def __float__(self):
        return self.nominator/ self.denominator

    def simplify(self):
        d = gcd(self.nominator, self.denominator)

        return Fraction(self.nominator // d, self.denominator // d)


def sort_fractions(list_of_fractions):
     return sorted(list_of_fractions, key = attrgetter('num'))
 
def main():
    a = [Fraction(2,3), Fraction(1,2), Fraction(1,3)]
    print(sort_fractions(a))

if __name__ == '__main__':
    main()
