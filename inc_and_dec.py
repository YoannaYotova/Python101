def increasing_or_decreasing(seq):
	first_step = seq[1] - seq[0]
	for i in range(2,len(seq)):
		step = seq[i] - seq[i - 1]
		if step != first_step or step == 0:
			return False
		elif step > 0:
			return 'Up!'
		else:
			return 'Down!'

def main():
	seq = [9,8,7,6]
	print(increasing_or_decreasing(seq))

if __name__ == '__main__':
	main()