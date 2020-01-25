def soma_dos_quadrados(maximo):
    soma = 0
    for valor in range(1, (maximo + 1), 1):
        soma += valor.__pow__(2)
    return soma


def quadrado_da_soma(maximo):
    soma = 0
    for valor in range(1, (maximo + 1), 1):
        soma += valor
    return soma.__pow__(2)


def diferenca(valor):
    return quadrado_da_soma(valor) - soma_dos_quadrados(valor)


if __name__ == '__main__':
    print(diferenca(100))
