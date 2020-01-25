def is_prime(number):
    i = 1
    cont = 0
    while cont < 2 and i <= number / 2:
        if number % i == 0:
            cont += 1
        i += 1
    if cont == 2:
        return False
    else:
        return True


def largest_prime(number):
    last = 1
    i = 1
    if is_prime(number):
        return False
    while i <= number / 2 and (i - last) <= 10000:
        print("i:", i, "       last:", last)
        if (number % i == 0) and (is_prime(i)):
            last = i
        i += 1
    return last


number = 600851475143
print("Maior numero primo:", largest_prime(number), "\nÉ primo ou não:", is_prime(number))
