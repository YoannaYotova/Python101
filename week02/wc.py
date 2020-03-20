import sys
def count(argument, word):
	count= 0
	if word == 'chars':
		with open(argument,'r') as f:
			count = len(f.read())
		return count
	if word == 'words':
		with open(argument,'r') as f:
			count = len(f.read().split())
		return count
	if word == 'lines':
		with open(argument,'r') as f:
			for i in f:
				count += 1
		return count



def main():
	print(count(sys.argv[2],sys.argv[1]))

if __name__ == '__main__':
	main()