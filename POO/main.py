from Classes import *

print('\n')

jogador_generico=Jogador(nome="Neymar", camisa=9, posicao="Cozinheiro", titular=False, time="Santos")
jogador_generico.se_apresente()
jogador_generico.correr()
jogador_generico.passar_bola(direcao="direita")
print('\n')
print('\n')

atacante=Atacante(nome="Cristiano Ronaldo", camisa=7, posicao="Atacante", titular=False, time="Flamengo")
atacante.se_apresente()
atacante.correr()
atacante.passar_bola(direcao="frente")
atacante.chutar_a_gol()

print('\n')
print('\n')

goleiro=Goleiro(nome="Cassio", camisa=11, posicao="Goleiro",  time="Corinthians")
goleiro.se_apresente()
goleiro.correr()
goleiro.agarrar_bola()
goleiro.passar_bola(direcao="esquerda")
