numeros = []
num = 1  # Valor inicial apenas para entrar no loop
#Icrimento para ler números do usuário até que ele digite -999
while num != -9999:
    num = int(input("Digite um número (-9999 para sair): "))
    if num != -9999:
        numeros.append(num)






#função para encontrar o maior número na lista
def encontrar_maior(numeros):
    if not numeros:
        return None       
    maior=numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior



#Função para encontar o menor número na lista
def encontrar_menor(numeros):
    if not numeros:
        return None       
    menor=numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor



#Função para calcular a média dos números na lista
def media(numeros):
    if not numeros:
        return None
    return sum(numeros) / len(numeros) 

def soma(numeros):
    if not numeros:
        return None
    soma1 = 0
    for numero in numeros:
        soma1 += numero
    return soma1

#Função para encontrar a posição de um valor na lista
def posicao(numeros, valor):
    for i in range(len(numeros)):
        if numeros[i] == valor:
            return i
    return -1



#Função para encontrar todas as posições de um valor na lista
def todas_posicoes(numeros, valor):
    indices = []  # Lista vazia para anotar as posições
    
    for i in range(len(numeros)):
        if numeros[i] == valor:
            indices.append(i)  # Achou? Anota o índice 'i' na lista
            
    return indices  # Só retorna depois que o 'for' olhou a lista TODA

#Função para contar quantos números tem na lista
def tamanho(numeros):
    return len(numeros)


#Exibe a lista final e o maior número encontrado
print(f"Lista final: {numeros}")
print(f"O maior número é: {encontrar_maior(numeros)}")
print(f"O menor número é: {encontrar_menor(numeros)}")
print(f"A média dos números é: {media(numeros)}")
print(f"A soma dos números é: {soma(numeros)}")
print(f"A posição do valor 5 é: {posicao(numeros, 5)}")
print(f"As posições do valor 5 são: {todas_posicoes(numeros, 5)}")
print(f"O tamanho da lista é: {tamanho(numeros)}")