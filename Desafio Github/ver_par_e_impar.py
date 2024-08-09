# Verificando Números Pares e Ímpares 

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "O número {} é par.".format(numero)
    else:
        return "O número {} é ímpar.".format(numero)

numero = int(input("Digite um número: "))

resultado = verificar_par_impar(numero)

print(resultado)