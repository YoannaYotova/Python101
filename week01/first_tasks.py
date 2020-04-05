#Sum of all digits of a number
n = -10
if n < 0:
    n = n * (-1)


def sum_of_digits(n):
    string = str(n)
    sum = 0
    for digit in string:
        sum = sum + int(digit)

    return sum


print(sum_of_digits(n))


# Turn a number into a list of digits
n = 99999
lst = []


def to_digit(n):
    string = str(n)
    for i in string:
        lst.append(int(i))
    return lst


print(to_digit(n))

print([int(i) for i in str(n)])


# Turn a list of digits into a number
digits = [21, 2, 33]

newl = "".join([str(i) for i in digits])
print(int(newl))
print(int("".join([str(d) for d in digits])))

# Factorial Digits
n = 145


def fact_digits(n):
    sum = 0
    string = str(n)
    for digit in string:
        f = 1
        sub = 1
        for fact in range(int(digit)):
            sub *= f
            f += 1
        sum += sub
    return sum


print(fact_digits(n))

# Palindrome
string = "baba"


def palindrome(string):
    newstr = ""
    converToStr = str(string)
    for i in converToStr:
        newstr = i + newstr
    if newstr == converToStr:
        print("True")
    else:
        print("False")


palindrome(string)

# Vowels in a string
str = "Python"


def count_vowels(str):
    new_str = str.lower()
    # print(str)
    # print(new_str)
    count = 0
    for i in new_str:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y'):
            count += 1
    return count


print(count_vowels("A nice day to code!"))

# Consonants in a string
str = "Python"


def count_consonants(str):
    new_str = str.lower()
    # print(str)
    # print(new_str)
    count = 0
    for i in new_str:
        if(i >= 'a' and i <= 'z'):
            if(i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'y'):
                count += 1
    return count


print(count_consonants("A nice day to code!"))

# Char Histogram
str = "Python!"
count = {}
dic = {}


def char_histogram(str):
    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key in count:
        if count[key] >= 1:
            dic.update({key: count[key]})
    return dic


print(char_histogram(str))

# Sum Numbers in Matrix
m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


def sum_matrix(m):
    s = 0
    for i in m:
        s += sum(i)
    return s


print(sum_matrix(m))

# NaN Expand
n = 2
strNaN = ""
if n == 0:
    print("\"\"")
    exit()


def nan_expand(n):
    global strNaN
    new_str = "Not a "
    if n > 0:
        strNaN += new_str
        n -= 1
        nan_expand(n)
    return strNaN + "NaN"


res = nan_expand(n)
print("\"" + res + "\" ")


# Integer prime factorization
import math

n = 100
l = []
count = 0


def prime_factorization(n):
    global count
    while n % 2 == 0:
        count += 1
        n = n // 2
    if count != 0:
        l.append((2, count))
    for i in range(3, int(math.sqrt(n) + 1), 2):
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count != 0:
            l.append((i, count))
    # condition if n is a prime number
    if n > 2:
        l.append((n, 1))
    t = tuple(l)
    new_list = list(t)
    return new_list


print(prime_factorization(n))


# The group function
l = [1, 1, 2, 2, 3, 1, 1]


def group(l):
    el = l[0]
    new_list1 = []
    res = []
    for i in l:
        if i == el:
            new_list1.append(i)
        else:
            el = i
            res.append(new_list1)
            new_list1 = []
            new_list1.append(i)

    res.append(new_list1)
    return res


print(group(l))


# Longest subsequence of equal consecutive elements
list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]


def max_consecutive(list):
    max_count = 0
    count = 0
    el = list[0]
    for i in list:
        if i == el:
            count += 1
        else:
            el = i
            count = 1
        if count > max_count:
                max_count = count
    return max_count


print(max_consecutive(list))
