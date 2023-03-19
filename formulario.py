import tkinter as tk
import tkinter.ttk as ttk

class Formulario(tk.Frame):
    def __init__(self, master, treeview):
        super().__init__(master)

        self.treeview = treeview

        # Crear elementos del formulario
        nombre_label = tk.Label(self, text="Nombre")
        self.nombre_entry = tk.Entry(self)
        edad_label = tk.Label(self, text="Edad")
        self.edad_entry = tk.Entry(self)
        correo_label = tk.Label(self, text="Correo electrónico")
        self.correo_entry = tk.Entry(self)
        guardar_boton = tk.Button(self, text="Guardar", command=self.guardar_datos)

        # Posicionar elementos del formulario
        nombre_label.grid(row=0, column=0)
        self.nombre_entry.grid(row=0, column=1)
        edad_label.grid(row=1, column=0)
        self.edad_entry.grid(row=1, column=1)
        correo_label.grid(row=2, column=0)
        self.correo_entry.grid(row=2, column=1)
        guardar_boton.grid(row=3, column=1)

    def guardar_datos(self):
        # Obtener los datos del formulario
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        correo = self.correo_entry.get()

        # Obtener el índice del último elemento del Treeview
        ultimo_item = self.treeview.get_children()[-1] if self.treeview.get_children() else None
        ultimo_numero = int(ultimo_item[1:]) if ultimo_item is not None else -1
        nuevo_indice = ultimo_numero + 1

        # Agregar una nueva fila al Treeview
        self.treeview.insert("", str(nuevo_indice), text=str(nuevo_indice), values=(nombre, edad, correo))

        # Limpiar el formulario
        self.nombre_entry.delete(0, "end")
        self.edad_entry.delete(0, "end")
        self.correo_entry.delete(0, "end")