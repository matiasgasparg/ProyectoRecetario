import tkinter as tk
from tkinter import ttk
class Secundaria(ttk.Frame):
 def __init__(self, parent):
    super().__init__(parent, padding=(20))
    parent.title("Ventana Secundaria")
    parent.geometry("350x100+180+100")
    self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
    parent.columnconfigure(0, weight=1)
    parent.rowconfigure(0, weight=1)
    parent.resizable(False, False)
    ttk.Button(self, text="Cerrar", command=parent.destroy).grid()
root = tk.Tk()
App(root).grid()
root.mainloop()