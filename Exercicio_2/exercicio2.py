def fibonacci_sum_even(maximo):
    first = 1
    second = 2
    third = 2
    soma = 0
    while second < maximo:
        if third % 2 == 0:
            soma += third
        third = second + first
        first = second
        second = third
    return soma


print(fibonacci_sum_even(4000000))
