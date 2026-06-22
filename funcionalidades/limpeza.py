import os
import shutil


def limpar_temporarios():

    pasta_temp = os.environ.get(
        "TEMP"
    )

    if not pasta_temp:
        return 0, 0

    apagados = 0
    bloqueados = 0

    for item in os.listdir(
        pasta_temp
    ):

        caminho = os.path.join(
            pasta_temp,
            item
        )

        try:

            if (
                os.path.isfile(caminho)
                or os.path.islink(caminho)
            ):
                os.unlink(caminho)

            elif os.path.isdir(caminho):
                shutil.rmtree(caminho)

            apagados += 1

        except Exception:
            bloqueados += 1

    return apagados, bloqueados