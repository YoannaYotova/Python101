from polynomials import Term, Polynomial
from utls import print_properly
import sys

def main():
    derivative = Polynomial.print_derivative()
    print_properly(derivative)

if __name__ == '__main__':
	main()