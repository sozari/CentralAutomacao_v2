import platform


def obter_info_sistema():

    return (
        f"Sistema Operacional: {platform.system()} {platform.release()}\n"
        f"Versão: {platform.version()}\n"
        f"Arquitetura: {platform.machine()}\n"
        f"Processador: {platform.processor()}\n"
        f"Hostname: {platform.node()}"
    )