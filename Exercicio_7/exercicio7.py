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


def th_prime_number(position):
    i_position = 0
    i = 1
    while i_position != position:
        print("Posição:", i_position, "i:", i)
        i += 1
        if is_prime(i):
            i_position += 1
    return i


if __name__ == '__main__':
    print(th_prime_number(10001))
