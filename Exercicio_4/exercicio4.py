def is_palindromic(number):
    iguais = 0
    number_str = str(number)
    tam = int(len(number_str))
    meio_tam = int(tam / 2)
    for item in range(meio_tam):
        if number_str[item] == number_str[(tam-1-item)]:
            iguais += 1
    if iguais == meio_tam:
        return True
    else:
        return False


maximo = 999
x = 99
y = 99
x_global = 0
y_global = 0
resul = 0
resul_ago = 0
print("Procurando o número... \nPode demorar um tempo")
for valor_x in range(maximo, x, -1):
    for valor_y in range(maximo, y, -1):
        resul = valor_y * valor_x
        if is_palindromic(resul) and resul > resul_ago:
            x_global = valor_x
            y_global = valor_y
            resul_ago = resul

print("\nPronto o seu resultado é:", resul_ago)
print("Tem-se esse numero se você multiplicar os numeros ", x_global, " e ", y_global)
