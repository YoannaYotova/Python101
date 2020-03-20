def checking_for_zero_denominator(fractions):
	for i in fractions:
		if i[1] == 0:
			raise ZeroDivisionError('Cannot devide by zero')

def sort_fractions(fractions, ascending = True):
	if len(fractions) <= 1:
		return fractions
	else:
		if ascending == True:
			checking_for_zero_denominator(fractions)
			return sorted(fractions, key = lambda tup: (tup[0]/tup[1]))
		else:
			checking_for_zero_denominator(fractions)
			return sorted(fractions, key = lambda tup: (tup[0]/tup[1]), reverse = True)


def mina():
	print(sort_fractions([(2,3), (1,2)]))

if __name__ == '__main__':
	main()
	