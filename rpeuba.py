import tkinter as tk
import tkinter.ttk as ttk
from formulario import Formulario
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        # Crear un Treeview con tres columnas
        self.treeview = ttk.Treeview(self, columns=("Nombre", "Edad", "Correo electrónico"))

        # Agregar encabezados de columna
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Edad")
        self.treeview.heading("#3", text="Correo electrónico")

        # Agregar algunos datos iniciales al Treeview
        self.treeview.insert("", "end", text="1", values=("Juan", "25", "juan@example.com"))
        self.treeview.insert("", "end", text="2", values=("María", "30", "maria@example.com"))

        # Crear un formulario para ingresar nuevos datos
        self.formulario = Formulario(self, self.treeview)

        # Posicionar el Treeview y el formulario
        self.treeview.pack()
        self.formulario.pack()

if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()