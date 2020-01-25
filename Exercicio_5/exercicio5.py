def smalest_multiple(multiplos, *args):
    lst = [*args]
    print("Calculando...\nPode demorar conforme o valor oferecido")
    for num in range(multiplos, 99999999999999, multiplos):
        if all(num % n == 0 for n in lst):
            return num
    return None


if __name__ == '__main__':
    lista = [11, 13, 14, 16, 17, 18, 19, 20]
    valor = smalest_multiple(20, *lista)
    if valor is None:
        print("Não foi encontrado uma solução")
    else:
        print("Foi encontrado e a solução é:", valor)
