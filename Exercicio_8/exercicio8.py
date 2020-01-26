def greatest_product_series(string, maximo=13):
    if (type(string) is "<class 'str'>") or (len(string) < maximo):
        return None
    print("Verificando aguarde...")
    resul = 1
    resul_ago = 0
    length_text = len(string)
    for x in range((length_text - maximo + 1)):
        resul = 1
        print("\n")
        for n in range(maximo):
            print(int(string[x + n]))
            resul *= int(string[n + x])
        if resul > resul_ago:
            resul_ago = resul
    return resul_ago


if __name__ == '__main__':
    arquivo = open("C:/Users/asd/Desktop/numeros.txt", "r")
    texto = arquivo.read()
    print(type(texto))
    print("Resultado", greatest_product_series(texto))
    arquivo.close()
