import tkinter as tk
import tkinter.ttk as ttk
import csv
import os
class EditRowWindow(tk.Toplevel):
    def __init__(self, parent, values):
        super().__init__(parent)
        self.title("Editar Fila")
        self.geometry("400x200")

        # Label y Entry para el tiempo de preparación
        self.prep_time_label = tk.Label(self, text="Tiempo de preparación:")
        self.prep_time_label.pack(padx=5, pady=5)
        self.prep_time_entry = tk.Entry(self)
        self.prep_time_entry.pack(padx=5, pady=5)
        self.prep_time_entry.insert(0, values[1])

        # Label y Entry para el tiempo de cocción
        self.cook_time_label = tk.Label(self, text="Tiempo de cocción:")
        self.cook_time_label.pack(padx=5, pady=5)
        self.cook_time_entry = tk.Entry(self)
        self.cook_time_entry.pack(padx=5, pady=5)
        self.cook_time_entry.insert(0, values[2])

        # Label y Entry para la fecha de creación
        self.creation_date_label = tk.Label(self, text="Fecha de creación:")
        self.creation_date_label.pack(padx=5, pady=5)
        self.creation_date_entry = tk.Entry(self)
        self.creation_date_entry.pack(padx=5, pady=5)
        self.creation_date_entry.insert(0, values[3])

        # Checkbox para el favorito
        self.favorite_var = tk.BooleanVar(value=bool(values[4]))
        self.favorite_checkbox = tk.Checkbutton(self, text="Favorito", variable=self.favorite_var)
        self.favorite_checkbox.pack(padx=5, pady=5)

        # Botón para guardar cambios
        self.save_button = tk.Button(self, text="Guardar", command=self.save_changes)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para cancelar cambios
        self.cancel_button = tk.Button(self, text="Cancelar", command=self.cancel_changes)
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Índice seleccionado en el TreeView
        self.selected_index = parent.selected_index

        # Referencia al TreeView padre
        self.parent = parent

    def save_changes(self):
        # Obtener valores de los Entry y el Checkbox
        prep_time = self.prep_time_entry.get()
        cook_time = self.cook_time_entry.get()
        creation_date = self.creation_date_entry.get()
        favorite = self.favorite_var.get()

        # Actualizar valores de la fila seleccionada en el TreeView
        self.parent.treeview.item(self.selected_index, values=["", prep_time, cook_time, creation_date, favorite])

        # Cerrar ventana
        self.destroy()

    def cancel_changes(self):
        # Cerrar ventana sin guardar cambios
        self.destroy()