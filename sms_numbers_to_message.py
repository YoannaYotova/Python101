dic = {'2': 'a', '22': 'b', '222': 'c',
	   '3': 'd', '33': 'e', '333': 'f',
	   '4': 'g', '44': 'h', '444': 'i',
	   '5': 'j', '55': 'k', '555': 'l',
	   '6': 'm', '66': 'n', '666': 'o',
	   '7': 'p', '77': 'q', '777': 'r', '7777': 's',
	   '8': 't', '88': 'u', '888': 'v',
	   '9': 'w', '99': 'x', '999': 'y', '9999': 'z',

	   '0': ' '
	   }

l = [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3 ,3 ,0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]

def group(pressed_sequence):
	el = l[0]
	new_list1=[]
	res = []
	for i in l:
		if i == el:
			new_list1.append(i)
		else:
			el = i
			res.append(new_list1)
			new_list1=[]
			new_list1.append(i)

	res.append(new_list1)
	return res


def num_into_message(pressed_sequence):
	new_list = group(l)
	capital_letter = False
	message = ''
	for i in new_list:
		char = "".join(str(d) for d in i)
		if char == '-1':
			continue
		elif char in dic:
			if capital_letter == True:
				message += dic[char].capitalize()
				capital_letter = False
			else:
				message += dic[char]
		elif char == '1':
			capital_letter = True
		elif len(char) % 3 != 0 and char[0] != '7' and char[0] != '9':
			new_char = ''
			for i in range(0, len(char) % 3):
				new_char += char[0]

			if capital_letter == True:
				message += dic[new_char].capitalize()
				capital_letter = False
			else:
				message += dic[new_char]
		else:
			new_char = ''
			for i in range(0, len(char) % 4):
				new_char += char[0]

			if capital_letter == True:
				message += dic[new_char].capitalize()
				capital_letter = False
			else:
				message += dic[new_char]
	return message

def main():
	print(num_into_message(l))


if __name__ == '__main__':
	main()





