def birthday_ranges(birthdays, ranges):
	result = []
	for i in ranges:
		count = 0
		for j in range(i[0], i[1] + 1):
			for l in birthdays:
				if l == j:
					count += 1
		result.append(count)
	return result

def main():
	birthdays = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
	ranges = [(4, 9), (6, 7), (200, 225), (300, 365)]

	print(birthday_ranges(birthdays,ranges))

if __name__ == '__main__':
	main()