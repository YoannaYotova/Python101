def is_even_count_of_digits(number):
	global str_num
	if len(str_num) % 2 == 0:
		return True
	else:
		return False

def is_number_balanced(number):
	global str_num
	list_with_digits = [int(i) for i in str_num]
	if is_even_count_of_digits(number):
		sum_left = sum(list_with_digits[:len(str_num)//2])
		sum_right = sum(list_with_digits[len(str_num)//2:])
	else:
		sum_left = sum(list_with_digits[:len(str_num)//2])
		sum_right = sum(list_with_digits[len(str_num)//2 + 1:])
	if sum_right == sum_left:
		return True
	else:
		return False

def main():
	number = 1238033
	str_num = str(number)
	print(is_number_balanced(number))

if __name__ == '__main__':
	main()
