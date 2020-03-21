from polynomials import Term, Polynomial
import sys

def print_properly(answer):
	print(f"The derivative of f(x) = {sys.argv[1]} is:")
	print(f"f'(x) = {answer}")

if __name__ == '__main__':
	main()
