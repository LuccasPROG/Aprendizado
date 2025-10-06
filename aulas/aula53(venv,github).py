# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

"""
📌 Colinha de comandos Python/venv/pip e Git/GitHub
Salve esse arquivo e consulte sempre que precisar!
"""

# ==============================
# Python / Venv / Pip
# ==============================

# Criar e ativar venv
# python -m venv venv           # cria o venv na pasta "venv"
# .\venv\Scripts\Activate.ps1   # ativa o venv no PowerShell
# deactivate                     # desativa o venv

# Instalar pacotes
# pip install pacote             # instala um pacote dentro do venv
# pip install -r requirements.txt # instala todos os pacotes do arquivo

# Conferir pacotes
# pip freeze                     # lista todos os pacotes do venv
# pip freeze > requirements.txt  # atualiza o requirements.txt

# Atualizar pacotes
# pip install --upgrade pacote   # atualiza um pacote específico

# Dicas importantes
# - Sempre ativar o venv antes de rodar scripts
# - Sempre atualizar o requirements.txt após instalar ou atualizar pacotes

# ==============================
# Git / GitHub
# ==============================

# Configurações iniciais
# git config --global user.name "SeuNome"
# git config --global user.email "seuemail@exemplo.com"

# Criar / iniciar repositório
# git init                        # inicia repositório git
# git clone url-do-repositorio     # clona um repositório existente

# Adicionar / confirmar alterações
# git status                       # vê mudanças
# git add .                        # adiciona tudo para o próximo commit
# git commit -m "mensagem"         # cria commit com mensagem

# Enviar para o GitHub
# git branch -M main               # define branch principal como main
# git remote add origin url        # conecta com GitHub
# git push -u origin main          # envia alterações pro GitHub
# git push -u origin main --force  # força envio (cuidado)

# Atualizar / puxar alterações
# git pull origin main             # puxa alterações do GitHub
# git fetch                        # atualiza info do repositório remoto

# Outros comandos úteis
# git log                           # vê histórico de commits
# git checkout nome-do-arquivo      # volta um arquivo específico
# git reset --hard                  # volta tudo para o último commit (cuidado)

# ==============================
# Dica de ouro
# ==============================
# Salve esse arquivo no seu projeto ou pasta de estudos.
# Abra sempre que esquecer algum comando.