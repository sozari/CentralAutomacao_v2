# Biblioteca para trabalhar com pastas e caminhos
import os

# Importa as janelas prontas do Tkinter
from tkinter import filedialog, messagebox, simpledialog



def criar_pastas():

    # Abre uma janela para o usuário escolher
    # onde a nova pasta será criada
    pasta = filedialog.askdirectory(
        title="Escolha onde criar a pasta"
    )

    # Se o usuário cancelar a seleção
    if not pasta:
        return

    # Abre uma caixa de texto para digitar
    # o nome da nova pasta
    nome_pasta = simpledialog.askstring(
        "Nome da Pasta",
        "Digite o nome da pasta:"
    )

    # Se o usuário cancelar ou deixar vazio
    if not nome_pasta:
        return

    # Junta o caminho escolhido com o nome digitado
    # Ex:
    # C:\Users\Joao\Desktop + MinhaPasta
    caminho = os.path.join(
        pasta,
        nome_pasta
    )

    # Cria a pasta
    # exist_ok=True evita erro caso ela já exista
    os.makedirs(
        caminho,
        exist_ok=True
    )

    # Mostra uma mensagem de sucesso
    messagebox.showinfo(
        "Sucesso",
        f"Pasta criada:\n{caminho}"
    )