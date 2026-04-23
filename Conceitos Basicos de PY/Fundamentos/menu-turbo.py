import subprocess as sp
import pandas as pd
import os

dicionariofilmes={}
p=""
i=0 

class Filme:
    def adicionar(self,nome,lancamento,genero):
        return{
            "nome":nome,
            "lancamento":lancamento,
            "genero":genero 
        }
        

gerenciador = Filme()        


while True:
    sp.run("cls", shell=True)

    print("            === Menu de Listagem === \n")
    print('*' * 50)
    print("1 - Adicionar novo filme")
    print("2 - Tabela Filmes")
    print("3 - Listar arquivos com detalhes")
    print("4 - Sair \n")

    opcao=input("Escolha um opção: ")


    if opcao == "1":
        os.system('cls')
        print("               ==Adicionar filmes==")
        print("Adicionar filmes")
        n=input("Nome do filme:  ")
        l=int(input("Data de lançamento:  "))
        g=input("Genero:  ").split(",")

        temp=[n, l, g]

        nome, lancamento, genero= temp

        dt=gerenciador.adicionar(nome,lancamento,genero)
        dicionariofilmes[i] = dt
        i += 1
        p = input("Digite 'fim' para parar ou Enter para continuar: ").lower()

        print(f"Filme {nome}, foi adicionado!")
        
    
    elif opcao == "2":
        if len(dicionariofilmes)==0:

            print("\n\nNenhum filme cadastrado.")
        
        else:

            df=pd.DataFrame.from_dict(dicionariofilmes, orient="index")

            print("teste dos dados")
            print(df)
        input("\n Pressione Enter para voltar ao menu...")