import sys

def sum_numbers(filename):
	sum_of_num = 0 
	s = []
	with open(filename, 'r') as f:
		s = f.read().split(' ')
		for i in range(0,len(s) - 1):
			sum_of_num += int(s[i])
	return sum_of_num


def  main():
	print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
	main()