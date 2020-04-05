def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def goldbach(num):
    list_of_primes = []
    for i in range(2, num):
        if is_prime(i):
            for l in range(i, num):
                if is_prime(l):
                    if num == i + l:
                        list_of_primes.append((i, l))
    return list_of_primes


def main():
    num = int(input('Enter a number: '))
    print(goldbach(num))


if __name__ == '__main__':
    main()
