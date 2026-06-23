import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from datetime import datetime

from funcionalidades.sistema import obter_info_sistema
from funcionalidades.organizador import organizar_pasta
from funcionalidades.backup import realizar_backup
from funcionalidades.processos import listar_processos
from funcionalidades.limpeza import limpar_temporarios
from funcionalidades.pastas import criar_pastas


def iniciar():

    root = tk.Tk()
    root.title("Central de Automação para Windows")
    root.geometry("720x620")
    root.resizable(False, False)

    # ================= ESTILO =================

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "TButton",
        font=("Segoe UI", 10),
        padding=5
    )

    # ================= LOG =================

    def log(msg):

        horario = datetime.now().strftime("%H:%M:%S")

        log_area.insert(
            tk.END,
            f"[{horario}] {msg}\n"
        )

        log_area.see(tk.END)

    # ================= FUNÇÕES =================

    def abrir_info_sistema():

        try:

            info = obter_info_sistema()

            log("Informações do sistema consultadas.")

            messagebox.showinfo(
                "Informações do Sistema",
                info
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def abrir_organizador():

        pasta = filedialog.askdirectory(
            title="Selecione a pasta"
        )

        if not pasta:
            return

        try:

            quantidade = organizar_pasta(
                pasta
            )

            log(
                f"{quantidade} arquivos organizados."
            )

            messagebox.showinfo(
                "Organização Concluída",
                f"{quantidade} arquivos foram organizados."
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def abrir_backup():

        origem = filedialog.askdirectory(
            title="Selecione a pasta de origem"
        )

        if not origem:
            return

        destino = filedialog.askdirectory(
            title="Selecione onde salvar o backup"
        )

        if not destino:
            return

        try:

            arquivo_zip = realizar_backup(
                origem,
                destino
            )

            log(
                "Backup concluído."
            )

            messagebox.showinfo(
                "Backup Concluído",
                f"Backup salvo em:\n\n{arquivo_zip}"
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def abrir_processos():

        try:

            resultado = listar_processos()

            log(
                "Lista de processos consultada."
            )

            janela = tk.Toplevel(root)

            janela.title(
                "Processos em Execução"
            )

            janela.geometry(
                "900x500"
            )

            texto = scrolledtext.ScrolledText(
                janela,
                font=("Consolas", 10)
            )

            texto.pack(
                fill=tk.BOTH,
                expand=True
            )

            texto.insert(
                tk.END,
                resultado
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def abrir_limpeza():

        resposta = messagebox.askyesno(
            "Confirmação",
            "Deseja limpar os arquivos temporários?"
        )

        if not resposta:
            return

        try:

            apagados, bloqueados = limpar_temporarios()

            log(
                f"{apagados} itens removidos."
            )

            messagebox.showinfo(
                "Limpeza Concluída",
                f"Itens removidos: {apagados}\n"
                f"Itens ignorados: {bloqueados}"
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    # ================= CABEÇALHO =================

    header_frame = tk.Frame(root)
    header_frame.pack(pady=20)

    tk.Label(
        header_frame,
        text="Central de Automação para Windows",
        font=("Segoe UI", 18, "bold")
    ).pack()

    tk.Label(
        header_frame,
        text="Autores: João Pedro Souza, Gabriel Cabral, Luiz, Leo Maciel",
        font=("Segoe UI", 10)
    ).pack(pady=(8, 0))

    tk.Label(
        header_frame,
        text="Curso de Tecnologia da Informação - Porto Alegre / RS",
        font=("Segoe UI", 9, "italic")
    ).pack()

    # ================= BOTÕES =================

    botoes_frame = tk.Frame(root)
    botoes_frame.pack(pady=15)

    BTN_W = 32

    ttk.Button(
        botoes_frame,
        text="🗂️ 1. Organizar Arquivos por Tipo",
        width=BTN_W,
        command=abrir_organizador
    ).grid(row=0, column=0, padx=10, pady=6)

    ttk.Button(
        botoes_frame,
        text="💾 2. Realizar Backup (ZIP)",
        width=BTN_W,
        command=abrir_backup
    ).grid(row=0, column=1, padx=10, pady=6)

    ttk.Button(
        botoes_frame,
        text="🖥️ 3. Informações do Sistema",
        width=BTN_W,
        command=abrir_info_sistema
    ).grid(row=1, column=0, padx=10, pady=6)

    ttk.Button(
        botoes_frame,
        text="⚙️ 4. Listar Processos (PowerShell)",
        width=BTN_W,
        command=abrir_processos
    ).grid(row=1, column=1, padx=10, pady=6)

    ttk.Button(
        botoes_frame,
        text="🧹 5. Limpar Arquivos Temporários",
        width=BTN_W,
        command=abrir_limpeza
    ).grid(row=2, column=0, padx=10, pady=6)

    ttk.Button(
        botoes_frame,
        text="📁 6. Criar pastas",
        width=BTN_W,
        command=criar_pastas
    ).grid(row=2, column=1, padx=10, pady=6)

    # ================= CONSOLE =================

    console_frame = tk.Frame(root)
    console_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(15, 10)
    )

    tk.Label(
        console_frame,
        text="Console de Execução:",
        font=("Segoe UI", 10, "bold")
    ).pack(anchor="w")

    log_area = scrolledtext.ScrolledText(
        console_frame,
        height=12,
        bg="#1b1b1b",
        fg="#00ff00",
        font=("Consolas", 10)
    )

    log_area.pack(
        fill="both",
        expand=True
    )

    log(
        "Sistema inicializado. Aguardando comandos da interface..."
    )

    root.mainloop()