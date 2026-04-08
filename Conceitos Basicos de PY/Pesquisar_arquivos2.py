import os
import json

# 1. Definição da origem
# Usamos o caminho absoluto para garantir que o script saiba exatamente onde começar.
diretorio_raiz = 'C:/Users/nicol/Downloads' 
arquivos_csv = []  # Lista que servirá como nosso "banco de dados" temporário.

"""
POR QUE OS.WALK EM VEZ DE OS.LISTDIR?
O os.listdir() apenas "olha" o que está na superfície da pasta. 
O os.walk() é um gerador que realiza uma VARREDURA RECURSIVA: ele entra na pasta,
lista o que tem nela, e se encontrar uma subpasta, ele entra nela também, 
repetindo o processo até chegar ao fim da "árvore" de diretórios.
"""

for rota, pastas, arquivos in os.walk(diretorio_raiz):
    # O os.walk nos devolve três informações a cada passo:
    # 'rota'   -> O caminho da pasta atual onde ele está.
    # 'pastas' -> Uma lista com as subpastas daquela rota.
    # 'arquivos'-> Uma lista com os nomes de todos os arquivos naquela rota.

    for nome_arquivo in arquivos:
        # Filtro de Extensão:
        # O endswith() funciona como um filtro lógico (booleano).
        # Adicionei o .lower() para garantir que ele encontre tanto ".csv" quanto ".CSV".
        if nome_arquivo.lower().endswith(".csv"):
            
            # Montagem do Caminho (Path Joining):
            # Não concatenamos strings com + (ex: rota + nome_arquivo) porque o os.path.join
            # gerencia automaticamente as barras invertidas (/) de acordo com o sistema operacional.
            caminho_completo = os.path.join(rota, nome_arquivo)
            
            # Armazenamento:
            # Guardamos o caminho completo para que, futuramente, o Python possa abrir 
            # o arquivo sem precisar saber em qual pasta ele estava originalmente.
            arquivos_csv.append(caminho_completo)
            try:
                with open(caminho_completo,'r',encoding="utf-8") as f:
                    conteudo=f.read()
                    print(f"--- Conteúdo de: {nome_arquivo} ---")
                    print(conteudo)
            except Exception as e:
                print(f"errro ao ler {caminho_completo}:{e}")






# Exibição dos Resultados
print(f"Varredura concluída. Encontrados {len(arquivos_csv)} arquivos CSV.")
print("-" * 30)
for caminho in arquivos_csv:
    print(f"Localizado: {caminho}")

        