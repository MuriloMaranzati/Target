# Resolução pergunta 5:

# Lista para guardar a cadeia de caracteres da palavra.
caracteres = []

# Pede uma palavra e lê o tamanho da mesma.
string = str(input("Digite uma palavra: "))
tam = len(string)

# inverte a ordem dos caracteres com base no tamanho.
while tam > 0:
    tam -= 1
    caracteres.append(tam)

# Mostra o resultado com a palavra inversa.
print('Palavra invertida: ', end='')
for inverso in caracteres:
    print(string[inverso], end='')
