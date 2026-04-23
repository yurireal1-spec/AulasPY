📖 README - Coletor de Estrelas
🎮 Sobre o Jogo
Jogo simples onde você controla um personagem para coletar estrelas douradas. Cada estrela vale 10 pontos. O objetivo é chegar a 200 pontos!

🚀 Como Executar
Método 1 - Direto (Mais fácil)
Salve o código como jogo.html

Dê duplo clique no arquivo

Aguarde carregar (2-3 segundos)

Use as setas do teclado para jogar

Método 2 - Servidor Python
bash
python -m http.server 8000
Depois abra: http://localhost:8000/jogo.html

🎮 Como Jogar
Tecla	Ação
⬆️	Cima
⬇️	Baixo
⬅️	Esquerda
➡️	Direita
🔄 Botão	Reiniciar
Objetivo: Colete as estrelas ⭐ e faça 200 pontos!

🛠️ Tecnologias
Python 3 (Brython)

HTML5/CSS3

Canvas API

📁 Estrutura
text
projeto/
└── jogo.html    # Código completo do jogo
🐛 Problemas Comuns
Problema	Solução
Tela preta	Aguarde carregar ou recarregue (F5)
Teclas não funcionam	Clique dentro do jogo primeiro
Não carrega	Verifique sua internet
📊 Código em Números
Variáveis: 22

Decisões (if): 9

Repetições (loops): 6

Linhas totais: ~180

✅ Requisitos
Navegador moderno (Chrome, Firefox, Edge)

Internet (para carregar o Brython)

JavaScript habilitado

🎯 Personalização Rápida
No código, você pode alterar:

python
# Velocidade do jogador (linha ~47)
PLAYER_SPEED = 5

# Pontuação para vencer (linha ~115)
if score >= 200:

# Número de estrelas (linha ~48)
NUM_STARS = 8
📝 Licença
Livre para estudo e aprendizado.

Divirta-se! ⭐🐍

Arquivo: jogo.html | Python no Navegador