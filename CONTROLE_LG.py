import tkinter as tk
import serial
from tkinter import messagebox

PORTA = "/dev/ttyUSB0"
BAUD = 9600

try:
    arduino = serial.Serial(PORTA, BAUD, timeout=1)
except Exception as e:
    messagebox.showerror("Erro", str(e))
    raise SystemExit

def enviar(cmd):
    arduino.write(cmd.encode())

janela = tk.Tk()
janela.title("Controle LG")
janela.geometry("420x550")
janela.resizable(False, False)

tk.Button(
    janela,
    text="POWER",
    width=20,
    height=2,
    command=lambda: enviar('p')
).pack(pady=10)

# Navegação
frame_nav = tk.Frame(janela)
frame_nav.pack(pady=20)

tk.Button(frame_nav, text="↑", width=8, height=2,
          command=lambda: enviar('u')).grid(row=0, column=1)

tk.Button(frame_nav, text="←", width=8, height=2,
          command=lambda: enviar('l')).grid(row=1, column=0)

tk.Button(frame_nav, text="OK", width=8, height=2,
          command=lambda: enviar('o')).grid(row=1, column=1)

tk.Button(frame_nav, text="→", width=8, height=2,
          command=lambda: enviar('r')).grid(row=1, column=2)

tk.Button(frame_nav, text="↓", width=8, height=2,
          command=lambda: enviar('d')).grid(row=2, column=1)

# Volume e Canal
frame_av = tk.Frame(janela)
frame_av.pack(pady=20)

tk.Label(frame_av, text="Volume").grid(row=0, column=0, padx=30)
tk.Label(frame_av, text="Canal").grid(row=0, column=1, padx=30)

tk.Button(frame_av, text="+", width=8, height=2,
          command=lambda: enviar('+')).grid(row=1, column=0)

tk.Button(frame_av, text="+", width=8, height=2,
          command=lambda: enviar('c')).grid(row=1, column=1)

tk.Button(frame_av, text="-", width=8, height=2,
          command=lambda: enviar('-')).grid(row=2, column=0)

tk.Button(frame_av, text="-", width=8, height=2,
          command=lambda: enviar('x')).grid(row=2, column=1)

# Menu
tk.Button(
    janela,
    text="MENU",
    width=20,
    height=2,
    command=lambda: enviar('m')
).pack(pady=20)

janela.mainloop()