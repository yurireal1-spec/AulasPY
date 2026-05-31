'''
# 1 - imprime um nome completo
def imprime_nome(pnome,psobrenome):
    print(f" *** {pnome} {psobrenome} ***")

imprime_nome("Anderson","Amaral")

# 2 - Função para somar dois números

def soma_dois(p1,p2):
    r= p1+p2

    return r
n1 = 10
n2 = 15
print(f" {n1} + {n2} = {soma_dois(n1,n2)}")

# 3 - Função com parâmetroe valor default

def endereco(pais = "Brasil"):
    print(f"Eu moro em: {pais}")

endereco("Uruguai")    

def avalia_filme(pfilme,pqtd):
    print(f"Avaliação do filme {pfilme}")
    total=0
    for i in range(1,pqtd+1):
        avaliacao = int(input(f"Digite a {i}ª nota: "))
        total+=avaliacao
    if pqtd>0:
        media = total/pqtd
    else:
        media = 0
    
    print(f"A média de avaliações do filme {pfilme} = {media:.2f}")

avalia_filme ("MIB",4)
'''
'''
# Exemplo de (*args).
# Internamente, destinos = ("Paris", "Londres", "Tóquio")
def viajar(*destinos):
    for destino in destinos:
        print(f"Próxima parada: {destino}")

viajar("Paris", "Londres", "Tóquio") 

'''

#Exemplo de (**Kwargs).
# Internamente, dados = {"nome": "Leo", "cor_tema": "Azul", "nivel": 10}

def configurar_perfil(**dados):
    if "cor_tema" in dados:
        print(f"Definindo cor para: {dados['cor_tema']}")
    print(f"Dados recebidos: {dados}")

configurar_perfil(nome="Leo", cor_tema="Azul", nivel=10)
