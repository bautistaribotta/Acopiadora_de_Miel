import tkinter as tk
from tkinter import ttk

# Colores y fuentes
COLOR_BG = "#1E1E1E"
COLOR_PANEL = "#2C2C2C"
COLOR_INPUT_BG = "#3A3A3A"
COLOR_TEXT = "#FFFFFF"
FUENTE = ("Segoe UI", 12)

def centrar(ventana, w, h):
    sw = ventana.winfo_screenwidth()
    sh = ventana.winfo_screenheight()
    x = int(sw/2 - w/2)
    y = int(sh/2 - h/2 - 40)
    ventana.geometry(f"{w}x{h}+{x}+{y}")

def login_ui():
    root = tk.Tk()
    root.title("Login")
    root.configure(bg=COLOR_BG)
    root.resizable(False, False)
    centrar(root, 700, 380)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TEntry",
                    padding=6,
                    foreground=COLOR_TEXT,
                    fieldbackground=COLOR_INPUT_BG,
                    background=COLOR_INPUT_BG,
                    borderwidth=0,
                    relief="flat",
                    font=FUENTE)

    style.configure("TButton",
                    padding=8,
                    foreground=COLOR_TEXT,
                    background="#5A5AE6",
                    font=("Segoe UI", 12, "bold"))
    style.map("TButton",
              background=[("active", "#4848C9")])

    style.configure("TCombobox",
                    padding=6,
                    foreground=COLOR_TEXT,
                    fieldbackground=COLOR_INPUT_BG,
                    background=COLOR_INPUT_BG,
                    borderwidth=0,
                    arrowcolor=COLOR_TEXT,
                    font=FUENTE)

    panel = tk.Frame(root, bg=COLOR_PANEL)
    panel.place(relx=0.5, rely=0.5, anchor="center", width=320, height=300)

    titulo = tk.Label(panel, text="Iniciar Sesión", bg=COLOR_PANEL,
                      fg=COLOR_TEXT, font=("Segoe UI", 18, "bold"))
    titulo.pack(pady=(20, 25))

    combo = ttk.Combobox(panel,
                         values=["Administrador", "Usuario"],
                         state="readonly")
    combo.current(1)
    combo.pack(fill="x", padx=40, pady=10)

    entry_pass = ttk.Entry(panel, show="*")
    entry_pass.insert(0, "Contraseña")
    entry_pass.pack(fill="x", padx=40, pady=10)

    btn = ttk.Button(panel, text="Entrar")
    btn.pack(fill="x", padx=40, pady=25)

    root.mainloop()

login_ui()
