import os
import shutil
from datetime import datetime


def realizar_backup(origem, destino):

    data_hora = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    nome_backup = (
        f"Backup_{data_hora}"
    )

    caminho_backup = os.path.join(
        destino,
        nome_backup
    )

    shutil.make_archive(
        caminho_backup,
        "zip",
        origem
    )

    return caminho_backup + ".zip"