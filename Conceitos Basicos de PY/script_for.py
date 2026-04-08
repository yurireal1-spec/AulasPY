'''
 Script focado em for para ler e atualizar os arquivos do composer.json de forma simples.
Tenho que ver a lista de bibliotecas mais as versões e preciso padronizar as informações em arquivos próprios.
'''
import os
import json

pasta = "vendor_composers"
arquivos = os.listdir(pasta) # pegar togos os arquivos/pasta que estão dentro de "vendor_composers"


# Vai passar por todos os arquivos que vieram da lista arquivos.
for arquivo in arquivos:
    if arquivo.endswith(".lock"):                               #vai verificar se o arquivo termina com ".lock", o endswith verifica a extensão do arquivo.
        caminho = os.path.join(pasta,arquivo)                   #Junta o caminho da pasta mais o nme do arquivo.
        with open(caminho, "r") as f:                           #open() abre o arquivo para leitura usando o r ou abre para escrita com w, o uso do with é para abrir o arquivo com "segurança" e depois fecha-lo
            dados = json.load(f)                                #Converte o json em python
        require = dados.get("require",{})                       #Pegar o require usando get e retornar {} se não existir
        novo_arquivo = arquivo + "_formatado.lock"              #Cria o nome do novo arquivo de saída.
        with open(novo_arquivo, "w") as out:                    #Abre o arquivo em modo escrita.
            for nome, versao in require.items():                #Esse for percorre todas as dependências, nome → nome da biblioteca; versao → versão da biblioteca
                versao_limpa = versao.replace("^","")           #Remove o caractere ^ da versão para deixá-la em formato mais simples.
                linha = nome + " - " + versao_limpa + "\n"      #Cada dependência é escrita no arquivo no formato: ↧
                out.write(linha)                                #nome-da-lib - versao
        if require:                                             #Verifica se existem dependências no arquivo.
            primeiro = list(require.keys())[0]                  #Obtém o nome da primeira biblioteca, que será usada como identificador do projeto.
            nome_projeto = arquivo + "_projeto.txt"             #Define o nome do arquivo.
            with open(nome_projeto, "w") as out:                #Cria o arquivo e escreve o nome da biblioteca principal.
                out.write(primeiro)                             #''''
print("Arquivos gerados!")
