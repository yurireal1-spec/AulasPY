import os
import json

# Caminho da pasta raiz
diretorio_raiz = 'C:/Users/nicol/Desktop/Linux_Pratica'

# Lista que vai guardar todos os dados coletados
dados_agrupados = []

print("Iniciando a leitura dos arquivos...")

# 1. Percorre todas as pastas e subpastas
for root, dirs, files in os.walk(diretorio_raiz):
    for nome_arquivo in files:
        # 2. Filtra apenas os arquivos .txt
        if nome_arquivo.endswith('.txt'):
            caminho_completo = os.path.join(root, nome_arquivo)
            
            try:
                # 3. Abre e lê o conteúdo do arquivo
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                    
                    # Tenta converter o conteúdo de string para um objeto Python (Dicionário/Lista)
                    # Se o conteúdo do TXT for exatamente um JSON, isso aqui funciona:
                    dados_json = json.loads(conteudo)
                    
                    # 4. Adiciona aos nossos dados agrupados
                    dados_agrupados.append(dados_json)
                    
            except Exception as e:
                print(f"Erro ao ler {nome_arquivo}: {e}")

# 5. Salva tudo em um novo arquivo JSON único
with open('resultado_final.json', 'w', encoding='utf-8') as f_out:
    json.dump(dados_agrupados, f_out, indent=4, ensure_ascii=False)

print(f"Sucesso! {len(dados_agrupados)} arquivos foram agrupados em 'resultado_final.json'.")
print(dados_agrupados)git