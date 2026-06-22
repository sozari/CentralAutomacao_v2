import subprocess
import platform


def listar_processos():

    comando = (
        "Get-Process | "
        "Sort-Object CPU -Descending | "
        "Select-Object -First 15 Name, Id, CPU | "
        "Format-Table -AutoSize"
    )

    flags = (
        subprocess.CREATE_NO_WINDOW
        if platform.system() == "Windows"
        else 0
    )

    resultado = subprocess.run(
        ["powershell", "-Command", comando],
        capture_output=True,
        text=True,
        creationflags=flags
    )

    return resultado.stdout