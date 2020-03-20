def sum_of_numbers(string):
	temp_str = ""
	res = 0
	for i in string:
		if i.isdigit():
			temp_str += i
		elif len(temp_str) != 0:
			res += int(temp_str)
			temp_str = ""
	if len(temp_str) != 0:
		res += int(temp_str)
	return res

def main():
	string = "1110"
	print(sum_of_numbers(string))

if __name__ == '__main__':
	main()

