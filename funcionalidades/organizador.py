import os
import shutil

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Executaveis": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"]
}


def organizar_pasta(caminho):

    total = 0

    for arquivo in os.listdir(caminho):

        caminho_arquivo = os.path.join(caminho, arquivo)

        if os.path.isdir(caminho_arquivo):
            continue

        extensao = os.path.splitext(arquivo)[1].lower()

        categoria = "Outros"

        for nome, extensoes in CATEGORIAS.items():

            if extensao in extensoes:
                categoria = nome
                break

        pasta_destino = os.path.join(caminho, categoria)

        os.makedirs(
            pasta_destino,
            exist_ok=True
        )

        shutil.move(
            caminho_arquivo,
            os.path.join(
                pasta_destino,
                arquivo
            )
        )

        total += 1

    return total