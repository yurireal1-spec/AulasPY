import pandas as pd
import os
import json

# --- Configurações de Caminho ---
CAMINHO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
PASTA_HISTORICO = os.path.join(CAMINHO_SCRIPT, "historico")
ARQUIVO_JSON = os.path.join(PASTA_HISTORICO, "filmes_catalogo.json")

# Garantir que a pasta exista
os.makedirs(PASTA_HISTORICO, exist_ok=True)

# --- Variáveis Globais ---
dicionario_filmes = {}
contador = 0

class Filme:
    def adicionar(self, nome, lancamento, genero):
        return {
            "nome": nome,
            "lancamento": lancamento,
            "genero": genero
        }

gerenciador = Filme()

# --- Funções de Utilidade ---
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

# --- Lógica do Sistema ---

def adicionar_filme():
    global contador
    while True:
        limpar_tela()
        print("=== Adicionar Novo Filme ao Buffer ===")
        nome = input("Nome do filme: ").strip()
        if not nome: break

        try:
            ano = int(input("Ano de lançamento: "))
        except ValueError:
            print("Erro: Digite um ano válido.")
            pausar(); continue

        gen_raw = input("Gêneros (separados por vírgula): ")
        generos = [g.strip() for g in gen_raw.split(",") if g.strip()]

        dicionario_filmes[contador] = gerenciador.adicionar(nome, ano, generos)
        contador += 1
        
        print(f"\n✔ '{nome}' adicionado à lista de espera.")
        if input("\nAdicionar outro? (s/n): ").lower() != 's': break

def visualizar_buffer():
    limpar_tela()
    print("=== Filmes na Fila de Espera (Ainda não salvos) ===")
    if not dicionario_filmes:
        print("Lista vazia.")
    else:
        df = pd.DataFrame.from_dict(dicionario_filmes, orient="index")
        print(df)
    pausar()


def atualizar_catalogo_json():
    """Junta o que está na memória com o que está no arquivo, removendo duplicados."""
    limpar_tela()
    global dicionario_filmes, contador
    
    if not dicionario_filmes:
        print("Não há filmes novos para atualizar.")
        pausar(); return

    try:
        df_novos = pd.DataFrame.from_dict(dicionario_filmes, orient="index")
        
        if os.path.exists(ARQUIVO_JSON):
            df_antigo = pd.read_json(ARQUIVO_JSON)
            df_final = pd.concat([df_antigo, df_novos], ignore_index=True)
        else:
            df_final = df_novos

        # Remove duplicados pelo nome (ignora maiúsculas/minúsculas se desejar)
        df_final = df_final.drop_duplicates(subset=['nome'], keep='last')
        
        # Salva
        df_final.to_json(ARQUIVO_JSON, orient="records", indent=4, force_ascii=False)
        
        # LIMPEZA: Após salvar, limpamos a memória
        dicionario_filmes.clear()
        contador = 0
        
        print(f"✅ Catálogo atualizado com sucesso em: {ARQUIVO_JSON}")
    except Exception as e:
        print(f"❌ Erro ao atualizar: {e}")
    pausar()

def visualizar_catalogo_completo():
    limpar_tela()
    print("=== Catálogo Oficial (Arquivo JSON) ===")
    if os.path.exists(ARQUIVO_JSON):
        try:
            df = pd.read_json(ARQUIVO_JSON)
            if df.empty:
                print("O arquivo está vazio.")
            else:
                print(df)
                print(f"\nTotal de filmes: {len(df)}")
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
    else:
        print("Arquivo JSON ainda não foi criado.")
    pausar()


def excluir_filme_json():
    limpar_tela()
    print("=== Excluir Filme do Catálogo Oficial ===")
    
    # 1. Verifica se o arquivo existe
    if not os.path.exists(ARQUIVO_JSON):
        print("❌ O catálogo ainda não existe. Não há nada para excluir.")
        pausar()
        return

    try:
        # 2. Carrega o catálogo atual
        df = pd.read_json(ARQUIVO_JSON)
        
        if df.empty:
            print("❌ O catálogo está vazio.")
            pausar()
            return
        
        # Mostra o catálogo para o usuário escolher
        print(df)
        print("-" * 50)
        
        # 3. Pede o nome do filme a ser deletado
        nome_excluir = input("\nDigite o nome exato do filme que deseja excluir (ou Enter para cancelar): ").strip()
        
        if not nome_excluir:
            return  # Cancela e volta para o menu

        # 4. Verifica se o filme realmente existe no DataFrame
        filme_existe = df['nome'].str.lower() == nome_excluir.lower()
        
        if not filme_existe.any():
            print(f"\n❌ O filme '{nome_excluir}' não foi encontrado no catálogo.")
        else:
            # --- NOVA CAMADA DE CONFIRMAÇÃO ---
            print(f"\n⚠ ATENÇÃO: Você está prestes a deletar '{nome_excluir}' permanentemente.")
            confirmacao = input("Para confirmar, digite o nome do filme novamente: ").strip()
            
            # Compara a confirmação (também ignorando maiúsculas/minúsculas)
            if confirmacao.lower() != nome_excluir.lower():
                print("\n❌ Confirmação incorreta! Operação de exclusão cancelada.")
                pausar()
                return
            # ----------------------------------

            # 5. Se passou na confirmação, filtra o DataFrame
            df_atualizado = df[df['nome'].str.lower() != nome_excluir.lower()]
            
            # 6. Salva o arquivo JSON atualizado
            df_atualizado.to_json(ARQUIVO_JSON, orient="records", indent=4, force_ascii=False)
            print(f"\n✅ '{nome_excluir}' foi removido com sucesso do catálogo!")
            
    except Exception as e:
        print(f"❌ Erro ao processar a exclusão: {e}")
        
    pausar()
    limpar_tela()
    print("=== Excluir Filme do Catálogo Oficial ===")
    
    # 1. Verifica se o arquivo existe
    if not os.path.exists(ARQUIVO_JSON):
        print("❌ O catálogo ainda não existe. Não há nada para excluir.")
        pausar()
        return

    try:
        # 2. Carrega o catálogo atual
        df = pd.read_json(ARQUIVO_JSON)
        
        if df.empty:
            print("❌ O catálogo está vazio.")
            pausar()
            return
        
        # Mostra o catálogo atual para o usuário ver o que pode excluir
        print(df)
        print("-" * 50)
        
        # 3. Pede o nome do filme a ser deletado
        nome_excluir = input("\nDigite o nome exato do filme que deseja excluir (ou Enter para cancelar): ").strip()
        
        if not nome_excluir:
            return  # Cancela e volta para o menu

        # 4. Verifica se o filme realmente existe no DataFrame
        # Usamos .str.lower() para evitar problemas com maiúsculas/minúsculas
        filme_existe = df['nome'].str.lower() == nome_excluir.lower()
        
        if not filme_existe.any():
            print(f"\n❌ O filme '{nome_excluir}' não foi encontrado no catálogo.")
        else:
            # 5. Filtra o DataFrame mantendo apenas os filmes que NÃO têm esse nome
            df_atualizado = df[df['nome'].str.lower() != nome_excluir.lower()]
            
            # 6. Salva o arquivo JSON com os dados atualizados
            df_atualizado.to_json(ARQUIVO_JSON, orient="records", indent=4, force_ascii=False)
            print(f"\n✅ '{nome_excluir}' foi removido com sucesso do catálogo!")
            
    except Exception as e:
        print(f"❌ Erro ao processar a exclusão: {e}")
        
    pausar()





# --- Menu Principal ---
while True:
    limpar_tela()
    print("=" * 50)
    print("      SISTEMA DE GERENCIAMENTO NETFLIX TURBO")
    print("=" * 50)
    print("1 - Adicionar filmes (Memória)")
    print("2 - Ver filmes na fila de espera")
    print("3 - SALVAR/ATUALIZAR Catálogo (JSON)")
    print("4 - VER Catálogo Completo (JSON)")
    print("5 - Excluir Filme Dentro do (JSON)")
    print("10 - Sair")
    print("-" * 50)
    
    op = input("Escolha: ")

    if   op == "1": adicionar_filme()
    elif op == "2": visualizar_buffer()
    elif op == "3": atualizar_catalogo_json()
    elif op == "4": visualizar_catalogo_completo()
    elif op == "5": excluir_filme_json()
    elif op == "10": 
        print("Encerrando..."); break
    else:
        print("Opção inválida."); pausar()
        