def Sum_multiples(multiple_num,max=1000):
    soma=0
    for item in range(max):
        if (item % multiple_num == 0):
            soma = soma + item
    return soma

print(Sum_multiples(3)+Sum_multiples(5)-Sum_multiples(15))