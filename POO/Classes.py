class Jogador:
    def __init__(self, nome: str, time: str, camisa: int, posicao: str, titular=False):
        self.nome = nome
        self.time = time
        self.camisa = camisa
        self.posicao = posicao
        self.titular = titular

    def se_apresente(self):
        print(f"Prazer! Me chamo {self.nome}, sou camisa {self.camisa} {self.posicao} {'Titular'if self.titular else 'Reseva'} do {self.time}!")
    
    def correr(self):
        print(f"O jogador {self.nome} está correndo!")

    def passar_bola(self, direcao: str):
        
        direcao = direcao.lower() 
        
        if direcao == "direita":
            print("Tocou a bola para a Direita")
        elif direcao == "frente":
            print("Tocou a bola para a Frente")
        elif direcao == "esquerda":
            print("Tocou a bola para a Esquerda")
        else:
            print("Direção de passe inválida!")

# HERANÇA: Atacante herda tudo de Jogador
class Atacante(Jogador):
    # POLIMORFISMO: Modifica o método correr para algo mais específico de atacante
    def correr(self):
        print(f"O atacante {self.nome} está dando um pique em direção à área!")
        
    # Método exclusivo da classe Atacante
    def chutar_a_gol(self):
        print(f"{self.nome} soltou a bomba para o gol!")


# HERANÇA: Goleiro herda tudo de Jogador
class Goleiro(Jogador):
    # POLIMORFISMO: Modifica o método correr (goleiro corre diferente)
    def correr(self):
        print(f"O goleiro {self.nome} está correndo de lado para fechar o ângulo.")
        
    # Método exclusivo da classe Goleiro
    def agarrar_bola(self):
        print(f"{self.nome} fez uma grande defesa e segurou a bola!")